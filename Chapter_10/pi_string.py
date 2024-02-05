from pathlib import Path

path = Path('Chapter_10/text_files/pi_digits.txt') # Relative file path
contents = path.read_text()

lines = contents.splitlines()
print(lines)

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))