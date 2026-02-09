# OpenAI Client
import openai

def get_decision(prompt):
    # Configure OpenAI API key
    openai.api_key = 'your-api-key'
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=100
    )
    return response.choices[0].text.strip()