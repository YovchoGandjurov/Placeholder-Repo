ban_word = input().split()
text = input()

for word in ban_word:
    text = text.replace(word, "*" * len(word))

print(text)
