def isPalindrome(s):
    return s == s[::-1]
 
s = input("Enter a string: ")
ans = isPalindrome(s)
 
if ans:
    print("Palindrome")
else:
    print("Not a palindrome")
