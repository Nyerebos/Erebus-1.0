import deepspeech
import pvporcupine
import pyaudio

def detect_wake_word(keyword_path):
    porcupine = pvporcupine.create(
        library_path=pvporcupine.LIBRARY_PATH,
        model_path=keyword_path
    )

    ds = deepspeech.Model('path/to/your/deepspeech/model/deepspeech-0.9.3-models.pbmm')

    audio_stream = pyaudio.PyAudio().open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = pcm.frombuffer(pcm, dtype=int)

        if porcupine.process(pcm) >= 0:
            print("Wake word detected!")
            text = ds.stt(pcm)
            if text:
                return text

if __name__ == '__main__':
    wake_word_model_path = 'path/to/your/wake/word/model.ppn'
    detected_text = detect_wake_word(wake_word_model_path)
    print(f"Detected Text: {detected_text}")




