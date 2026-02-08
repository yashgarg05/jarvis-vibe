import ollama

SYSTEM_PROMPT = """
You are Jarvis, a calm, intelligent AI assistant.
Respond clearly, concisely, and professionally.
"""

conversation = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def think(user_input: str) -> str:
    conversation.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="llama3.1",
        messages=conversation
    )

    reply = response["message"]["content"]
    conversation.append({"role": "assistant", "content": reply})

    # Optional: prevent memory explosion
    if len(conversation) > 12:
        conversation[:] = [conversation[0]] + conversation[-10:]

    return reply
