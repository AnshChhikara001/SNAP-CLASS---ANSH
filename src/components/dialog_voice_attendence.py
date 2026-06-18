import streamlit as st
import pandas as pd
from datetime import datetime

import src.pipelines.voice_pipeline as vp
from src.database.config import supabase

from src.components.dialog_attendance_records import attendance_result_dialog


@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):
    st.write(
        "Record audio of students saying 'I am present'. Then AI will recognize the students."
    )

    audio_data = st.audio_input(
        "Record classroom audio",
        key=f"voice_audio_{selected_subject_id}"
    )
    if st.button(
        "Analyze Audio",
        key=f"analyze_audio_{selected_subject_id}",
        width="stretch",
        type="primary",
    ):
    
        with st.spinner("Processing audio data..."):

            enrolled_res = (
                supabase.table("subject_students")
                .select("*, students(*)")
                .eq("subject_id", selected_subject_id)
                .execute()
            )

            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning("No students enrolled in this course")
                return

            candidates_dict = {
                s["students"]["student_id"]: s["students"]["voice_embedding"]
                for s in enrolled_students
                if s["students"].get("voice_embedding")
            }

            if not candidates_dict:
                st.error("No enrolled students have voice profiles registered.")
                return

            if audio_data is None:
                st.error("Please record classroom audio first.")
                return

            audio_bytes = audio_data.read()

            print("Audio bytes type:", type(audio_bytes))
            print("Audio bytes length:", len(audio_bytes))
            print("Candidates:", candidates_dict)

            print("VOICE PIPELINE FILE:", vp.__file__)
            detected_scores = vp.process_bulk_audio(audio_bytes, candidates_dict)
            print("Detected scores:", detected_scores)

            results = []
            attendance_to_log = []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node["students"]

                print("Detected:", detected_scores)
                print("Student ID:", student["student_id"], type(student["student_id"]))

                if detected_scores:
                    print("Keys:", list(detected_scores.keys()))
                    print("Key type:", type(next(iter(detected_scores.keys()))))
                else:
                    print("No speakers detected")
                student_result = detected_scores.get(student["student_id"])

                if student_result:
                    score = student_result["confidence"]
                    is_present = True
                else:
                    score = 0.0
                    is_present = False

                results.append(
                    {
                        "Name": student["name"],
                        "ID": student["student_id"],
                        "Confidence": f"{score:.2%}" if is_present else "-",
                        "Status": "✅ Present" if is_present else "❌ Absent",
                    }
                )
                attendance_to_log.append(
                    {
                        "student_id": student["student_id"],
                        "subject_id": selected_subject_id,
                        "timestamp": current_timestamp,
                        "is_present": is_present,
                    }
                )

            st.session_state.voice_attendance_results = (
                pd.DataFrame(results),
                attendance_to_log,
            )

    if st.session_state.get("voice_attendance_results"):
        st.success("Audio processed successfully.")
        st.info("Close this dialog to view the attendance results.")