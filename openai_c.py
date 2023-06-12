import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="hello",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)