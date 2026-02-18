# JF String Notes

name = input("What be thy title?: ").strip().title()
print(f"Hello, {name}!")

sentence = "the quick brown fox jumps over the lazy dog."
print(f"{name}, did you know that {sentence}?")

word = input("Pick a word in the above sentence to change: ").strip().lower()
new = input("Pick the word to replace it with: ").strip().lower()
sentence = sentence.replace(word, new)

print(f"{name}, did you know that {sentence}?")