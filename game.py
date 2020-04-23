def easy():
    import random
    guessTaken = 0
    totalGuess = 6
    number = random.randint(1, 10)
    print('......Loading')
    print('Well, I am thinking of a number between 1 and 10')
    while guessTaken < 6:
        print('')
        print('Take a guess.')
        guess = input()
        guess = int(guess)	
        print('--------------------------------')
        totalGuess = int(totalGuess) - 1
        totalGuess = str(totalGuess)
        print('NOTE! You have ' + totalGuess + ' guesses left')	
        guessTaken  = guessTaken + 1
        if guess < number:
            print('That was wrong, your guess is too low')
            print('--------------------------------')		
        if guess > number:
            print('That was wrong, Your guess is too high')
            print('--------------------------------')		
        if guess == number:
            break
    if guess == number:
        guessTaken = str(guessTaken)
        print('Good job!, You guessed my number in ' + guessTaken + ' guesses!')
        print('You got it right')
        print('--------------------------------')		
    if guess != number:
        number = str(number)
        print('Game over!')
        print('The number I was thinking of was ' + number)
        print('--------------------------------')
    print("Do you want to play again? 'y/n' ")
    reply = input()
    reply = reply.lower()
    if reply == 'y':
        game()
    elif reply == 'n':
        print('Thanks for playing. Goodbye!')
    else:
        print("please type 'y/n' ")
#easy()
def medium():
    import random
    guessTaken = 0
    totalGuess = 4
    number = random.randint(1, 20)
    print('......Loading')
    print('Well, I am thinking of a number between 1 and 20')
    while guessTaken < 4:
        print('')
        print('Take a guess.')
        guess = input()
        guess = int(guess)	
        print('--------------------------------')
        totalGuess = int(totalGuess) - 1
        totalGuess = str(totalGuess)
        print('NOTE! You have ' + totalGuess + ' guesses left')	
        guessTaken  = guessTaken + 1
        if guess < number:
            print('That was wrong, your guess is too low')
            print('--------------------------------')		
        if guess > number:
            print('That was wrong, your guess is too high')
            print('--------------------------------')		
        if guess == number:
            break
    if guess == number:
        guessTaken = str(guessTaken)
        print('Good job!, You guessed my number in ' + guessTaken + ' guesses!')
        print('You got it right')
        print('--------------------------------')		
    if guess != number:
        number = str(number)
        print('Game over!')
        print('The number I was thinking of was ' + number)
        print('--------------------------------')
    print("Do you want to play again? 'y/n' ")
    reply = input()
    reply = reply.lower()
    if reply == 'y':
        game()
    elif reply == 'n':
        print('Thanks for playing. Goodbye!')
    else:
        print("please type 'y/n' ")
#medium()
def hard():
    import random
    guessTaken = 0
    totalGuess = 3
    number = random.randint(1, 50)
    print('......Loading')
    print('Well, I am thinking of a number between 1 and 50')
    while guessTaken < 3:
        print('')
        print('Take a guess.')
        guess = input()
        guess = int(guess)	
        print('--------------------------------')
        totalGuess = int(totalGuess) - 1
        totalGuess = str(totalGuess)
        print('NOTE! You have ' + totalGuess + ' guesses left')	
        guessTaken  = guessTaken + 1
        if guess < number:
            print('That was wrong, your guess is too low')
            print('--------------------------------')		
        if guess > number:
            print('That was wrong, your guess is too high')
            print('--------------------------------')		
        if guess == number:
            break
    if guess == number:
        guessTaken = str(guessTaken)
        print('Good job!, You guessed my number in ' + guessTaken + ' guesses!')
        print('You got it right')
        print('--------------------------------')		
    if guess != number:
        number = str(number)
        print('Game over!')
        print('The number I was thinking of was ' + number)
        print('--------------------------------')
    print("Do you want to play again? 'y/n' ")
    reply = input()
    reply = reply.lower()
    if reply == 'y':
        game()
    elif reply == 'n':
        print('Thanks for playing. Goodbye!')
    else:
        print("please type 'y/n' ")
#hard()    
def game():
    print ('')
    print ('Hi there!')
    print('--------------------------------')
    print('')
    print ('This is a guessing game. Spoiler alert! 95% of those who play against me, lose')
    print('--------------------------------')
    def choice():
        print('')
        print ('There are 3 levels to this game, which do you want to play?')
        print (' 1 for easy, \n 2 for medium \n 3 for hard')
        response = input()
        print('--------------------------------')
        if response == '1':
            easy()
        elif response == '2':
            medium()
        elif response == '3':
            hard()
        else:
            print('Please choose \n 1. for Easy \n 2. for medium \n 3. for hard')
    choice()
game()
