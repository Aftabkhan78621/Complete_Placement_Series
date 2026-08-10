# ============================================================
# STRINGS PATTERN - Batch 1 (Traversal)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. COUNT CHARACTERS
# ============================================================

"""
THEORY (Interview Explanation)

Character Traversal string ka sabse basic concept hai. Isme string ke
har character ko ek-ek karke visit kiya jata hai. Isi traversal se
Count Vowels, Count Digits, Count Alphabets aur Frequency jaise
questions bante hain. Python me len() se answer mil sakta hai, lekin
interview me traversal logic dikhana zyada important hota hai. Ye
String Pattern ki foundation hai aur TCS Prime me frequently pucha
jata hai.
"""

def count_characters(s):

    count = 0

    for ch in s:

        count += 1

    return count


print("Count Characters :")
print(count_characters("Hello123"))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 2. COUNT WORDS
# ============================================================

"""
THEORY (Interview Explanation)

Words count karne ke liye normally spaces count ki jati hain. Agar
string empty nahi hai to words = spaces + 1 hote hain. Interview me
multiple spaces bhi de sakte hain, isliye split() ki jagah traversal
approach samajhna zaruri hai. Neeche wala solution consecutive spaces
ko bhi handle karta hai.
"""

def count_words(s):

    count = 0

    inside_word = False

    for ch in s:

        if ch != " " and not inside_word:

            count += 1
            inside_word = True

        elif ch == " ":

            inside_word = False

    return count


print()

print("Count Words :")
print(count_words("Hello World Python"))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 3. COUNT VOWELS
# ============================================================

"""
THEORY (Interview Explanation)

Vowels English alphabet me a, e, i, o, u hote hain. Traversal ke dauran
har character ko lowercase me convert karke vowel set se compare kiya
jata hai. Ye question string traversal aur membership checking ko test
karta hai. Service-based interviews me ye bahut common basic question
hai.
"""

def count_vowels(s):

    count = 0

    vowels = "aeiou"

    for ch in s.lower():

        if ch in vowels:

            count += 1

    return count


print()

print("Count Vowels :")
print(count_vowels("Programming"))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 4. COUNT CONSONANTS
# ============================================================

"""
THEORY (Interview Explanation)

Consonants wo alphabet hote hain jo vowels nahi hote. Har character ko
check karte hain ki wo alphabet hai ya nahi. Agar alphabet hai aur vowel
nahi hai to consonant count badha dete hain. Is problem me alphabets aur
vowels dono concepts ek saath use hote hain.
"""

def count_consonants(s):

    count = 0

    vowels = "aeiou"

    for ch in s.lower():

        if ch.isalpha() and ch not in vowels:

            count += 1

    return count


print()

print("Count Consonants :")
print(count_consonants("Programming"))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 5. COUNT DIGITS
# ============================================================

"""
THEORY (Interview Explanation)

Digits count karne ke liye har character ko check kiya jata hai ki wo
0–9 ke beech hai ya nahi. Python me isdigit() method easiest approach
hai. Ye question string traversal aur character classification ko test
karta hai. TCS Prime ke basic coding questions me frequently dekha jata
hai.
"""

def count_digits(s):

    count = 0

    for ch in s:

        if ch.isdigit():

            count += 1

    return count


print()

print("Count Digits :")
print(count_digits("Python1234"))


# ============================================================
# 6. COUNT ALPHABETS
# ============================================================

"""
THEORY (Interview Explanation)

Alphabet count karne ke liye har character par isalpha() method use ki
jati hai. Digits aur special characters ignore ho jate hain. Ye basic
string validation aur parsing problems ki foundation hai.
"""

def count_alphabets(s):

    count = 0

    for ch in s:

        if ch.isalpha():

            count += 1

    return count


print()

print("Count Alphabets :")
print(count_alphabets("Python123@"))


# ============================================================
# 7. COUNT SPECIAL CHARACTERS
# ============================================================

"""
THEORY (Interview Explanation)

Special characters wo hote hain jo na alphabet hote hain aur na digit,
aur space bhi nahi hote. Har character ko check karke unwanted symbols
count kiye jate hain. Ye input validation aur data cleaning me kaam
aata hai.
"""

def count_special(s):

    count = 0

    for ch in s:

        if not ch.isalnum() and ch != " ":

            count += 1

    return count


print()

print("Count Special Characters :")
print(count_special("Python@123#AI!"))


# ============================================================
# Expected Output
# ============================================================

# Count Characters :
# 8

# Count Words :
# 3

# Count Vowels :
# 3

# Count Consonants :
# 8

# Count Digits :
# 4

# Count Alphabets :
# 6

# Count Special Characters :
# 3


# ============================================================
# Complexity
# ============================================================

# All Problems
# Time  : O(n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Traverse character by character.
# ✔ isalpha() -> Alphabet
# ✔ isdigit() -> Digit
# ✔ isalnum() -> Alphabet or Digit
# ✔ lower() avoids separate upper/lower checks.
# ✔ Foundation for almost every String problem.

# ============================================================
# STRINGS - Batch 1 COMPLETE ✅
# ============================================================

# ============================================================
# STRINGS PATTERN - Batch 2 (Reverse Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. REVERSE STRING
# ============================================================

"""
THEORY (Interview Explanation)

Reverse String String Pattern ka sabse basic interview question hai.
Isme string ke characters ko reverse order me arrange karna hota hai.
Interview me slicing (s[::-1]) ki jagah traversal ya two-pointer
approach prefer ki jati hai kyunki usse logic clear hota hai. Reverse
ka concept Palindrome, Rotation aur Two Pointer questions ki foundation
hai. TCS Prime aur service-based companies me ye frequently pucha jata
hai.
"""

def reverse_string(s):

    result = ""

    for i in range(len(s)-1, -1, -1):

        result += s[i]

    return result


print("Reverse String :")
print(reverse_string("Python"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. REVERSE WORDS
# ============================================================

"""
THEORY (Interview Explanation)

Reverse Words me poore sentence ke words ka order reverse karna hota
hai, lekin har word ke characters same rehte hain. Ye string parsing
aur splitting ka common interview question hai. Service-based companies
me ye basic string manipulation ke liye kaafi pucha jata hai.
"""

def reverse_words(sentence):

    words = sentence.split()

    words.reverse()

    return " ".join(words)


print()

print("Reverse Words :")
print(reverse_words("I Love Python"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. REVERSE EACH WORD
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me sentence ka order same rehta hai, lekin har individual
word reverse ho jata hai. Pehle sentence ko words me split karte hain,
fir har word ko reverse karke dobara join kar dete hain. Ye interview
me String Manipulation aur Traversal dono ko test karta hai.
"""

def reverse_each_word(sentence):

    words = sentence.split()

    result = []

    for word in words:

        reverse = ""

        for i in range(len(word)-1, -1, -1):

            reverse += word[i]

        result.append(reverse)

    return " ".join(result)


print()

print("Reverse Each Word :")
print(reverse_each_word("I Love Python"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 4. REVERSE STRING (Without Slicing)
# ============================================================

"""
THEORY (Interview Explanation)

Interview me kai baar specifically bola jata hai ki slicing use nahi
karni. Is case me Two Pointer approach sabse best hoti hai. Ek pointer
start par aur dusra end par hota hai. Dono characters ko swap karte hue
andar ki taraf badhte hain. Ye in-place approach hai aur Two Pointer
Pattern ka classic example mana jata hai.
"""

def reverse_without_slicing(s):

    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:

        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return "".join(chars)


print()

print("Reverse Without Slicing :")
print(reverse_without_slicing("Python"))


# ============================================================
# Expected Output
# ============================================================

# Reverse String :
# nohtyP

# Reverse Words :
# Python Love I

# Reverse Each Word :
# I evoL nohtyP

# Reverse Without Slicing :
# nohtyP


# ============================================================
# Complexity
# ============================================================

# Reverse String
# Time  : O(n)
# Space : O(n)

# Reverse Words
# Time  : O(n)
# Space : O(n)

# Reverse Each Word
# Time  : O(n)
# Space : O(n)

# Reverse Without Slicing
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Reverse String → Basic Traversal
# ✔ Reverse Words → Reverse word order only
# ✔ Reverse Each Word → Reverse individual words
# ✔ Two Pointer is preferred when slicing is not allowed
# ✔ Very Frequently Asked in TCS Prime & Service-Based Companies

# ============================================================
# STRINGS - Batch 2 COMPLETE ✅
# ============================================================


# ============================================================
# STRINGS PATTERN - Batch 3 (Palindrome Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. PALINDROME STRING
# ============================================================

"""
THEORY (Interview Explanation)

Palindrome wo string hoti hai jo left se aur right se same read hoti
hai. Is problem ko solve karne ka best approach Two Pointer hai. Ek
pointer string ke start par aur doosra end par rakha jata hai. Dono
characters compare kiye jate hain. Agar kabhi mismatch mil jaye to
string palindrome nahi hai. Agar pointers cross ho jaye bina mismatch
ke to string palindrome hai. Ye TCS Prime ka bahut common question hai.
"""

def palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        if s[left] != s[right]:

            return False

        left += 1
        right -= 1

    return True


print("Palindrome :")
print(palindrome("madam"))
print(palindrome("python"))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 2. VALID PALINDROME
# ============================================================

"""
THEORY (Interview Explanation)

Valid Palindrome me spaces, commas aur special characters ignore kiye
jate hain. Sirf alphabets aur digits compare hote hain aur comparison
case-insensitive hota hai. Two Pointer approach use karke invalid
characters skip karte hain. Ye service-based interviews me frequently
pucha jane wala medium-level string question hai.
"""

def valid_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():

            left += 1

        while left < right and not s[right].isalnum():

            right -= 1

        if s[left].lower() != s[right].lower():

            return False

        left += 1
        right -= 1

    return True


print()

print("Valid Palindrome :")
print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("Hello"))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 3. LONGEST PALINDROMIC PREFIX
# ============================================================

"""
THEORY (Interview Explanation)

Longest Palindromic Prefix me string ke starting se sabse lamba
palindrome find karna hota hai. Basic approach me hum longest prefix se
start karte hain aur check karte hain ki wo palindrome hai ya nahi.
Jab pehla palindrome prefix mil jata hai wahi answer hota hai. TCS Prime
me iska basic version hi pucha jata hai.
"""

def longest_palindromic_prefix(s):

    def is_palindrome(text):

        left = 0
        right = len(text) - 1

        while left < right:

            if text[left] != text[right]:
                return False

            left += 1
            right -= 1

        return True

    for i in range(len(s), 0, -1):

        if is_palindrome(s[:i]):

            return s[:i]

    return ""


print()

print("Longest Palindromic Prefix :")
print(longest_palindromic_prefix("levelup"))
print(longest_palindromic_prefix("abacxyz"))


# ============================================================
# Expected Output
# ============================================================

# Palindrome :
# True
# False

# Valid Palindrome :
# True
# False

# Longest Palindromic Prefix :
# level
# aba


# ============================================================
# Complexity
# ============================================================

# Palindrome
# Time  : O(n)
# Space : O(1)

# Valid Palindrome
# Time  : O(n)
# Space : O(1)

# Longest Palindromic Prefix (Basic)
# Time  : O(n²)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Two Pointer is the preferred approach.
# ✔ Ignore case using lower().
# ✔ Ignore special characters using isalnum().
# ✔ Basic palindrome is one of the most asked TCS Prime questions.
# ✔ Valid Palindrome is a direct extension of the basic problem.

# ============================================================
# STRINGS - Batch 3 COMPLETE ✅
# ============================================================

# ============================================================
# STRINGS PATTERN - Batch 4 (HashMap / Frequency Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. CHARACTER FREQUENCY
# ============================================================

"""
THEORY (Interview Explanation)

Character Frequency String + HashMap Pattern ka foundation hai.
Isme har character kitni baar aaya hai ye count kiya jata hai.
HashMap (Dictionary) use karne se har character ka count O(1)
average time me update ho jata hai. Isi concept se Maximum Frequency,
Duplicate Characters aur First Non-Repeating jaise questions bante hain.
Ye TCS Prime ka bahut important pattern hai.
"""

def character_frequency(s):

    frequency = {}

    for ch in s:

        frequency[ch] = frequency.get(ch, 0) + 1

    return frequency


print("Character Frequency :")
print(character_frequency("programming"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. MAXIMUM FREQUENCY CHARACTER
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me sabse jyada baar aane wale character ko find karna hota
hai. Pehle HashMap se frequency count karte hain, fir us dictionary ko
traverse karke maximum frequency wala character return karte hain.
Interview me frequency counting ka ye sabse common application hai.
"""

def maximum_frequency_character(s):

    frequency = {}

    for ch in s:

        frequency[ch] = frequency.get(ch, 0) + 1

    maximum = ""

    count = 0

    for ch in frequency:

        if frequency[ch] > count:

            count = frequency[ch]

            maximum = ch

    return maximum


print()

print("Maximum Frequency Character :")
print(maximum_frequency_character("programming"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. FIRST NON-REPEATING CHARACTER
# ============================================================

"""
THEORY (Interview Explanation)

First Non-Repeating Character ka matlab pehla character jiska frequency
sirf 1 ho. Pehle frequency map banaya jata hai, fir original string ko
dobara traverse karke pehla frequency 1 wala character return kar diya
jata hai. Agar koi na mile to -1 return karte hain.
"""

def first_non_repeating(s):

    frequency = {}

    for ch in s:

        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in s:

        if frequency[ch] == 1:

            return ch

    return -1


print()

print("First Non-Repeating Character :")
print(first_non_repeating("aabbcde"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 4. FIRST REPEATING CHARACTER
# ============================================================

"""
THEORY (Interview Explanation)

First Repeating Character me pehla aisa character return karna hota hai
jo dubara milta hai. Iske liye HashSet ya HashMap use karte hain.
Traversal ke dauran agar character pehle se set me hai to wahi answer
hai, warna use set me add kar dete hain.
"""

def first_repeating(s):

    visited = set()

    for ch in s:

        if ch in visited:

            return ch

        visited.add(ch)

    return -1


print()

print("First Repeating Character :")
print(first_repeating("abcaef"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 5. DUPLICATE CHARACTERS
# ============================================================

"""
THEORY (Interview Explanation)

Duplicate Characters me un sabhi characters ko print karna hota hai
jo ek se jyada baar aaye hain. Frequency map banakar frequency > 1
wale characters collect kar lete hain. Ye data cleaning aur string
analysis me use hota hai.
"""

def duplicate_characters(s):

    frequency = {}

    result = []

    for ch in s:

        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in frequency:

        if frequency[ch] > 1:

            result.append(ch)

    return result


print()

print("Duplicate Characters :")
print(duplicate_characters("programming"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 6. UNIQUE CHARACTERS
# ============================================================

"""
THEORY (Interview Explanation)

Unique Characters me sirf wahi characters return karte hain jo
exactly ek baar aaye hain. Ye First Non-Repeating ka extension hai.
HashMap se frequency count karne ke baad frequency == 1 wale
characters answer me add kar diye jate hain.
"""

def unique_characters(s):

    frequency = {}

    result = []

    for ch in s:

        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in s:

        if frequency[ch] == 1:

            result.append(ch)

    return result


print()

print("Unique Characters :")
print(unique_characters("programming"))


# ============================================================
# Expected Output
# ============================================================

# Character Frequency :
# {'p':1,'r':2,'o':1,'g':2,'a':1,'m':2,'i':1,'n':1}

# Maximum Frequency Character :
# r

# First Non-Repeating Character :
# c

# First Repeating Character :
# a

# Duplicate Characters :
# ['r','g','m']

# Unique Characters :
# ['p','o','a','i','n']


# ============================================================
# Complexity
# ============================================================

# All Problems
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Dictionary = Frequency Count
# ✔ Set = Fast Duplicate Detection
# ✔ get(key,0) avoids KeyError
# ✔ Frequency Pattern is one of the highest-frequency
#   patterns in TCS Prime interviews.
# ✔ Foundation for Anagram and Sliding Window problems.

# ============================================================
# STRINGS - Batch 4 COMPLETE ✅
# ============================================================

# ============================================================
# STRINGS PATTERN - Batch 5 (Anagram Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. VALID ANAGRAM
# ============================================================

"""
THEORY (Interview Explanation)

Anagram ka matlab dono strings me same characters same frequency ke
saath hone chahiye, bas order different ho sakta hai. Sabse efficient
approach HashMap (Dictionary) se frequency compare karna hai. Agar dono
strings ki frequency same hai to strings anagram hain, warna nahi.
Ye TCS Prime aur service-based companies ka sabse common string
question hai.
"""

def valid_anagram(s1, s2):

    if len(s1) != len(s2):

        return False

    frequency = {}

    for ch in s1:

        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in s2:

        if ch not in frequency:

            return False

        frequency[ch] -= 1

        if frequency[ch] < 0:

            return False

    return True


print("Valid Anagram :")
print(valid_anagram("listen", "silent"))
print(valid_anagram("hello", "world"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. GROUP ANAGRAMS
# ============================================================

"""
THEORY (Interview Explanation)

Group Anagrams me same anagram wale words ko ek group me rakhna hota
hai. Har word ko sort karke uska sorted version key bana dete hain.
Jinke sorted keys same hote hain, wo ek hi group me chale jate hain.
Ye HashMap ka bahut important application hai aur Infosys, Cognizant,
Accenture aur TCS Prime me medium-level question ke roop me pucha
ja sakta hai.
"""

from collections import defaultdict

def group_anagrams(words):

    groups = defaultdict(list)

    for word in words:

        key = "".join(sorted(word))

        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print()

print("Group Anagrams :")
print(group_anagrams(words))


# ============================================================
# Expected Output
# ============================================================

# Valid Anagram :
# True
# False

# Group Anagrams :
# [['eat', 'tea', 'ate'],
#  ['tan', 'nat'],
#  ['bat']]


# ============================================================
# Complexity
# ============================================================

# Valid Anagram
# Time  : O(n)
# Space : O(n)

# Group Anagrams
# Time  : O(n × k log k)
# k = Average length of each word
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Same frequency = Anagram
# ✔ Length mismatch → Immediately False
# ✔ Sorted string is the best HashMap key
# ✔ Frequency Map and Sorting are the two standard approaches
# ✔ Very Frequently Asked in TCS Prime & Service-Based Companies

# ============================================================
# STRINGS - Batch 5 COMPLETE ✅
# ============================================================


# ============================================================
# STRINGS PATTERN - Batch 6 (Two Pointer Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. REVERSE STRING (Two Pointer)
# ============================================================

"""
THEORY (Interview Explanation)

Two Pointer Pattern me ek pointer string ke beginning par aur doosra
end par hota hai. Dono pointers ke characters ko swap karte hue beech
ki taraf move karte hain. Is approach me har character sirf ek baar
visit hota hai, isliye ye O(n) solution hai. Reverse String ka ye
standard interview solution hai aur TCS Prime me frequently pucha
jata hai.
"""

def reverse_string(s):

    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:

        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return "".join(chars)


print("Reverse String :")
print(reverse_string("Python"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. PALINDROME CHECK
# ============================================================

"""
THEORY (Interview Explanation)

Palindrome check ke liye Two Pointer sabse efficient approach hai.
Left aur right characters compare kiye jate hain. Agar kabhi mismatch
mil jaye to answer False hota hai. Agar pointers cross ho jaye bina
mismatch ke to string palindrome hoti hai. Is question se interviewer
Two Pointer logic test karta hai.
"""

def palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        if s[left] != s[right]:

            return False

        left += 1
        right -= 1

    return True


print()

print("Palindrome :")
print(palindrome("madam"))
print(palindrome("python"))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 3. REMOVE DUPLICATE CHARACTERS
# ============================================================

"""
THEORY (Interview Explanation)

Duplicate characters remove karne ke liye traversal ke saath HashSet
use karte hain. Har character ko ek hi baar result me add karte hain.
Agar character pehle se set me hai to skip kar dete hain. Ye string
cleaning aur preprocessing me kaafi use hota hai.
"""

def remove_duplicates(s):

    visited = set()

    result = ""

    for ch in s:

        if ch not in visited:

            result += ch

            visited.add(ch)

    return result


print()

print("Remove Duplicates :")
print(remove_duplicates("programming"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 4. REMOVE CHARACTER
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me ek specific character ko string se remove karna hota hai.
Traversal ke dauran agar current character target character nahi hai
to use result me add kar dete hain. Ye filtering aur data cleaning ka
basic question hai jo service-based interviews me pucha jata hai.
"""

def remove_character(s, target):

    result = ""

    for ch in s:

        if ch != target:

            result += ch

    return result


print()

print("Remove Character :")
print(remove_character("programming", "m"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 5. REMOVE SPACES
# ============================================================

"""
THEORY (Interview Explanation)

Remove Spaces problem me string ke saare blank spaces hata diye jate
hain. Har character traverse karke agar wo space nahi hai to result
me add kar dete hain. Ye input formatting aur preprocessing me bahut
common operation hai.
"""

def remove_spaces(s):

    result = ""

    for ch in s:

        if ch != " ":

            result += ch

    return result


print()

print("Remove Spaces :")
print(remove_spaces("I Love Python"))


# ============================================================
# Expected Output
# ============================================================

# Reverse String :
# nohtyP

# Palindrome :
# True
# False

# Remove Duplicates :
# progamin

# Remove Character :
# prograing

# Remove Spaces :
# ILovePython


# ============================================================
# Complexity
# ============================================================

# Reverse String
# Time  : O(n)
# Space : O(n)

# Palindrome
# Time  : O(n)
# Space : O(1)

# Remove Duplicates
# Time  : O(n)
# Space : O(n)

# Remove Character
# Time  : O(n)
# Space : O(n)

# Remove Spaces
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Two Pointer is mainly used for reverse and palindrome.
# ✔ HashSet removes duplicates efficiently.
# ✔ String traversal solves remove character and remove spaces.
# ✔ Time Complexity is O(n) for all problems.
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# STRINGS - Batch 6 COMPLETE ✅
# ============================================================


# ============================================================
# STRINGS PATTERN - Batch 7 (Sliding Window Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. LONGEST UNIQUE SUBSTRING
# ============================================================

"""
THEORY (Interview Explanation)

Sliding Window Pattern me do pointers (left aur right) use hote hain.
Window ko expand aur shrink karke answer nikala jata hai. Longest Unique
Substring me window ke andar koi duplicate character nahi hona chahiye.
Jaise hi duplicate mile, left pointer ko move karke duplicate remove
karte hain. Ye TCS Prime aur service-based companies ka sabse important
Sliding Window question hai.
"""

def longest_unique_substring(s):

    left = 0
    visited = {}
    answer = 0

    for right in range(len(s)):

        if s[right] in visited and visited[s[right]] >= left:

            left = visited[s[right]] + 1

        visited[s[right]] = right

        answer = max(answer, right - left + 1)

    return answer


print("Longest Unique Substring :")
print(longest_unique_substring("abcabcbb"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. MINIMUM WINDOW SUBSTRING
# ============================================================

"""
THEORY (Interview Explanation)

Minimum Window Substring me source string ka sabse chhota substring
find karna hota hai jo target string ke sabhi characters contain kare.
Window ko expand karke required characters collect karte hain aur
condition satisfy hote hi left se shrink karke minimum length update
karte hain. Ye Sliding Window ka advanced aur high-frequency question
hai.
"""

from collections import Counter

def minimum_window(s, t):

    need = Counter(t)

    missing = len(t)

    left = start = end = 0

    for right in range(len(s)):

        if need[s[right]] > 0:
            missing -= 1

        need[s[right]] -= 1

        while missing == 0:

            if end == 0 or right - left + 1 < end - start:

                start = left
                end = right + 1

            need[s[left]] += 1

            if need[s[left]] > 0:

                missing += 1

            left += 1

    return s[start:end]


print()

print("Minimum Window Substring :")
print(minimum_window("ADOBECODEBANC", "ABC"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. LONGEST SUBSTRING WITH K DISTINCT CHARACTERS
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me window ke andar maximum K distinct characters allowed
hote hain. Agar distinct characters K se zyada ho jaye to left pointer
move karke frequency reduce karte hain. Jab distinct count fir se K ya
usse kam ho jaye tab answer update karte hain. Ye HashMap + Sliding
Window ka classic interview question hai.
"""

def longest_k_distinct(s, k):

    left = 0
    frequency = {}

    answer = 0

    for right in range(len(s)):

        frequency[s[right]] = frequency.get(s[right], 0) + 1

        while len(frequency) > k:

            frequency[s[left]] -= 1

            if frequency[s[left]] == 0:

                del frequency[s[left]]

            left += 1

        answer = max(answer, right - left + 1)

    return answer


print()

print("Longest K Distinct :")
print(longest_k_distinct("eceba", 2))


# Time  : O(n)
# Space : O(k)



# ============================================================
# 4. MAXIMUM VOWELS IN WINDOW
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me fixed-size Sliding Window use hoti hai. Window ke andar
kitne vowels hain ye maintain karte hain. Window expand hone par naye
character ko add karte hain aur window size exceed hone par left
character remove kar dete hain. Har step par maximum vowel count update
karte hain.
"""

def maximum_vowels(s, k):

    vowels = "aeiou"

    current = 0
    answer = 0

    for i in range(len(s)):

        if s[i] in vowels:

            current += 1

        if i >= k:

            if s[i-k] in vowels:

                current -= 1

        answer = max(answer, current)

    return answer


print()

print("Maximum Vowels :")
print(maximum_vowels("abciiidef", 3))


# ============================================================
# Expected Output
# ============================================================

# Longest Unique Substring :
# 3

# Minimum Window Substring :
# BANC

# Longest K Distinct :
# 3

# Maximum Vowels :
# 3


# ============================================================
# Complexity
# ============================================================

# Longest Unique Substring
# Time  : O(n)
# Space : O(n)

# Minimum Window Substring
# Time  : O(n)
# Space : O(n)

# Longest K Distinct
# Time  : O(n)
# Space : O(k)

# Maximum Vowels
# Time  : O(n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Sliding Window = Left + Right Pointer
# ✔ Expand → Right++
# ✔ Shrink → Left++
# ✔ HashMap stores frequency.
# ✔ Fixed Window and Variable Window are the two main types.
# ✔ One of the highest-frequency patterns in TCS Prime.

# ============================================================
# STRINGS - Batch 7 COMPLETE ✅
# ============================================================



# ============================================================
# STRINGS PATTERN - Batch 8 (Substring Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. PRINT ALL SUBSTRINGS
# ============================================================

"""
THEORY (Interview Explanation)

Substring String Pattern ka sabse basic concept hai. Substring hamesha
continuous characters ka group hota hai. Har possible starting index se
har possible ending index tak substring generate ki ja sakti hai.
Nested loops ka use karke O(n²) substrings print ki jati hain. Ye
Longest Palindrome, Pattern Matching aur Dynamic Programming ki
foundation hai. TCS Prime me basic version frequently pucha jata hai.
"""

def print_all_substrings(s):

    result = []

    for i in range(len(s)):

        for j in range(i + 1, len(s) + 1):

            result.append(s[i:j])

    return result


print("All Substrings :")
print(print_all_substrings("abc"))


# Time  : O(n²)
# Space : O(n²)



# ============================================================
# 2. LONGEST WORD
# ============================================================

"""
THEORY (Interview Explanation)

Sentence me sabse bada word find karna ek common string manipulation
question hai. Sentence ko spaces ke basis par split karte hain aur
har word ki length compare karte hain. Jiski length maximum hoti hai,
wahi answer hota hai. Ye interview me string traversal aur parsing
ko test karta hai.
"""

def longest_word(sentence):

    words = sentence.split()

    answer = ""

    for word in words:

        if len(word) > len(answer):

            answer = word

    return answer


print()

print("Longest Word :")
print(longest_word("I love programming in Python"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. LONGEST COMMON PREFIX
# ============================================================

"""
THEORY (Interview Explanation)

Longest Common Prefix me string array ka common starting part find
karna hota hai. Pehli string ko reference maan kar har position par
baaki strings ke characters compare karte hain. Jaise hi mismatch mile,
current prefix return kar dete hain. Ye service-based companies ka
bahut common interview question hai.
"""

def longest_common_prefix(words):

    if not words:

        return ""

    prefix = words[0]

    for word in words[1:]:

        while not word.startswith(prefix):

            prefix = prefix[:-1]

            if not prefix:

                return ""

    return prefix


words = ["flower", "flow", "flight"]

print()

print("Longest Common Prefix :")
print(longest_common_prefix(words))


# Time  : O(n × m)
# n = Number of Strings
# m = Prefix Length



# ============================================================
# 4. STRING ROTATION
# ============================================================

"""
THEORY (Interview Explanation)

Do strings tab rotation hoti hain jab ek string ko circular shift
karke dusri string banayi ja sake. Efficient trick ye hai ki first
string ko khud se concatenate kar do. Agar second string usme substring
ke roop me mil jaye to dono rotation hain. Ye TCS Prime aur Infosys
me frequently pucha jane wala question hai.
"""

def string_rotation(s1, s2):

    if len(s1) != len(s2):

        return False

    return s2 in (s1 + s1)


print()

print("String Rotation :")
print(string_rotation("abcd", "cdab"))
print(string_rotation("abcd", "acbd"))


# ============================================================
# Expected Output
# ============================================================

# All Substrings :
# ['a', 'ab', 'abc', 'b', 'bc', 'c']

# Longest Word :
# programming

# Longest Common Prefix :
# fl

# String Rotation :
# True
# False


# ============================================================
# Complexity
# ============================================================

# Print All Substrings
# Time  : O(n²)
# Space : O(n²)

# Longest Word
# Time  : O(n)
# Space : O(n)

# Longest Common Prefix
# Time  : O(n × m)
# Space : O(1)

# String Rotation
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Substring = Continuous characters.
# ✔ Nested loops generate all substrings.
# ✔ Longest Common Prefix is a standard interview question.
# ✔ Rotation Trick → s2 in (s1 + s1)
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# STRINGS - Batch 8 COMPLETE ✅
# ============================================================

# ============================================================
# STRINGS PATTERN - Batch 9 (String Manipulation Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. REMOVE SPACES
# ============================================================

"""
THEORY (Interview Explanation)

Remove Spaces ek basic string manipulation problem hai. Isme string ke
saare blank spaces hata diye jate hain. Har character traverse kiya
jata hai aur agar wo space nahi hota to result string me add kar diya
jata hai. Ye data cleaning aur input preprocessing me bahut use hota
hai aur TCS Prime me frequently pucha jata hai.
"""

def remove_spaces(s):

    result = ""

    for ch in s:

        if ch != " ":

            result += ch

    return result


print("Remove Spaces :")
print(remove_spaces("I Love Python"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. REMOVE EXTRA SPACES
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me multiple consecutive spaces ko sirf ek space me convert
karna hota hai. Words ke beech ek hi space rehni chahiye aur starting/
ending spaces remove ho jani chahiye. Ye formatting aur text processing
ke liye common interview question hai.
"""

def remove_extra_spaces(s):

    return " ".join(s.split())


print()

print("Remove Extra Spaces :")
print(remove_extra_spaces("  I    Love    Python   "))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. REMOVE DUPLICATE CHARACTERS
# ============================================================

"""
THEORY (Interview Explanation)

Duplicate characters remove karne ke liye HashSet use karte hain.
Har character ko sirf pehli baar result me add kiya jata hai.
Agar character pehle se visited hai to use ignore kar dete hain.
Ye string preprocessing ka common task hai.
"""

def remove_duplicates(s):

    visited = set()

    result = ""

    for ch in s:

        if ch not in visited:

            visited.add(ch)

            result += ch

    return result


print()

print("Remove Duplicate Characters :")
print(remove_duplicates("programming"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 4. TOGGLE CASE
# ============================================================

"""
THEORY (Interview Explanation)

Toggle Case me uppercase letters lowercase ban jate hain aur lowercase
letters uppercase ban jate hain. Python me swapcase() built-in method
available hai, lekin interviewer traversal-based logic bhi puch sakta
hai. Ye basic string manipulation question hai.
"""

def toggle_case(s):

    result = ""

    for ch in s:

        if ch.islower():

            result += ch.upper()

        elif ch.isupper():

            result += ch.lower()

        else:

            result += ch

    return result


print()

print("Toggle Case :")
print(toggle_case("PyThOn123"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 5. UPPER ↔ LOWER
# ============================================================

"""
THEORY (Interview Explanation)

Uppercase aur Lowercase conversion string formatting ka basic concept
hai. Python me upper() aur lower() methods use hote hain. Interview me
kabhi manually ASCII values se conversion bhi puchi ja sakti hai, lekin
service-based companies me built-in methods generally acceptable hote
hain.
"""

def convert_case(s):

    return s.upper(), s.lower()


print()

print("Upper & Lower :")
print(convert_case("Python"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 6. REPLACE CHARACTER
# ============================================================

"""
THEORY (Interview Explanation)

Replace Character me string ke ek specific character ko doosre
character se replace karna hota hai. Traversal ke dauran matching
character milne par replacement add kar dete hain. Ye basic string
processing aur data cleaning me use hota hai.
"""

def replace_character(s, old, new):

    result = ""

    for ch in s:

        if ch == old:

            result += new

        else:

            result += ch

    return result


print()

print("Replace Character :")
print(replace_character("banana", "a", "o"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 7. REPLACE WORD
# ============================================================

"""
THEORY (Interview Explanation)

Replace Word me sentence ke ek word ko doosre word se replace karte
hain. Service-based interviews me built-in replace() method generally
acceptable hota hai. Ye text processing aur string formatting ka common
question hai.
"""

def replace_word(sentence, old, new):

    return sentence.replace(old, new)


print()

print("Replace Word :")
print(replace_word("I Love Python", "Python", "Java"))


# ============================================================
# Expected Output
# ============================================================

# Remove Spaces :
# ILovePython

# Remove Extra Spaces :
# I Love Python

# Remove Duplicate Characters :
# progamin

# Toggle Case :
# pYtHoN123

# Upper & Lower :
# ('PYTHON', 'python')

# Replace Character :
# bonono

# Replace Word :
# I Love Java


# ============================================================
# Complexity
# ============================================================

# Remove Spaces              O(n)
# Remove Extra Spaces        O(n)
# Remove Duplicates          O(n)
# Toggle Case               O(n)
# Upper ↔ Lower             O(n)
# Replace Character         O(n)
# Replace Word              O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ String Manipulation focuses on modifying strings.
# ✔ HashSet is useful for removing duplicates.
# ✔ upper(), lower() and replace() are standard methods.
# ✔ Traversal-based solutions are preferred in interviews.
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# STRINGS - Batch 9 COMPLETE ✅
# ============================================================

# ============================================================
# STRINGS PATTERN - Batch 10
# (Compression + Pattern Matching + Lexicographical)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. STRING COMPRESSION
# ============================================================

"""
THEORY (Interview Explanation)

String Compression me consecutive same characters ko character + count
format me convert kiya jata hai. Jaise "aaabbc" ko "a3b2c1" likhte hain.
Ye Two Pointer aur Traversal ka application hai. Interview me count
maintain karna aur last group ko handle karna important hota hai. TCS
Prime me iska basic version pucha ja sakta hai.
"""

def string_compression(s):

    if not s:
        return ""

    result = ""

    count = 1

    for i in range(1, len(s)):

        if s[i] == s[i-1]:

            count += 1

        else:

            result += s[i-1] + str(count)

            count = 1

    result += s[-1] + str(count)

    return result


print("String Compression :")
print(string_compression("aaabbcccc"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. RUN LENGTH ENCODING
# ============================================================

"""
THEORY (Interview Explanation)

Run Length Encoding (RLE) String Compression ka hi standard form hai.
Consecutive repeated characters ko character aur frequency ke pair me
store kiya jata hai. Image Compression aur Data Compression me bhi iska
basic concept use hota hai. Interview me logic String Compression jaisa
hi hota hai.
"""

def run_length_encoding(s):

    return string_compression(s)


print()

print("Run Length Encoding :")
print(run_length_encoding("wwwwaaadex"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. NAIVE PATTERN SEARCHING
# ============================================================

"""
THEORY (Interview Explanation)

Naive Pattern Matching me pattern ko text ke har possible position par
compare kiya jata hai. Agar saare characters match ho jaye to pattern
mil gaya. Ye Pattern Matching ka sabse basic algorithm hai aur TCS Prime
me isi level ka question expected hota hai.
"""

def naive_search(text, pattern):

    result = []

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        if text[i:i+m] == pattern:

            result.append(i)

    return result


print()

print("Naive Pattern Search :")
print(naive_search("AABAACAADAABAABA", "AABA"))


# Time  : O(n × m)
# Space : O(1)



# ============================================================
# 4. COUNT PATTERN OCCURRENCES
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me pattern kitni baar text me occur hua hai ye count karna
hota hai. Naive Pattern Matching ka hi extension hai. Har matching
position par counter increment kar dete hain.
"""

def count_pattern(text, pattern):

    count = 0

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        if text[i:i+m] == pattern:

            count += 1

    return count


print()

print("Count Pattern Occurrences :")
print(count_pattern("AABAACAADAABAABA", "AABA"))


# Time  : O(n × m)
# Space : O(1)



# ============================================================
# 5. FIRST & LAST OCCURRENCE
# ============================================================

"""
THEORY (Interview Explanation)

Pattern ka first aur last occurrence built-in methods se easily mil
jata hai. find() first index return karta hai aur rfind() last index.
Agar pattern exist nahi karta to -1 return hota hai. Ye basic interview
question hai.
"""

def first_occurrence(text, pattern):

    return text.find(pattern)


def last_occurrence(text, pattern):

    return text.rfind(pattern)


print()

print("First Occurrence :")
print(first_occurrence("banana", "ana"))

print()

print("Last Occurrence :")
print(last_occurrence("banana", "ana"))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 6. LARGEST & SMALLEST STRING
# ============================================================

"""
THEORY (Interview Explanation)

Lexicographical order dictionary order jaisa hota hai. Python me max()
largest string aur min() smallest string return karta hai. Interview me
kabhi manually compare karne ko bhi bola ja sakta hai, lekin built-in
methods generally acceptable hote hain.
"""

def largest_smallest(words):

    return max(words), min(words)


words = ["apple", "mango", "banana", "zebra"]

print()

print("Largest & Smallest String :")
print(largest_smallest(words))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 7. SORT STRINGS
# ============================================================

"""
THEORY (Interview Explanation)

Strings ko lexicographical order me arrange karna sorting problem hai.
Python ka sorted() function default dictionary order me sort karta hai.
Ye String Sorting aur Lexicographical comparison ka common interview
question hai.
"""

def sort_strings(words):

    return sorted(words)


print()

print("Sort Strings :")
print(sort_strings(words))


# Time  : O(n log n)
# Space : O(n)



# ============================================================
# 8. COMPARE TWO STRINGS
# ============================================================

"""
THEORY (Interview Explanation)

Do strings ko compare karne ke liye equality (==), greater than (>)
aur less than (<) operators use kiye jate hain. Python automatically
lexicographical comparison karta hai. Ye String Basics ka simple
interview question hai.
"""

def compare_strings(a, b):

    if a == b:
        return "Equal"

    elif a > b:
        return "First String is Greater"

    else:
        return "Second String is Greater"


print()

print("Compare Strings :")
print(compare_strings("apple", "banana"))


# ============================================================
# Expected Output
# ============================================================

# String Compression :
# a3b2c4

# Run Length Encoding :
# w4a3d1e1x1

# Naive Pattern Search :
# [0, 9, 12]

# Count Pattern Occurrences :
# 3

# First Occurrence :
# 1

# Last Occurrence :
# 3

# Largest & Smallest String :
# ('zebra', 'apple')

# Sort Strings :
# ['apple', 'banana', 'mango', 'zebra']

# Compare Strings :
# Second String is Greater


# ============================================================
# Complexity
# ============================================================

# String Compression       O(n)
# Run Length Encoding      O(n)
# Naive Pattern Search     O(n × m)
# Count Pattern            O(n × m)
# First/Last Occurrence    O(n)
# Largest/Smallest         O(n)
# Sort Strings             O(n log n)
# Compare Strings          O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Compression = Character + Count
# ✔ RLE is based on Compression.
# ✔ Naive Search checks every possible position.
# ✔ find() -> First Occurrence
# ✔ rfind() -> Last Occurrence
# ✔ sorted() sorts lexicographically.
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# STRINGS PATTERN COMPLETE ✅
# ============================================================