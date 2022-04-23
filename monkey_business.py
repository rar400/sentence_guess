#Create a script that simulates a monkey communicating with their zoo keeper;
# they are given a list of words to point at, and will be awarded for repeating the sentence given to them by the zoo keeper.
#The monkeys are not very smart and must use the word_assist function provided below to pick their words, they must also
#Take turns one at a time communicating with the zoo keeper.
#You have 2 goals, make a working simulation, and make your simulation take the least amount of time (try to beat the class)

import random
import datetime

start_time = datetime.datetime.now()
print(start_time)

def word_assist(words=['I','think','therefore','I','am']):
    correct_guesses = ['' for i in range(len(words))]
    picked_sequences = []
    tries = 0
    while True:
        while True:
            words_copy = words.copy() # create copy of the words list
            monkey_sentence = []
            # this for loop will enable the monkey to choose create a sequence
            for i in range(len(words)):
                if correct_guesses[i] == '': # if its blank it means that the monkey has already picked a correct word
                    monkey_choice = random.choice(words_copy) # monkey picks letter
                    monkey_sentence.append(monkey_choice) # adds picked words to monkey sentence
                    words_copy.remove(monkey_choice) # removes picked word from copied list
                else:
                    monkey_sentence.append(correct_guesses[i]) # add to the monkey sentence
            if monkey_sentence not in picked_sequences: # checks if monkey has already guessed the sentence
                print("Monkey picked sequence:",monkey_sentence)
                break  # ends the while loop
        if monkey_sentence == words:
            print("It took",tries,"tries for the monkey to follow the sequence.")
            break
        else:
            for i in range(len(monkey_sentence)): # loops for remanining guesses words
                if monkey_sentence[i] == words[i]: # zookeerper checking the correct guesses so far
                    print("Zookeper:",monkey_sentence[i],"is in the correct place.")
                    correct_guesses[i] = monkey_sentence[i]
        picked_sequences.append(monkey_sentence)
        tries += 1  # adds to the tally for guesses words

    end_time = datetime.datetime.now()
    print(end_time)
word_assist()

