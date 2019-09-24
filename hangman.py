import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("\t", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()
secret_word = choose_word(wordlist)
# end of helper code



def listDatShit(string, replacement):   #my own 
    """ takes a string, and returns a list with whatever replacement you'd like"""
    l = []
    for i in range(0, len(string)):
        l.append(replacement)
    return l

def stringFromList(lisst, separator):  #my own
    """takes a list,
    concatenates all the separate entries into a string,
    using whatever separator u like between the separate entries only"""
    s = ""
    for i in range(0, len(lisst)-1):
        s = s + lisst[i] + separator
    s = s + lisst[-1]
    return s

def UniqueLetters(string):  #my own
    """ Take a string and returns # of unique letters"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = list(letters)
    uniqueSet = []
    x = list(string)
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            uniqueSet.append(x[i])
    return len(uniqueSet)



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    points = 0
    for i in range(0, len(letters_guessed)):
        if letters_guessed[i] in secret_word:
            points += 1
    if points == UniqueLetters(secret_word):
        return True
                
#secret_word = "oski"
#letters_guessed = ["a", "b", "c", "d", "o", "s", "k", "i"]
#print(is_word_guessed(secret_word, letters_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessList = listDatShit(secret_word, "_")
    secretList = list(secret_word)

    for i in range(0, len(letters_guessed)):
        for j in range(0, len(secretList)):
            if letters_guessed[i] == secretList[j]:
                guessList[j] = letters_guessed[i]
    return(stringFromList(guessList, " "))

#secret_word = "oski"
#letters_guessed = ["s", "b", "i", "o", "l", "j"]
#print(get_guessed_word(secret_word, letters_guessed))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''    
    lettersLeftList = list("abcdefghijklmnopqrstuvwxyz")    #i moved it from outside, hope it won't case bug later
    for i in range(0,len(letters_guessed)):
                   if letters_guessed[i] in lettersLeftList:
                       lettersLeftList.remove(letters_guessed[i])
    lettersLeftList = stringFromList(lettersLeftList, "")
    return lettersLeftList

#letters_guessed = ["a", "b", "c", "d", "e", "f"]
#print(get_available_letters(letters_guessed))
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    '''
    print("The secret word has %s letters:\t" %len(secret_word), stringFromList(listDatShit(secret_word, "_"), " "), "\n")
    guessSingle = []
    letters_guessed = []
    lettersLeft = "abcdefghijklmnopqrstuvwxyz"
    lettersLeftList = list(lettersLeft)
    guessesLeft = 6
    warningsLeft = 3
    print("you have %s warnings left" %(warningsLeft))
    while guessesLeft > 0:
        print("you have %s guesses left" %(guessesLeft))
        print("these are your available guesses:  ", get_available_letters(letters_guessed))
        guessSingle = input("What is your guess?\t")
        guessSingle = guessSingle.lower()
        if guessSingle not in lettersLeftList:
            if guessSingle not in "abcdefghijklmnopqrstuvwxyz":
                print("that's not a letter!")
            elif guessSingle in letters_guessed:
                print("you already guessed that!")
            else:
                print("wtf was that? invalid input")
            if warningsLeft > 1:
                print("\tYou have %s warnings left" %(warningsLeft-1))
            if warningsLeft == 1:
                print("\tLAST WARNING!")
            warningsLeft -= 1
            if warningsLeft < 0:
                if guessesLeft == 1:
                    print("shit, you done messed up now!")
                    guessesLeft -= 1
                else:
                    print("Man! I told u to stop messing around! You lose a guess!")
                    guessesLeft -= 1
        if guessSingle in lettersLeftList:
            letters_guessed.append(guessSingle)
            lettersLeftList.remove(guessSingle)
            if guessSingle in secret_word:
                print("Good guess!\t", end = "")
                if (is_word_guessed(secret_word, letters_guessed)) == True:
                    print("\n\nYOU WON!!!\n\tAnswer is %s" %secret_word)
                    score = guessesLeft * UniqueLetters(secret_word)
                    print("YOUR SCORE IS...", score, "\n\n")
                    break
            if guessSingle not in secret_word:
                vowels = ["a", "e", "i", "o", "u"]
                if guessSingle in vowels:
                    print("oh snap! wrong vowels cost u 2 guesses!", end = "")
                    guessesLeft -= 2
                else:
                    print("newwwp!\t", end = "")
                    guessesLeft -= 1            

        print(get_guessed_word(secret_word, letters_guessed))
        guessSingle = []
        print("---------------------------------------------------------\n")
    if guessesLeft <= 0:
        print("\n\nawww, too bad, you lose!  Word is...\t", secret_word, "\n\n")
#TESTING CODES HERE
#hangman("buttboy")
#secret_word = choose_word(wordlist)
#hangman(secret_word)
#IDEA: Turn this into a wheel of fortune game, where there are spaces & hyphens   
# ----------------------------------------------------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #my_word = get_guessed_word(secret_word, letters_guessed)
    my_word_list = my_word.split(" ")
    other_word_list = list(other_word)
    points = 0
    if len(my_word_list) != len(other_word_list):
        return False
    if len(my_word_list) == len(other_word_list):   
        for i in range(0, len(my_word_list)):
            if my_word_list[i] == other_word_list [i]:
                #print("testing", my_word_list[i], "vs", other_word_list [i])
                #print("true for now, get 1 point")
                points +=1
            elif my_word_list[i] == "_":
                if other_word_list[i] in my_word_list:
                    points = 0
                else:
                    points += 1
            #print("testing: %s points earned" %points)
            if points != (i+1):
                #print("testing, failed as soon as u encounter a false match")
                return False
                break
    if points == len(my_word_list):
        #print("testing, revealed letters in my_word match other_word!")
        return True
    #else:
        #print("testing, weird, should've been rejected already, this is a redundant step")
        #return False
                    
#TESTING
    """
letters_guessed = ["a", "e", "l", "p"]
secret_word = "arple"
other_word = "apple"
my_word = get_guessed_word(secret_word, letters_guessed)
print("TEST", my_word, "vs", other_word)
print("TEST", match_with_gaps(my_word, other_word))  
"""


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    print("Searching for possible answers...")
    matchExist = False
    for i in wordList:
        if (match_with_gaps(my_word, i)) == True:
            print(i, end = " ")
            matchExist = True
    if matchExist == False:
          print("\tNo matches found")
    print("")
    return None
    
# TESTING
#letters_guessed = ["a", "p", "l"]
#secret_word = "amply"
#my_word = get_guessed_word(secret_word, letters_guessed)
#print("TEST", show_possible_matches(my_word))




def hangman_with_hints(secret_word):
    '''
    same hangman, except with the modification/addition of...
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    '''
    print("The secret word has %s letters:\t" %len(secret_word), stringFromList(listDatShit(secret_word, "_"), " "), "\n")
    guessSingle = []
    letters_guessed = []
    lettersLeft = "abcdefghijklmnopqrstuvwxyz"
    lettersLeftList = list(lettersLeft)
    guessesLeft = 6
    warningsLeft = 3
    print("you have %s warnings left" %(warningsLeft))
    my_word = ""
    while guessesLeft > 0:
        print("you have %s guesses left" %(guessesLeft))
        print("these are your available guesses:  ", get_available_letters(letters_guessed))
        guessSingle = input("What is your guess?\t")
        guessSingle = guessSingle.lower()
        if guessSingle not in lettersLeftList:
            if guessSingle == "*":
                show_possible_matches(my_word)          
            else:
                if guessSingle not in "abcdefghijklmnopqrstuvwxyz":
                    print("that's not a letter!")
                elif guessSingle in letters_guessed:
                    print("you already guessed that!")
                else:
                    print("wtf was that? invalid input")
                if warningsLeft > 1:
                    print("\tYou have %s warnings left" %(warningsLeft-1))
                if warningsLeft == 1:
                    print("\tLAST WARNING!")
                warningsLeft -= 1
                if warningsLeft < 0:
                    if guessesLeft == 1:
                        print("shit, you done messed up now!")
                        guessesLeft -= 1
                    else:
                        print("Man! I told u to stop messing around! You lose a guess!")
                        guessesLeft -= 1
        if guessSingle in lettersLeftList:
            letters_guessed.append(guessSingle)
            lettersLeftList.remove(guessSingle)
            if guessSingle in secret_word:
                print("Good guess!\t", end = "")
                if (is_word_guessed(secret_word, letters_guessed)) == True:
                    print("\n\nYOU WON!!!\n\tAnswer is %s" %secret_word)
                    score = guessesLeft * UniqueLetters(secret_word)
                    print("YOUR SCORE IS...", score, "\n\n")
                    break
            if guessSingle not in secret_word:
                vowels = ["a", "e", "i", "o", "u"]
                if guessSingle in vowels:
                    print("oh snap! wrong vowels cost u 2 guesses!", end = "")
                    guessesLeft -= 2
                else:
                    print("newwwp!\t", end = "")
                    guessesLeft -= 1
        my_word = get_guessed_word(secret_word, letters_guessed)
        print(my_word)
        guessSingle = []
        print("---------------------------------------------------------\n")
    if guessesLeft <= 0:
        print("\n\nawww, too bad, you lose!  Word is...\t", secret_word, "\n\n")


    
# To test
# if __name__ == "__main__":
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)





