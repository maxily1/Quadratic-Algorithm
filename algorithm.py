'''
Project Name: Quadratic Cipher

Project Description: My first try of making an algorithm all by myself. 

Author: Max Iliouchenko
Date of Project Start: 23/02/2021
Date of Project End: N/A
'''

# Importing required modules
import math

# Choose whether it's going to be a file or just a message to input
choice = input("Please select (encode \ decode): ")
choice = choice.lower()

type_choice = input("Please enter your choice (message \ file): ")
type_choice = type_choice.lower()

# Start of program
# Checking if the user would like to encode or deocde
if choice == "encode":
    # Encode - message chapter
    if type_choice == "message":
        ascii_list = []
        message = input("Please enter your message: ")
        for char in message:
            char_ascii = ord(char)
            ascii_list.append(char_ascii)

        encoded_list = []
        for num in ascii_list:
            encoded_num = math.sqrt(num)
            encoded_list.append(encoded_num)

        encoded_str = ','.join(str(n) for n in encoded_list)
        print("The encoded result is: " + encoded_str)


# Decode - message chapter
if choice == "decode":
    # Decode - message chapter
    if type_choice == "message":
        message = input("Please enter your message: ")
        encoded_list = message.split(',')
        char_list = []
        for encoded_char in encoded_list:
            decoded_char = float(encoded_char) ** 2.0
            decoded_char = round(decoded_char)
            print(decoded_char, end=" ")
            char = chr(int(decoded_char))
            char_list.append(char)
    
        decoded_str = ''.join(char_list)
        print("\nThe decoded result is: " + decoded_str)



