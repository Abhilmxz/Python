# def is_palindrome(s):
#     s = s.lower()  # Convert to lowercase for case-insensitive comparison
#     return s == s[::-1]

# user_input = input("Enter a string: ")
# if is_palindrome(user_input):
#     print("Yes, it's a palindrome!")
# else:
#     print("No, it's not a palindrome.")


def is_number_palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num

user_number = int(input("Enter an Number: "))
if is_number_palindrome(user_number):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
34
