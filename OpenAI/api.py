# # 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

# from openai import OpenAI

# client = OpenAI(
#   api_key="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"
# )

# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   store=True,
#   messages=[
#     {"role": "user", "content": "write a sort description about ai"}
#   ]
# )

# print(completion.choices[0].message);


from openai import OpenAI
# client = OpenAI()


client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
