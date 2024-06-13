import os
import google.generativeai as genai

os.environ["GEMINI_API_KEY"] = "AIzaSyDWsOco8PP9XweKGtL1h4Hkkyc36Y99Tgg"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)
texto = "ovo,tapioca,tomate,frango"
response = chat_session.send_message("Me de uma  receita que so tenha os seguintes ingredientes"+(str(texto)))

print(response.text)