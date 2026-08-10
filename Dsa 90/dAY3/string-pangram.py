# # pangram => a pangram is a sentence that contains all 26 englih alphabets (a-z) at leaast once
# a = 'gjggggkekkeeeee'
# print(set(a))

sentence = input("Enter a sentence: ")
letter = set()

for ch in sentence.lower():
    if (('a' <=  ch <='z') | ('A' <=  ch <='Z')):
        letter.add(ch)
if len(letter) == 26:
    print('Pangram')
else:
    print("Not pangram",letter)


# tc : o(n)
#  sc : o(26)
