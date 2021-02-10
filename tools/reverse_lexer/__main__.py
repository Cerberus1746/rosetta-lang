import string
from pathlib import Path


space_count = 0
curr_sentence = ""

exception_set = set()
keywords = set()

base_file = Path(__file__).parent / ".." / ".." / "schemas"/ "base_language.roset"

with base_file.open() as curr_file:
    while curr_char := curr_file.read(1):
        if curr_char in string.digits + string.ascii_letters + "_":
            curr_sentence += curr_char
        else:
            if curr_sentence:
                keywords.add(curr_sentence)
                curr_sentence = ""

            exception_set.add(curr_char)

print(keywords)
print(exception_set)
