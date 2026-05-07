from voice import speak
from brain import get_ai_response

def main():
    print("--- CHITHRA AI INITIALIZED ---")
    speak("Hello Sir, I am online. How can I help you?")

    while True:
        # User ගෙන් input එකක් ගන්නවා
        user_input = input("\nYou: ").strip()

        # අයින් වෙන්න ඕනේ නම්
        if user_input.lower() in ["exit", "bye", "stop"]:
            speak("Goodbye Sir! Turning off systems.")
            break

        if user_input:
            print("Thinking...")
            # Gemini ගෙන් උත්තරය ඉල්ලනවා
            ai_reply = get_ai_response(user_input)

            clean_reply = ai_reply.replace("*", "").replace("#", "")
    
            speak(clean_reply)

if __name__ == "__main__":
    main()