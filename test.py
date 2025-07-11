import google.generativeai as genai

genai.configure(api_key="AIzaSyDXij67zQf3y7nZfqz4JZLQIvkDFxznYwo")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Who is Elon Musk?")
print(response.text)
