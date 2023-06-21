##### Answers to Question 1: Python Basics?


###########################################
##### A-If you have two lists, L1=[‘HTTP’,’HTTPS’,’FTP’,’DNS’] L2=[80,443,20,53], convert it to generate this
##### dictionary d={‘HTTP’:80,’HTTPS’:443,’FTP’:20,’DNS’:53 }
##### Answer:

print("A's Answer:")

L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 20, 53]

d = {}

for i in range(0, 4):
    d [L1[i]] = L2[i]

print("dict is :", d)

###########################################
##### B- Generate and print a list of primary numbers from 1 to 1000.
##### Answer:

print("B's Answer:")

prime_list = []

# started loop from 2, because 1 is not a prime number
for number in range(2, 1001):

    # number checking loop (this loop is to check if the number is dividable by all smaller numbers)
    for j in range(2, number+1):

        # if j reached the number we're checking, this means the condition is not broken, and the number is a prime
        if j == number:
            prime_list.append(number)

        # this means the number is not prime, so we break the number checking loop
        elif number % j == 0:
            break

print("prime list is :", prime_list)

###########################################
##### C- L=[‘Network’ , ’Math’ , ’Programming’, ‘Physics’ , ‘Music’]
##### In this exercise, you will implement a Python program that reads the items of the previous list and identifies
##### the items that starts with ‘Ph’ letter, then print it on screen.
##### Answer:

print("C's Answer:")

L = ['Network', 'Math', 'Programming', 'Physics', "Music"]

# for all items in the list, item here represent each string element in the list
for item in L:
    if item.startswith("Ph"):
        print(item)

###########################################
##### D: Using Dictionary comprehension, Generate this dictionary d={1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11}
##### Answer:

print("D's Answer:")

d = {}

for i in range(2, 12):
    d [i-1] = i

print(d)
