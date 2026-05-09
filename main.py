from voice import speak
from brain import get_ai_response
from processor import check_local_intent 
import pyautogui
import time

def main():
    print("--- CHITHRA AI INITIALIZED ---")
    speak("Hello Sir, how can I help you?")

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input: continue
        
        if user_input.lower() in ["exit", "bye"]: break

        intent, target = check_local_intent(user_input)

        if intent == "OS_OPEN_APP":
            speak(f"Sure, opening {target}")
            pyautogui.press('win')
            time.sleep(0.5)
            pyautogui.write(target)
            time.sleep(0.5)
            pyautogui.press('enter')

        else:
            print("Thinking (Gemini)...")
            ai_reply = get_ai_response(user_input)
            
            if "[OPEN:" in ai_reply:
                app_name = ai_reply.split("[OPEN:")[1].split("]")[0].strip()
                pyautogui.press('win')
                pyautogui.write(app_name)
                pyautogui.press('enter')

            clean_reply = ai_reply.split("[")[0].strip()
            speak(clean_reply)

if __name__ == "__main__":
    main()