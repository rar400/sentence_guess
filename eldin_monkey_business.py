#Create a script that simulates three monkeys (Lenny, Moe, and Joocems) communicating with their zoo keeper;
# they are given a list of words to point at, and will be awarded for repeating the sentence given to them by the zoo keeper.
#The monkeys are not very smart and must use the word_assist function provided below to pick their words, they must also
#Take turns one at a time communicating with the zoo keeper.
#You have 2 goals, make a working simulation, and make your simulation take the least amount of time (try to beat the class)
#help by eldin pita


import random

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
                if correct_guesses[i] == '':
                    monkey_choice = random.choice(words_copy)
                    monkey_sentence.append(monkey_choice)
                    words_copy.remove(monkey_choice)
                else:
                    monkey_sentence.append(correct_guesses[i])
            if monkey_sentence not in picked_sequences:
                print("Monkey picked sequence:",monkey_sentence)
                break
        if monkey_sentence == words:
            print("It took",tries,"tries for the monkey to follow the sequence.")
            break
        else:
            for i in range(len(monkey_sentence)):
                if monkey_sentence[i] == words[i]:
                    print("Zookeper:",monkey_sentence[i],"is in the correct place.")
                    correct_guesses[i] = monkey_sentence[i]
        picked_sequences.append(monkey_sentence)
        tries += 1

word_assist()
