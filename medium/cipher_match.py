# Determine if two strings are a cipher match.  Two strings are a cipher match
# if they have the same ordering of characters, even if the characters themselves
# are not the same.  For example, “aabb” and “ccdd” are a cipher match, as are
# “abccd” and “efggh”

def cipher_match(str1, str2):
  return string_to_cipher(str1) == string_to_cipher(str2)

def string_to_cipher(string):
  used_chars = {}
  cipher = []
  character_count = 0
  for c in string:
    dict_entry = used_chars.get(c)
    if dict_entry:
      cipher.append(dict_entry)
    else:
      used_chars[c] = character_count
      character_count += 1
  return cipher

str1 = "aabb" 
str2 = "ccdd"
cipher_match(str1, str2)
