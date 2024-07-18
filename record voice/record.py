import sounddevice as sd
import wavio

def record_audio(duration, sample_rate):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    return audio_data

def save_audio(audio_data, sample_rate, filename):
    wavio.write(filename, audio_data, sample_rate, sampwidth=2)
    print(f"Audio saved to {filename}")

def main():
    duration = int(input("Enter the duration of the recording in seconds: "))
    sample_rate = 44100  # Sample rate in Hz (standard for high-quality audio)
    filename = input("Enter the filename to save the recording (e.g., 'output.wav'): ")

    audio_data = record_audio(duration, sample_rate)
    save_audio(audio_data, sample_rate, filename)

if __name__ == "__main__":
    main()
