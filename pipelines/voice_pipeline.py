from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np 
import io
import librosa
import streamlit as st


@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        st.error('Voice recog error')
        return None
    

def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None, 0.0

    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():
        stored_embedding = np.asarray(stored_embedding, dtype=np.float32)

        similarity = np.dot(new_embedding, stored_embedding)

        print(f"Student {sid}: {similarity}")

        if similarity > best_score:
            best_score = similarity
            best_sid = sid

    print(f"Best Match -> Student: {best_sid}, Score: {best_score}")

    if best_score >= threshold:
        return best_sid, best_score

    return None, best_score


def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.40):
    try:
        print("=" * 60)
        print("ENTERED process_bulk_audio")

        encoder = load_voice_encoder()

        # Load audio
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        print("Audio loaded")
        print("Sample rate:", sr)
        print("Audio duration:", len(audio) / sr)

        # Split audio into speech segments
        segments = librosa.effects.split(audio, top_db=30)

        print("Number of segments:", len(segments))
        print("Segments:", segments)

        identified_results = {}

        for start, end in segments:
            duration = (end - start) / sr
            print(f"\nSegment duration: {duration:.2f}s")

            if duration < 0.5:
                print("Skipped (too short)")
                continue

            print("Processing segment...")

            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)

            embedding = encoder.embed_utterance(wav)
            embedding = np.asarray(embedding, dtype=np.float32)
            embedding /= np.linalg.norm(embedding)

            best_sid = None
            best_score = -1.0

            for sid, stored_embedding in candidates_dict.items():
                stored_embedding = np.asarray(stored_embedding, dtype=np.float32)
                stored_embedding /= np.linalg.norm(stored_embedding)

                similarity = np.dot(embedding, stored_embedding)

                print(f"Student {sid}: {similarity:.4f}")

                if similarity > best_score:
                    best_score = similarity
                    best_sid = sid

            print(f"Best match: {best_sid}, Score: {best_score:.4f}")

            if best_score >= threshold:
                if (
                    best_sid not in identified_results
                    or best_score > identified_results[best_sid]
                ):
                    identified_results[best_sid] = best_score

        print("=" * 60)
        print("Final detected:", identified_results)
        return identified_results

    except Exception as e:
        print("VOICE ERROR:", repr(e))
        st.exception(e)
        return {}