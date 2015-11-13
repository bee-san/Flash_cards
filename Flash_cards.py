#!python3
# allows us to access a random 'key' in the dictionary
import random
from collections import Counter
import time
# the questions/answer dictionary

my_dict_CS = Counter({
    "Base-2 number system": "binary",
    "Number system that uses the characters 0-F": "hexidecimal",
    "7-bit text encoding standard": "ascii",
    "16-bit text encoding standard": "unicode",
    "A number that is bigger than the maximum number that can be stored": "overflow",
    "8 bits": "byte",
    "1024 bytes": "kilobyte",
    "Picture Element. The smallest component of a bitmapped image": "pixel",
    "A continuously changing wave, such as natural sound": "analogue",
    "the number of times per second that a wave is measured": "sample rate",
    "A bunary representation of a program": "machine code",
    "Name of the first ever computer?": "Colusus",
    "The brain of the computer is?": "CPU",
    "What is 1NF?": "first normal form is a data normalisation type, there are 3 rules to 1NF. It MUST have a primary key."
                    " It MUST have unique data and Atomisd. It MUST not contain repeating data\nand it has attribute headings.",
    "How should primary keys be generated?" : "Randomly",
    "Name 3 topologies in networking" : "Star, Bus and hybrid.",
    "What is hybrid?" : "when you take the best bits of 2 things and combinend them to make it better",
    "What does each column have in a database?" : "A keyword to represent information. like Side dish or Cash.",
    "What is a string?" : "A seqeuence of charecters",
    "What is an integer?" : "A whole number",
    "What is a float?" : "A decimal number",
    "What does PERT stand for?" : "Program Evalaution Review Technique",
    "What ways do arrows go in PERT?" : "Arrows MUST go in the left and come out the right, ALWAYS",
    "What's the best way to draw PERT charts on paper?" : "Lined paper, landscape, it's super quick.",
    "What must you always label in a PERT diagram?" : "The diagram it self, PERT DIAGRAM, and it must have a key.",
    "How do you calcualte slack time in a PERT diagram?" : "Earliest finish take away the top number",
    "What was the first computer bug?" : "Anna Lovelace, real bug which short circuited a machine.",
    "What is Pervasive computing?" : "Computers are everywhere. In plants, Washing machines, cars.",
    "What is UNF?" : "Unnormalised data",
    "Order of operations for Boolean Algebra?" : "The order of Boolean operations from high to low priority is NOT, "
                                                 "AND, OR, while expressions inside brackets are always evaluated first.",
    "Why does temporary internet files slow down a browser?" : "The browser takes time to index them",
    "What is fragmentation?" : "Fragmentation is where a file is stored on multiple disks."



})

my_dict_MATH = Counter({
    "Way to remeber Mean, Average etc?": "Hey diddle diddle, the medium is the middle. we add and divide for the"
                                         " mean. the mode is the one you see the most. and the range is the difference inbetween",
    "turn a decimal into a fraction?": "Write the decimal number over 1 - EG 2.5 becomes 2.5/1\nTimes the "
                                       "top number by 10 and do the same to the bottom number keep timsing by 10"
                                       " until both numbers are integers. Simplfy if nessacery.",
    "Turn a fraction into a percentage": "100 divided by bottom number times that answer by top",
    "How to turn a fraction into a decimal": "top number divided by bottom number",
    "Calcualte speed." : "Speed = distance over time"


})

my_dict_ENGLISH = Counter({
    "What does AFOREST stand for?": "Alliteration, Facts, Opinions, Rhetorical, Emotive, Statistics, Three",
    "What makes a good title?" : "A rhetorical question, something which hooks the reader. Anything from AFOREST",
    "What are the 5 W's?" : "Who, What, When, Where and Why?",
    "What are strong paragraph openers to build on the previous point?" : "Furthermore, Additionally, As if this isn't enough"





})


# welcome message
print("\nRevision Quiz")
print("=======================")

# the quiz will end when this variable becomes 'False'
playing = True

# While the game is running
while playing:

    # set the score to 0
    score = 0

    # gets the number of questions the player wants to answer
    reccomended_num = random.randint(1, 20)
    print("\nReccomended number is {}".format(reccomended_num))
    num = int(input("\nHow many questions would you like: "))
    topic = input(str("What are you studying? ENGLISH, MATH, COMPUTER SCIENCE. ")).upper()

    if topic.startswith("E"):
        dict_to_use = my_dict_ENGLISH

    elif topic.startswith("M"):
        dict_to_use = my_dict_MATH

    elif topic.startswith("C"):
        dict_to_use = my_dict_CS

    # loop the correct number of times
    time_start = time.time()
    for i in range(num):

        # the question is one of the dictionary keys, picked at random
        question = (random.choice(list(dict_to_use.keys())))
        # the answer is the string mapped to the question key
        answer = dict_to_use[question]

        # print the question, along with the question number
        print("\nQuestion " + str(i + 1))
        print(question + "? ")

        # get the user's answer attempt
        guess = input("> ")

        # if their guess is the same as the answer
        if guess.lower() == answer.lower():
            # add 1 to the score and print a message
            print("Correct!")
            score += 1
        else:
            print("Nope!")
            print("Correct answer: {}".format(answer))
            guess = input(str("Did you get this? ")).upper()
            # if guess.upper.startswith("Y"):
            if guess.startswith("Y"):
                score += 1

    # after the quiz, print their final score
    print("\nYour final score was " + str(score))
    print("You got {} out of {}!".format(score, num))
    percent = ((score) * 100 / (num))
    percent = int(percent)
    print("You got {}% right!".format(percent))
    time_end = time.time()
    time_finish = int((time_end - time_start))
    print("It took {} seconds for you to complete this quiz!".format(time_finish))
    should_be_total_time = (10 * num)
    print("The normal time to complete this quiz is {} seconds!".format(should_be_total_time))
    difference_in_time = int((should_be_total_time - time_finish))
    print("This is the difference in your time vs the normal time {} seconds!".format(difference_in_time))
    if (percent > 69 and difference_in_time > 25):
        print("Well done! Share this with friends!")

    # store the user's input...
    again = input("\nEnter any key to play again, or 'q' to quit.")

    # and quit if they types 'q'
    if again.lower() == 'q':
        playing = False