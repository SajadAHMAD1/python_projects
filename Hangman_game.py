


                    #### Python Project 5: Hangman Game (Repeated Characters of a Word Advanced Version) ####

#Programmer: Dr. Sajad Ahmad Rather
#Language: Python
#Dated: 5th June 2023 (Monday)


from random import choice
# Random word
word = ['able','about','account','acid','across','act','addition','adjustment','advertisement','after','again','against','agreement','fuel','crush','cry']
actual_word = choice(word)
#print(f'Actual word: {actual_word}')
list_word = list(actual_word)
#print(list_word)

# actual_word = input('Enter the word: ')
# list_word = list(actual_word)
#print(list_word)

list_word1 = list(actual_word)

#print(list_word1)

length_list = len(list_word1)
#print(length_list )

for i in range(length_list):
    list_word1[i] = ' '

new_list_word = list_word1
#print(new_list_word)

correct_char = []

reserve_words = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l',
                 'm','n','o','p','q','r','s','t','u','v','w','x','y',
                 'z']

guess_allowed = 8

# Create dashes of a given word
p = ''.join(list_word)
#print(p)

for j in reserve_words:
    print('\n')
    print(f'Guess character of this word: {new_list_word}')
    guess = input('Enter the guess character: ')
    if guess in reserve_words:
        if guess in list_word:
            if correct_char.count(guess) < list_word.count(guess):
                guess_allowed = guess_allowed + 1
                print(f'Remaining Guesses: {guess_allowed}')
                correct_char.append(guess)
                #print(f'Correct characters: {correct_char}')

                #Method-I: Decreasing length by one and removing empty spaces one at a time
                #q = len(new_list_word) - 1
                #print(f'Modified word length: {q}')
                #new_list_word.remove(" ")
                #print(f'Modified word:{new_list_word}')

                #Method-II: Filling empty space with the desired character like ['b',' ',' ',' '], ['b','l',' ',' '], ....
                #(Distinct words)
                #char_index = list_word.index(guess)
                #print(char_index)
                #new_list_word.insert(char_index,guess)
                # new_list_word.remove(" ")
                #print(f'Modified word:{new_list_word}')
                #print(f'Modified word:{new_list_word}')
                for i in range(len(new_list_word)):
                    #if list_word.count(guess) > 1:

                    if  list_word[i] == guess:
                        if list_word[i] == new_list_word[i]:
                            continue
                        new_list_word.pop(i)
                        new_list_word.insert(i, guess)
                        print(f'Modified word:{new_list_word}')
                        break

                    #break
                        #list_word.remove(guess)
                        # print(f'Modified word:{new_list_word}')
                    #break
            else:
                guess_allowed = guess_allowed - 1
                print(f'Remaining Guesses: {guess_allowed}')
        else:
            guess_allowed = guess_allowed - 1
            print(f'Remaining Guesses: {guess_allowed}')



    if len(correct_char) == len(list_word):
        print('...You Won the Game...')
        if sorted(correct_char) == sorted(list_word):
            print(f'This is the word you guessed: {p}')
        break
    if guess_allowed == 0:
        print('...You Lose the Game...')
        break