"""Βήμα 1δ: chat με ιστορικό + streaming + error handling."""

import os
import litellm
from dotenv import load_dotenv
load_dotenv()

MODEL = os.getenv("MODEL")

messages = []   # το ιστορικό της συνομιλίας

while True:
    try:
        user_input = input("Ask ai4dev: ").strip()
        if user_input == "exit":
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        response = litellm.completion(
            model="anthropic/claude-haiku-5-5",
            messages=messages,
            stream=True,
        )

        print("Model: ", end="")
        parts = []
        for chunk in response:              # σφάλμα μπορεί να έρθει και ΕΔΩ (μέσα στο stream)
            delta = chunk.choices[0].delta.content
            if delta:
                print(delta, end="", flush=True)
                parts.append(delta)
        print()

        reply = "".join(parts)
        messages.append({"role": "assistant", "content": reply})

    except litellm.AuthenticationError:
        print("\nΛάθος ή κενό API key (έλεγξε το .env)")
        messages.pop()                      # αφαιρούμε την αναπάντητη ερώτηση
    except litellm.RateLimitError:
        print("\nΠολλά αιτήματα — δοκίμασε σε λίγο")
        messages.pop()
    except litellm.APIConnectionError as e:
        print(f"\nΠρόβλημα σύνδεσης: {e}")
        messages.pop()
    except litellm.APIError as e:
        print(f"\nΣφάλμα API: {e}")
        messages.pop()