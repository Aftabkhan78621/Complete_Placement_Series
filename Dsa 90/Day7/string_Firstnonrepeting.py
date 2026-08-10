text = 'hello world '
freq={}
resultFirstNonRepeating = []

for ch in text:
    freq[ch] = freq.get(ch,0) + 1
# print(freq)
for ch in text:
    if freq[ch] == 1:
        print(ch)
        break
    else:
        print(-1)