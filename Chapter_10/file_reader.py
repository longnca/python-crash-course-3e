from pathlib import Path

path = Path('Chapter_10/text_files/pi_digits.txt') # Relative file path
contents = path.read_text()
print(contents)
