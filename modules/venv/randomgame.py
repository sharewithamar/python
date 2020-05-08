from random import randint
import sys
#generate a number 1-10
answer = randint(int(sys.argv[1]),int(sys.argv[2]))
print(answer)
#get input from user
#input check is a number 1-10
while True:
    try:
        guess = int(input('guess a number 1~10:  '))
        if 0 < guess < 11:
            if(guess == answer):
                print('you guessed it right')
                break
            else:
                print('try again')
                continue
        else :
            print('enter within range')
            continue
    except ValueError:
        print('please enter a number')
        continue


#check if the number is right guess otherwise ask again

