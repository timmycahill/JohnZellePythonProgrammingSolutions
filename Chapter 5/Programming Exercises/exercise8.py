# exercise8.py
#       One problem with the previous exercise is that it does not deal with
#   the case when we "drop off the end" of the alphabet. A true Caesar cipher
#   does the shifting in a circular fashion where the next character after "z"
#   is "a." Modify your solution to the previous problem to make it circular.
#   You may assume that the input consists only of letters and spaces. Hint:
#   make a string containing all the letters of your alphabet and use positions
#   in this string as your code. you do not have to shift "z" into "a" just make
#   sure that you use a circular shift over the entire sequence of characters
#   in your alphabet string.

def main():
    # Introduction
    print("This program encodes/decodes a message using the Caesar Cipher.\n")
    
    # Get string and key
    message = input("Enter a message to be encoded/decoded: ")
    key = eval(input("Enter a value for the key: "))

    # Encode/Decode string
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    cipher = ""
    for ch in message:
        cipher += alphabet[(alphabet.find(ch) + key) % len(alphabet)]

    # Return encoded/decoded string
    print("The encoded/decoded message is '{0}'.".format(cipher))

main()

