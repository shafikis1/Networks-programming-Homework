##### Answers to Question 2: Convert from Binary to Decimal


###########################################
##### Write a Python program that converts a Binary number into its equivalent Decimal number.
##### The program should start reading the binary number from the user. Then the decimal equivalent number must be
##### calculated. Finally, the program must display the equivalent decimal number on the screen.

while True:

    binary_number = input("Enter a binary number to convert to decimal:(Enter \'e\' to end program):")

    # this condition to check if user entered the letter "e" to exit program(break while loop)
    if binary_number.__eq__("e"):
        break

    decimal_number = 0
    j = 1

    input_error = False

    #the loop is reversed, that's to count the decimal from right to left(smallest binary value to biggest)
    for i in reversed(binary_number):

        # this condition is solve input error(check if user entered a non-binary value)
        if i != "0" and i != "1":
            print("INPUT_ERROR ", "please enter a binary number")
            input_error = True
            break

        if i == "1":
            decimal_number += j
        
        # j increases itself for the next loop round like that: 2, 4, 8, 16, 32, 64, 128, 256, ........ 
        j *= 2

    # here the program failed because the user enter an incorrect value, so no output
    if not input_error:
        print("Binary value:", binary_number)
        print("Decimal value:", decimal_number)


