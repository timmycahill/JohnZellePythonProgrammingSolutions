# exercise7.py
#       A Caesar cipher is a simple substitution cipher based on the idea of
#   shifting each letter of the plaintext message a fixed number (called the
#   key) of positions in the alphabet. For example, if the key value was 2, the
#   word "Sourpuss" would be encoded as "Uqwtrwuu." The original message can be
#   recovered by "reencoding" it using the negative of the key.
#       Write a program that can encode and decode Caesar ciphers. The input to
#   the program will be a string of plaintext and the value of the key. The
#   output will be an encoded message where each character in the original
#   message is replaced by shifting it key characters in the Unicode character
#   set. For example, if ch is a character in the string and key is the amount
#   to shift, then the character that replaces ch can be calculated as:
#   chr(ord(ch) + key).

def main():
    # Introduction
    print("This program encodes/decodes a message using the Caesar Cipher.\n")
    
    # Get string and key
    message = input("Enter a message to be encoded/decoded: ")
    key = eval(input("Enter a value for the key: "))

    # Encode/Decode string
    cipher = ""
    for ch in message:
        cipher += chr(ord(ch) + key)

    # Return encoded/decoded string
    print("The encoded/decoded message is {0}.".format(cipher))

main()
