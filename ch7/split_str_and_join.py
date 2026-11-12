"""String splitting examples"""

line = "Python is a programming language that lets you work quickly and integrate systems more effectively."
words = line.split()  # returns a list of words

parts = ["Python", "is", "a", "programming", "language", "that", "lets", "you", "work", "quickly", "and", "integrate", "systems", "more", "effectively."]

str_line = "Python,Java,C++,C#,JavaScript"
langs = str_line.split(",")  # returns a list of languages


# joining a list of strings into a single string
sentence = "-".join(parts)  # joins the list of words into a single string with spaces
print(sentence)  # Output: Python-is-a-programming-language-that-lets-you-work-quickly-and-integrate-systems-more-effectively.
