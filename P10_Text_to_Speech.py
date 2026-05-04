from gtts import gTTS
import os

text = input("Enter the text you want to convert to speech: ")

language = "en"

speech = gTTS(text=text, lang=language, slow=False)

output_file = "speech.mp3"
speech.save(output_file)

print(f"\nSpeech saved successfully as '{output_file}'")
print("Open the file in your project to listen to the audio.")

