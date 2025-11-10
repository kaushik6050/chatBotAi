from openai import OpenAI


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

print("🤖 AI Bot Ready! Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! 👋")
        break

    # Send prompt to GPT model
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1-distill-llama-70b:free",
        messages=[
            {"role": "system", "content": "You are a friendly AI chatbot."},
            {"role": "user", "content": user_input}
        ]
    )

    # Print response
    print("Bot:", response.choices[0].message.content.strip())
