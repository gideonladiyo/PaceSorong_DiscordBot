import google.generativeai as genai

genai.configure(
    api_key="AIzaSyCf3vJwDi2n7cDlLJs7tNxl4cemUqKUSFY"
)

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Apa kabar dari Papua?")
print(response.text)

# models = genai.list_models()
# for m in models:
#     print(m.name, m.supported_generation_methods)
