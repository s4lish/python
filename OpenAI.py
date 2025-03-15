from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
