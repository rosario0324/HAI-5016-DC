from dotenv import load_dotenv
import os
from google import genai

# 환경변수에서 API 키 읽기
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("환경변수 GEMINI_API_KEY가 설정되어 있지 않습니다. 쉘에서 export로 설정하세요.")

# API 키를 명시적으로 전달
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)

# Make a loop that asks for the user's input and sends it to the model until the user types 'exit'
while True:
    user_input = input("Enter your question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )
    print("Response:", response.text)