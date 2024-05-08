def main():
  path = "books/frankenstein.txt"
  text = get_contents(path)

  print(f"--- Begin report of {path} ---")
  print(f"{count_words(text)} words found in the document")
  print("")
  print_char(text)
  print(f"--- End report ---")

def get_contents(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  words = text.split()
  return len(words)

def print_char(text):
  chars = {}
  for letter in text:
    lowered = letter.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1

  d = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
  
  for char in d:
    if char.isalpha():
      print(f"The {char} character was found {d[char]} times")

main()