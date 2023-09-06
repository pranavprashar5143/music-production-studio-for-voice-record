import pyaudio
import wave

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the recording stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Record audio
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording")

# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
audio.terminate()

# Save the recorded audio to a WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio saved as {OUTPUT_FILENAME}")

# Play the recorded audio
import pygame
pygame.init()
pygame.mixer.music.load(OUTPUT_FILENAME)
pygame.mixer.music.play()

input("Press Enter to exit...")

# Clean up
pygame.mixer.music.stop()
pygame.quit()