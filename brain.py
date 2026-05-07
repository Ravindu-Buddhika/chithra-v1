from google import genai
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

API_KEY = ""

client = genai.Client(api_key=API_KEY)

def get_ai_response(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=user_input
        )
        return response.text
    except Exception as e:
        print(f"Brain Error: {e}")
        return "I'm having trouble thinking, Sir. Please check my connection."