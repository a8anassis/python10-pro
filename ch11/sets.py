empty_set = set()
numbers = { 1, 2, 3, 4, 5 }
numbers2 = { 4, 5, 6, 7, 8 }

numbers.add(6)
numbers.remove(3)

union = numbers | numbers2                      # ένωση
intersection = numbers & numbers2               # τομή
difference = numbers - numbers2                 # διαφορά
symmetric_difference = numbers ^ numbers2       # συμμετρική διαφορά: Σε ένα από τα δύο sets αλλά όχι και στα δύο
