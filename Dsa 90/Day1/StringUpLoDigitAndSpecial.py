a = 'Abc@1238#'
alphabets = ''
digit = ''
special = ''

for ch in a:
    if ch.isalpha():
        alphabets += ch
    elif ch.isdigit():
        digit += ch
    else:
        special += ch
lengthUp = len(alphabets.upper())
lengthLo = len(alphabets.lower())

print('Alphabests: ',lengthUp)
print('Alphabests: ',lengthLo)
print('Alphabests: ',alphabets)
print('digits: ',digit)
print('special: ',special)