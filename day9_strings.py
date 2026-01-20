# Day 9: Strings and String Methods

text = "Artificial Intelligence"

print("Original text:", text)

# Length of string
print("Length:", len(text))

# Indexing
print("First character:", text[0])
print("Last character:", text[-1])

# Slicing
print("First 10 characters:", text[:10])
print("Last 10 characters:", text[-10:])

print("--------------------")

# String methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace AI with ML:", text.replace("Intelligence", "Learning"))
print("Split text:", text.split())

print("--------------------")

# Check substring
if "AI" in text:
    print("AI is present in the text")
else:
    print("AI is not present in the text")
