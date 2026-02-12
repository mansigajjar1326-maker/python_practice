# String Operations – Concept Clear Practice

# 1️⃣ Take input from user
text = input("Enter any sentence: ")

print("\n--- Basic Information ---")
print("Original text:", text)

# 2️⃣ Length of string
print("Length of text:", len(text))

# 3️⃣ Case conversion
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

# 4️⃣ Access characters
print("\n--- Character Access ---")
print("First character:", text[0])
print("Last character:", text[-1])

# 5️⃣ Check substring presence
word = input("\nEnter a word to search in the sentence: ")

if word.lower() in text.lower():
    print("Result: Word FOUND in the sentence")
else:
    print("Result: Word NOT found")

# 6️⃣ Count occurrences
print("Word appears", text.lower().count(word.lower()), "time(s)")

# 7️⃣ Replace word
new_word = input("Enter a word to replace it with: ")
updated_text = text.replace(word, new_word)

print("\n--- Updated Sentence ---")
print(updated_text)

# 8️⃣ Remove extra spaces
clean_text = text.strip()
print("\nText after removing extra spaces:", clean_text)

# 9️⃣ Split sentence into words
words_list = text.split()
print("Words in sentence:", words_list)
print("Total words:", len(words_list))
