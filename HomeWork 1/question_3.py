##### Answers to Question 3: Working with Files” Quiz Program”


###########################################
##### Type python quiz program that takes a text or json or csv file as input for (20 (Questions, Answers)). It asks the
##### questions and finally computes and prints user results and store user name and result in separate file csv or json file.

import json

#Result variable to store user's name, answers and final mark
results = {}
final_mark = 0

#Opening the json file
file = open("quiz.json")
quiz = json.load(file)

#Entering student name
user_name = input("Enter your name: ")
#First value is user's name
results ["Name"] = user_name

#There's only two values a user can enter: t for true, f for false
print("Answer \"t\" for True and \"f\" for False")

j = 1
#For loop for items in json file(quiz)
for item in quiz:

	#Answer enter by user
    answer = input(item)
    	#Correct answer from json file, which is first element of list
    correct_answer = quiz[item][0]

	#If user entered a value that's not t or f, show a warning
    if not answer.__eq__("t") and not answer.__eq__("f"):
        print("please answer with \"t\" for True, and \"f\" for False")
        answer = input(item)
        
	#If user answered correctly, increase the mark
    if answer.__eq__(correct_answer):
        print("Correct")
        final_mark += 5
        answer = "correct"

	#If user answered incorrectly, don't change the mark, and output the right answer
    else:
        if correct_answer.__eq__("f"):
            print("Wrong, correct answer is: ", quiz[item][1])
        elif correct_answer.__eq__("t"):
            print("Wrong, correct answer is true")

        answer = "Wrong"
	
	#Add that user answer correctly or incorrectly to question X in results
    results["Question"+str(j)] = answer
    j += 1

results["Result"] = final_mark

print("Thanks for taking the test, your result is: ", str(final_mark)+"/100")

# write results variable to a json file
with open("results.json", "w") as write_file:
    json.dump(results, write_file)

json_string = json.dumps(results)
