from pathlib import Path

path = Path('Chapter_10/text_files/pi_million_digits.txt') # Relative file path
contents = path.read_text()

lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))