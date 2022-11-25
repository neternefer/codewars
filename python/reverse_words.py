def reverse_words(text):
  """Complete the function that accepts a string parameter,
  and reverses each word in the string.
  All spaces in the string should be retained."""
  return (' ').join(([word[::-1] for word in text.split(' ')]))
