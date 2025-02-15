def main() -> None:
  path_to_file = "books/frankenstein.txt"
  with open(path_to_file) as f:
    f_contents = f.read()
    word_count = count_words(f_contents)
    letter_count = count_letters(f_contents)

  report_header = f"--- Begin report of {path_to_file} ---"
  report_footer = "--- End report ---"
  print(report_header)
  print(f"{word_count} words found in the document\n")
  for l in letter_count:
      if l.isalpha():
        print(f"The '{l}' character was found {letter_count[l]} times")
  print(report_footer)

def count_words(corpus):
  words = corpus.split()
  return len(words)

def count_letters(corpus):
  letters = dict()
  for l in corpus.lower():
    if l in letters:
      letters[l] += 1
    else:
      letters[l] = 1

  return letters

main()
