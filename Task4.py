my_string = "hello world"
my_char = 'l'

char_count = 0

for char in my_string:
    if char == my_char:
        char_count = char_count + 1

print(f"The character '{my_char}' appears {char_count} times.")
