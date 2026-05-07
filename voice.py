import win32com.client as wincl

def speak(text):
    print(f"CHITHRA: {text}")
    speak_engine = wincl.Dispatch("SAPI.SpVoice")
    speak_engine.Speak(text)