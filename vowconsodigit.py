# ANALYZE STRING INPUT
a = input()
vowel_count = 0
consonant_count = 0
digit_count = 0
vowels = "AEIOUaeiou"
for char in a:
    if char.isdigit():
        digit_count+=1
    elif char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print(consonant_count)
print(vowel_count)
print(digit_count)


