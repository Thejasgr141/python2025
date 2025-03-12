def count_vowels(s):
 vowel="aeiouAEIOU"
 return sum (1 for char in s if char in vowel)
text= "Sri Raghavendraya namaha"
print(count_vowels(text))
