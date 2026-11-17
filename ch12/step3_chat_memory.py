"""Βήμα 1γ: chat με ιστορικό + streaming."""

import os
import litellm
from dotenv import load_dotenv
load_dotenv()


MODEL = os.getenv("MODEL")

messages = []   # το ιστορικό της συνομιλίας

while True:
    user_input = input("Ask ai4dev: ")
    if user_input == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = litellm.completion(
        model="anthropic/claude-haiku-5-5",
        messages=messages,                  # ΟΛΟ το ιστορικό, όχι μόνο την ερώτηση
        stream=True,                        # η απάντηση έρχεται σταδιακά
    )

    print("Model: ", end="")
    parts = []
    for chunk in response:
        delta = chunk.choices[0].delta.content   # μόνο το νέο κομμάτι
        if delta:
            print(delta, end="", flush=True)
            parts.append(delta)
    print()

    reply = "".join(parts)                  # η πλήρης απάντηση
    messages.append({"role": "assistant", "content": reply})   # κρατάμε και την απάντηση