import google.generativeai as genai

genai.configure(api_key="Type_API_key_here")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Who is Elon Musk?")
print(response.text)
