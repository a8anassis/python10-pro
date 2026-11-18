"""Βήμα 1: η ελάχιστη κλήση σε LLM."""
import os

from dotenv import load_dotenv
load_dotenv()
import litellm

MODEL = os.getenv("MODEL_OPENROUTER_FREE")

# Completion σημαίνει συμπλήρωση, και το όνομα περιγράφει κυριολεκτικά τι κάνει ένα LLM.
# Του δίνεις ένα κείμενο και αυτό το συνεχίζει, προβλέποντας το επόμενο token ξανά και ξανά.
# Είναι το ίδιο με το autocomplete του IDE, αλλά για ολόκληρες παραγράφους.

# Η ιστορία του ονόματος:
#
# Text completion (GPT-3, 2020). Το API δεχόταν σκέτο κείμενο και το συνέχιζε:
# prompt:  "Η πρωτεύουσα της Κρήτης είναι"
# output:  " το Ηράκλειο."
#
# Endpoint: /v1/completions

# Chat completion (ChatGPT, 2023). Αντί για σκέτο κείμενο στέλνεις λίστα μηνυμάτων με ρόλους (system, user, assistant).
# Εσωτερικά η λίστα γίνεται ένα κείμενο με ειδικά tokens που σημειώνουν τους ρόλους.
# Η λίστα που περνάς στην παράμετρο messages. Στον κώδικά σου είναι η [message]:
#
# python
# message = {"role": "user", "content": "Ποια είναι η πρωτεύουσα της Κρήτης;"}
# response = litellm.completion(model=MODEL, messages=[message])
# #                                                  ^^^^^^^^^ αυτή η λίστα
#
# Εδώ έχει ένα μόνο στοιχείο. Σε πραγματική συνομιλία περιέχει όλο το ιστορικό, γιατί το μοντέλο δεν θυμάται τίποτα από κλήση σε κλήση. Κάθε φορά του ξαναστέλνεις ολόκληρη τη συζήτηση:
#
# python
# messages = [
#     {"role": "system",    "content": "Είσαι ξεναγός στην Κρήτη. Απαντάς σύντομα."},
#     {"role": "user",      "content": "Ποια είναι η πρωτεύουσα της Κρήτης;"},
#     {"role": "assistant", "content": "Το Ηράκλειο."},
#     {"role": "user",      "content": "Και πόσους κατοίκους έχει;"},
# ]
# response = litellm.completion(model=MODEL, messages=messages)
#
# Πριν φτάσει στο μοντέλο, η λίστα μετατρέπεται σε ένα ενιαίο κείμενο μέσω του chat template του μοντέλου.

message = {"role": "user", "content": "Ποια είναι η πρωτεύουσα της Κρήτης;"}
response = litellm.completion(
    model=MODEL,
    messages=[message]
)
print(response.choices[0].message.content)




