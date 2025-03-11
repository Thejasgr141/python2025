def is_palindrome(s):
    s = s.lower().replace(" ", "") 
    return s == s[::-1]  
text = input("Enter a string: ")

if is_palindrome(text):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
