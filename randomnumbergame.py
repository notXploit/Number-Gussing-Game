import random
from time import sleep
sleep(0.5)
print('Game By Yasser Mob')
sleep(0.5)
print('instagram : real.yassermob')
sleep(2)
difficult = input('Select Game Difficult / Easy / Normal / Hard: ')
if difficult == 'Easy':
    easynum = random.randint(0,50)
    print('The number between 0 to 50 !')
    sleep(1)
    while True:
        try:
          easyguss = int(input('Enter Your Guss Number: '))
        except:
            sleep(1)
            print('this is not a number !')
            continue
        if easyguss > 50:
            sleep(1)
            print('the number between 0 to 50 !')
            continue
        if easyguss > easynum:
            sleep(1)
            print('Lower !')
            continue
        elif easyguss < easynum:
            sleep(1)
            print('Higher !')
            continue
        elif easyguss == easynum:
            sleep(1)
            print('You Won ! , The number is',easynum)
            sleep(2)
            quit()
        else:
            quit()
elif difficult == 'Normal':
    normalnum = random.randint(0,150)
    print('the number between 0 to 150 !')
    sleep(1)
    while True:
        try:
           normalguss = int(input('enter your guss number: '))
        except:
            sleep(1)
            print('this is not a number !')
            continue
        if normalguss > 150:
            sleep(1)
            print('the number between 0 to 150 !')
            continue
        if normalguss > normalnum:
            sleep(1)
            print('Lower')
            continue
        elif normalguss < normalnum:
            sleep(1)
            print('Higher !')
            continue
        elif normalguss == normalnum:
            sleep(1)
            print('You won ! , The number is, ',normalnum)
            sleep(2)
            quit()
        else:
            quit()
elif difficult == 'Hard':
    hardnum = random.randint(0,500)
    print('the number between 0 to 500 !')
    sleep(1)
    while True:
        try:
          hardguss = int(input('enter your guss number: '))
        except:
            sleep(1)
            print('this is not a number !')
            continue
        if hardguss > 500:
            sleep(1)
            print('the number between 0 to 500 !')
            continue
        if hardguss > hardnum:
            sleep(1)
            print('Lower !')
            continue
        elif hardguss < hardnum:
            sleep(1)
            print('Higher !')
            continue
        elif hardguss == hardnum:
            sleep(1)
            print('You Won ! The number is ,',hardnum)
            sleep(2)
            quit()
# Random Number Gussing Game
# By Yasser Mob
# instagram : real.yassermob








