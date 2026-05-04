import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello World")

a = ["Keshav","Raj","Rahul","Rohan"]

for i in a:
  speaker.Speak(f" Hello {i}")