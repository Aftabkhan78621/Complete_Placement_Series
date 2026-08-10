#  check angram 
# listen == silent

s1 = input("Enter a sentence :")
s2 = input("Enter a sentence :")

if len(s1) != len(s2):
    print('Not Angram')
else:
    freq={}
    for ch in s1:
        freq[ch] = freq.get(ch,0) + 1
    for ch in s2:
        if ch not in freq:
            print("Not Angram")
            break
        freq[ch] -= 1

        if freq[ch] < 0:
            print("Not Angram")
            break
    else:
        print('Angram')