from google import genai
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

API_KEY = "AIzaSyC2MFPhlcqeaG-pRKSiuwX2PHUanJybYpU"

client = genai.Client(api_key=API_KEY)

def get_ai_response(user_input):
    try:
        system_instruction = """
        You are CHITHRA, a helpful AI assistant. 
        If the user asks to open an application like Notepad, include a special tag in your response like [OPEN: app_name].
        For example: "Sure Sir, opening Notepad now. [OPEN: notepad]"
        Keep other responses plain text and conversational.
        """
        
        prompt = f"{system_instruction}\n\nUser: {user_input}"
        
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Brain Error: {e}")
        return "I'm having trouble thinking, Sir."