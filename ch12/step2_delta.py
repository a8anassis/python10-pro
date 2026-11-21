"""Βήμα 2: streaming απάντηση — το κείμενο έρχεται σταδιακά."""

import os
from dotenv import load_dotenv
load_dotenv()
import litellm

MODEL = os.getenv("MODEL")                 # anthropic/claude-haiku-5-5
# MODEL = os.getenv("MODEL_LOCAL")         # ollama_chat/gemma3:4b — χωρίς API key, τοπικά

message = {"role": "user", "content": "Πες μου για την ιστορία του Ηρακλείου Κρήτης σε 3 παραγράφους."}

response = litellm.completion(
    model=MODEL,
    messages=[message],
    stream=True
)
# Τα ίδια τα chunks είναι τα events (ή τα πακέτα δεδομένων των events) που φτάνουν από τον διακομιστή.
#
# Για να το καταλάβεις καλύτερα, πίσω από το streaming βρίσκεται μια τεχνολογία που λέγεται SSE (Server-Sent Events).
# Στο πρωτόκολλο που χρησιμοποιείται για το streaming (το SSE - Server-Sent Events),
# τα events χωρίζονται και τελειώνουν πάντοτε με διπλή αλλαγή γραμμής (\n\n).
# Τα «ωμά» (raw) δεδομένα που έρχονται από το δίκτυο πριν τα επεξεργαστεί η βιβλιοθήκη (litellm ή openai),
# η μορφή είναι κάπως έτσι:

# data: {"id":"chatcmpl-1","choices":[{"delta":{"content":"Γεια"}}]}
#
# data: {"id":"chatcmpl-1","choices":[{"delta":{"content":" σου"}}]}
#
# data: {"id":"chatcmpl-1","choices":[{"delta":{"content":"!"}}]}
#
# data: [DONE]

for chunk in response:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()