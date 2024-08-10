from openai import OpenAI
client = OpenAI(api_key='YOUR_API_KEY')

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="jfdsjfdsl",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)