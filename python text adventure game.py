import random
import time
global sum
sum = 0
global heal
heal = 2
global health
health = 8
lefsum = 0
strsum = 0
ritsum = 0


def hangman():
    print("Start guessing...")
    time.sleep(0.5)
    word = ['secret', 'hello', 'new', 'python', 'hang', 'fiction']
    guessingword = ''
    turns = 10
    wor = random.randint(0, 5)
    while turns > 0:
        failed = 0
        for char in word[wor]:

            if char in guessingword:
                print(char)
            else:
                print("_"),
                failed += 1
        if failed == 0:
            print("!!!congratulation You won!!!")

            break
        guess = input("guess a character:")
        guessingword += guess
        if guess not in word[wor]:
            turns = turns- 1
            print("Wrong")
            print("You have",turns, 'more guesses')
            if turns == 0:
                print("You Loose")
    return turns


def dice():
    print("press 1 to roll the dice")
    while 1 > 0:
        diceroll = int(input("enter input : "))
        if diceroll == 1:
            break
        else:
            print(" invalid input ")
    no = random.randint(1 , 3)
    print("you got : " , no)
    return no


def dicesteps(x):
    global sum
    global health
    sum= sum+x
    if sum==1:
        print("!!!!!!YOU FELL IN A TRAP!!!!!!!")
        time.sleep(2)
        print("your health decline by 4 ")

        health=health-4
        dicesteps(dice())
    elif sum==2:
        print("the way is clear you can move ahead")
        time.sleep(2)
        dicesteps(dice())
    elif sum==3:
         print("\nSO YOU HAVE REACHED HERE \nSO BEFORE MOVING AHEAD LET ME ASK YOU A QUESTION ")
         time.sleep(3)
         print("\nDO you want to answer the question ")
         choice=int(input("press 1 for yes and 2 for no"))
         if choice==1:
             print("OHH SO YOU WANT TO ANSWER MY QUESTION GREAT THEN I WILL ASK IT ")
             time.sleep(3)
             print("\nIF THERE ARE sixtea CUPS ON A TABLE ,AND  2 FELL DOWN ")
             print("SO HOW MANY CUPS LEFT ON THE TABLE ")
             time.sleep(4)
             ans=input("enter the no : ")
             if ans=='4' or ans=='four':
                 print("correct answer you may pass and roll the dice again ")
                 dicesteps(dice())
             else:
                 print("!!wrong answer!! ")
                 time.sleep(2)
                 print("the guardian crushed you with a table you lost")
                 time.sleep(3)
                 print("DO YOU WANT TO PLAY AGAIN ")
                 deathwish = input("ENTER YES OR NO ")
                 if deathwish == 'yes':
                     _maingame()
                 else:
                     print("thanks for playing")
                     sleep.time(100000)
         else:
             print("you are not daring enough to answer my question so you can't move forward")
             time.sleep(3)
             print("the guardian trapped you inside the cave and you died there ")
             time.sleep(3)
             print("GAME OVER YOU DIED OF HUNGER AND THIRST THERE")
             time.sleep(3)
             print("DO YOU WANT TO PLAY AGAIN ")
             deathwish = input("ENTER YES OR NO ")
             if deathwish == 'yes':
                 _maingame()
             else:
                 print("thanks for playing")
                 sleep.time(100000)
    elif sum==4:
         print("you fell in a trap Health reduced by 4 ")

         health = health - 4

         if health == 0 :
             print("\nyou died from blood loss : ")
             print('\n game over ')
             time.sleep(3)
             print("DO YOU WANT TO PLAY AGAIN ")
             deathwish = input("ENTER YES OR NO ")
             if deathwish == 'yes':
                 _maingame()
             else:
                 print("thanks for playing")
                 sleep.time(100000)
         dicesteps(dice())
    elif sum == 5:
        print("you are safe no traps here you may roll the dice again ")
        time.sleep(2)
        dicesteps(dice())
    elif sum >= 6:
        print("this is a bonus tile your health increased by 4 and further you can use healing potion ")
        time.sleep(4)

        health=health + 4
        print("\nDO YOU WANT TO USE HEALING POTION  ")
        choice=input("enter yes or no : ")
        if choice == 'yes':

            health = health + 3
            print("\nyour current health is : ", health)
    return


def lefpath(y):
    global lefsum
    global health
    lefsum = lefsum + y
    if lefsum == 1:
        print(" relax your are safe at this step ")
        time.sleep(3)
        print("you may roll the dice again")
        time.sleep(2)
        lefpath(dice())
    elif lefsum == 2:
        print("\nthe guardian wants to ask an question ")
        time.sleep(2)
        print("\n I AM AN UNUSUAL NUMBER. REMOVE ONE LETTER AND I BECOME EVEN . WHAT NUMBER AM I?")
        time.sleep(7)
        chances = 2
        while chances > 0:
            answ=input("enter answer : ")
            if answ == "seven" or answ == 7:
                print("!!!!!congratulation correct answer!!!!!")
                print("you may pass from here roll the dice again ")
                break
            else:
                print("!!!!WRONG ANSWER!!!!")
                chances = chances - 1
        if chances ==0:
            print("you lost ")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        else:
            lefpath(dice())
    elif lefsum == 3:
        print("\nON YOU WAY FURTHER YOU ENCOUNTERED A GOBLIN ")
        time.sleep(3)
        print("\nnow you have 2 choices ")
        time.sleep(2)
        print("\nchoice 1: you saw a dark chamber nearby and sneaked in there \nchoice 2:you throw all of your gold into the nearby chamber in front of the goblin")
        time.sleep(6)
        choice=int(input("enter choice 1 or 2 "))
        if choice == 1:
            print("you went into the chamber deep and deep and found out that it is the den of goblins  ")
            time.sleep(4)
            print("a goblin ran to your side and chopped your head off")
            time.sleep(3)
            print("!!!!!its a game over for you!!!!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif choice == 2:
            print("\nwell the goblins are  creatures who  love's gold so he followed the gold pouch. \nmeanwhile you ran away from that  place  ")
            time.sleep(3)
            print("you can now roll the dice again")
            time.sleep(2)
            lefpath(dice())
        else:
            print(" you panicked and could'nt decide anything the goblin killed you ")
            print("!!!!!game over!!!!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
    elif lefsum == 4:
        print("\nthe guardian wants to ask an question ")
        time.sleep(2)
        print("\nNEVER RESTING ,NEVER STILL .MOVING SILENTLY FROM HILL TO HILL ,IT DOES NOT RUN ,WALK OR TROT")
        print("ALL IS COOL WHERE IT IS NOT ")
        time.sleep(7)
        chances = 2
        while chances > 0:
            answ = input("enter answer : ")
            if answ == "sunlight" or answ == "sunshine" or answ=="sunrays":
                print("!!!!!congratulation correct answer!!!!!")
                print("you may pass from here roll the dice again ")
                break
            else:
                print("!!!!WRONG ANSWER!!!!")
                chances = chances - 1
        if chances == 0:
            print("you lost ")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        else:
            lefpath(dice())
    elif lefsum == 5:
        print("\nnow you have entered a forest like stage with trees and a sky ")
        time.sleep(3)
        print("\nYOU SAW A WOLF COMING YOUR WAY ")
        time.sleep(2)
        print("\nnow what will you do you have the following choices")
        time.sleep(3)
        print("choice 1: climb a nearby tree \n choice 2: run in a different direction \n choice 3: lie there and pretend to be dead")
        choice=int(input("enter your choice 1 , 2 or 3 : "))
        if choice==1:
            print("\nyou are safe the wolf left without eating you congratulation you can now roll the dice again ")
            time.sleep(4)
            lefpath(dice())
        elif choice == 2:
            print("idiot what do you think you are a cheetah ----- the wolf chased you and ate you--")
            print("!!GAME OVER!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif choice == 3:
            print("\nyou are the king of IDIOTS ")
            time.sleep(2)
            print("\nit was an easy meal the wolf replied after eating you ")
            print("!!!GAME OVER !!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
    elif lefsum >= 6:
        print("\non moving further  you saw the same injured person whom you encounterd at the beginning with the king ")
        time.sleep(4)
        print("you were shocked on seeing them there")
        time.sleep(3)
        print("BOTH OF THEM LAUGHED AND SAID YOU PASSED THE TEST  ")
        time.sleep(3)
        print(" THIS WAS YOUR TEST OF MENTAL STRENGTH FOR BECOMING THE NEXT KING ")
        print("!!!!THE END!!!")
        time.sleep(3)
        print("DO YOU WANT TO PLAY AGAIN ")
        deathwish = input("ENTER YES OR NO ")
        if deathwish == 'yes':
            _maingame()
        else:
            print("thanks for playing")
            sleep.time(100000)


def ritpath(z) :
    global ritsum
    ritsum = ritsum + z
    if ritsum == 1:
        print("\nno trap here you are free to move forward you may roll the dice again")
        time.sleep(3)
        ritpath(dice())
    elif ritsum == 2:
        print("THE GUARDIAN CHALLENGE YOU FOR A WORD GUESS GAME ")
        result = hangman()
        if result == 0:
            print("your are captured in that stage forever")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif result >0:
            print("\nyou may roll the dice again")
            ritpath(dice())
    elif ritsum == 3:
        print("\nON YOU WAY FURTHER YOU ENCOUNTERED A GOBLIN ")
        time.sleep(3)
        print("\nnow you have 2 choices ")
        time.sleep(2)
        print("\nchoice 1: you saw a dark chamber nearby and sneaked in there \nchoice 2:you throw all of your gold into the nearby chamber in front of the goblin")
        time.sleep(6)
        choice = int(input("enter choice 1 or 2 "))
        if choice == 1:
            print("you went into the chamber deep and deep and found out that it is the den of goblins  ")
            time.sleep(4)
            print("a goblin ran to your side and chopped your head off")
            time.sleep(3)
            print("!!!!!its a game over for you!!!!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif choice == 2:
            print("\nwell the goblins are  creatures who  love's gold so he followed the gold pouch. \nmeanwhile you ran away from that  place  ")
            time.sleep(3)
            print("you can now roll the dice again")
            time.sleep(2)
            ritpath(dice())
        else:
            print(" you panicked and could'nt decide anything the goblin killed you ")
            print("!!!!!game over!!!!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
    elif ritsum == 4:
        print("THE GUARDIAN CHALLENGE YOU FOR A WORD GUESS GAME ")
        time.sleep(4)
        print("if you get the same word again then you are lucky")
        result = hangman()
        if result == 0:
            print("your are captured in that stage forever")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif result > 0:
            print("\nyou may roll the dice again")
            ritpath(dice())
    elif ritsum == 5:
        print("\nnow you have entered a forest like stage with trees and a sky ")
        time.sleep(3)
        print("\nYOU SAW A WOLF COMING YOUR WAY ")
        time.sleep(2)
        print("\nnow what will you do you have the following choices")
        time.sleep(3)
        print("choice 1: climb a nearby tree \n choice 2: run in a different direction \n choice 3: lie there and pretend to be dead")
        choice = int(input("enter your choice 1 , 2 or 3 : "))
        if choice == 1:
            print("\nyou are safe the wolf left without eating you congratulation you can now roll the dice again ")
            time.sleep(4)
            ritpath(dice())
        elif choice == 2:
            print("idiot what do you think you are a cheetah ----- the wolf chased you and ate you--")
            print("!!GAME OVER!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif choice == 3:
            print("\nyou are the king of IDIOTS ")
            time.sleep(2)
            print("\nit was an easy meal the wolf replied after eating you ")
            print("!!!GAME OVER !!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
    elif ritsum >= 6:
        print("\non moving further  you saw the same injured person whom you encounterd at the beginning with the king ")
        time.sleep(4)
        print("you were shocked on seeing them there")
        time.sleep(3)
        print("BOTH OF THEM LAUGHED AND SAID YOU PASSED THE TEST  ")
        time.sleep(3)
        print(" THIS WAS YOUR TEST OF MENTAL STRENGTH FOR BECOMING THE NEXT KING ")
        print("!!!!congratulation the game ended you won !!!")
        time.sleep(3)
        print("DO YOU WANT TO PLAY AGAIN ")
        deathwish = input("ENTER YES OR NO ")
        if deathwish == 'yes':
            _maingame()
        else:
            print("thanks for playing")
            sleep.time(100000)


def strpath(q):
    global strsum
    strsum = strsum + q
    if strsum == 1:
        print("\nno trap here you are free to move forward you may roll the dice again")
        time.sleep(3)
        strpath(dice())
    elif strsum == 2:
        print("THE GUARDIAN CHALLENGE YOU FOR A WORD GUESS GAME ")
        result = hangman()
        if result == 0:
            print("your are captured in that stage forever")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif result > 0:
            print("\nyou may roll the dice again")
            strpath(dice())
    elif strsum == 3:
        print("\nON YOU WAY FURTHER YOU ENCOUNTERED A GOBLIN ")
        time.sleep(3)
        print("\nnow you have 2 choices ")
        time.sleep(2)
        print("\nchoice 1: you saw a dark chamber nearby and sneaked in there \nchoice 2:you throw all of your gold into the nearby chamber in front of the goblin")
        time.sleep(6)
        choice = int(input("enter choice 1 or 2 "))
        if choice == 1:
            print("you went into the chamber deep and deep and found out that it is the den of goblins  ")
            time.sleep(4)
            print("a goblin ran to your side and chopped your head off")
            time.sleep(3)
            print("!!!!!its a game over for you!!!!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif choice == 2:
            print("\nwell the goblins are  creatures who  love's gold so he followed the gold pouch. \nmeanwhile you ran away from that  place  ")
            time.sleep(3)
            print("you can now roll the dice again")
            time.sleep(2)
            strpath(dice())
        else:
            print(" you panicked and could'nt decide anything the goblin killed you ")
            print("!!!!!game over!!!!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
    elif strsum == 4:
        print("\nthe guardian wants to ask an question ")
        time.sleep(2)
        print("\nI run but I cannot walk, I sometimes sing but never talk,\n I lack arms but I have hands, I lack a head but I have a face.")
        time.sleep(7)
        chances = 2
        while chances > 0:
            answ = input("enter answer : ")
            if answ == "clock" or answ == "watch":
                print("!!!!!congratulation correct answer!!!!!")
                print("you may pass from here roll the dice again ")
                break
            else:
                print("!!!!WRONG ANSWER!!!!")
                chances = chances - 1
        if chances == 0:
            print("you lost ")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        else:
            strpath(dice())
    elif strsum == 5:
        print("\nnow you have entered a forest like stage with trees and a sky ")
        time.sleep(3)
        print("\nYOU SAW A WOLF COMING YOUR WAY ")
        time.sleep(2)
        print("\nnow what will you do you have the following choices")
        time.sleep(3)
        print("choice 1: climb a nearby tree \n choice 2: run in a different direction \n choice 3: lie there and pretend to be dead")
        choice = int(input("enter your choice 1 , 2 or 3 : "))
        if choice == 1:
            print("\nyou are safe the wolf left without eating you congratulation you can now roll the dice again ")
            time.sleep(4)
            strpath(dice())
        elif choice == 2:
            print("idiot what do you think you are a cheetah ----- the wolf chased you and ate you--")
            print("!!GAME OVER!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
        elif choice == 3:
            print("\nyou are the king of IDIOTS ")
            time.sleep(2)
            print("\nit was an easy meal the wolf replied after eating you ")
            print("!!!GAME OVER !!!")
            time.sleep(3)
            print("DO YOU WANT TO PLAY AGAIN ")
            deathwish = input("ENTER YES OR NO ")
            if deathwish == 'yes':
                _maingame()
            else:
                print("thanks for playing")
                sleep.time(100000)
    elif strsum >= 6:
        print("\non moving further  you saw the same injured person whom you encounterd at the beginning with the king ")
        time.sleep(4)
        print("you were shocked on seeing them there")
        time.sleep(3)
        print("BOTH OF THEM LAUGHED AND SAID YOU PASSED THE TEST  ")
        time.sleep(3)
        print(" THIS WAS YOUR TEST OF MENTAL STRENGTH FOR BECOMING THE NEXT KING ")
        print("!!!!THE END!!!")
        time.sleep(3)
        print("DO YOU WANT TO PLAY AGAIN ")
        deathwish = input("ENTER YES OR NO ")
        if deathwish == 'yes':
            _maingame()
        else:
            print("thanks for playing")
            sleep.time(100000)
def _maingame():



    print("WELCOME TO THE ADVENTURE OF GREAT TEXT LABRYNITH  ")
    time.sleep(2)
    print("THE INTRO ")
    time.sleep(2)
    print("YOU ARE A PRINCE OF A KINGDOM YOUR FATHER HAS ASKED YOU TO EXPLORE THE GREAT LABRYNITH AT THE OUTSKIRTS ")
    time.sleep(5)
    print("\nIT WAS THE FIRST TIME YOU HEARD ABOUT THE LABRYNITH ,AND YOU EVEN DIDN'T KNEW THE PATH\nSO YOU HAD YOUR OWN DOUBTS ")
    time.sleep(6)
    print("\n SOME INFO ")
    time.sleep(1)
    print("THIS IS A GAME OF TEXT SO YOUR OPPPONENT AND YOUR CHOICES ALL WILL BE IN THE FORM OF TEXT")
    time.sleep(3)
    print("YOU WILL ENCOUNTER RIDDLE ,WORD SCRAMBLE AND SITUATION AS OPPONENTS")
    time.sleep(3)
    print("YOU WILL GET 2  CHANCES FOR A RIDDLE TO SOLVE , 10 TURNS  FOR WORDS SCRAMBLE ")
    time.sleep(3)
    print("YOU LEAVE THE KINGDOM WITH THESE ITEMS \n 1: 3 HEALING POTION ","\n2: SOME GOLD FOR THE EXPENSES")
    time.sleep(4)
    print("YOU WERE NOT GIVEN ANY WEAPON OR ARMOR OR COMPANION FOR  YOUR JOURNEY")
    time.sleep(3)
    print("YOUR LIFE IS 8 , HEALING POTION WILL RECOVER 3 LIFE AT A TIME ")
    time.sleep(3)
    print("BEFORE BEGINNING THE GAME ")
    name=input("enter your name : ")
    print("----------LETS BEGIN THE GAME",name,"----------")
    time.sleep(3)
    print("note the game is case sensitive")
    time.sleep(2)
    print("\nON YOUR WAY TO THE LABRYNITH YOU FOUND AN INJURED PERSON ON THE ROAD ")
    time.sleep(3)
    print("\nYOU HAVE 2 CHOICES PRESS \n1. FOR HELPING THROUGH HEALING POTION \n2.LEAVE HIM LIKE THAT ")
    time.sleep(1)
    a=int(input("ENTER YOUR CHOICE : "))
    if a==1:
        heal=heal-1
        print("INJURED PERSON - O-great warrier you saved this old man life ,I will never forgive this favour of  yours")
        time.sleep(3)
        print("\nI was attacked by some theifs and ended up like this.")
        time.sleep(3)
        print("\nIn return I cannot give you much , take this PHRASE it will come in handy in your journey....")
        time.sleep(3)
        print("\nThe phrase is GO NORTH TO THE NATION OF NINE STATE AND USE FIRE")
        time.sleep(3)

    print("\nNOW GOING FURTHER YOU ARRIVED AT A JUNCTION OF 4 PATH GOING IN 4 DIRECTION \ni.e NORTH,SOUTH,WEST ANF EAST \nYOU ARE ALSO REQUIRED TO SELECT THE NO OF STEPS TOO for reaching the labrynith")
    time.sleep(10)
    print("\nTHESE RIDDLES WILL HELP YOU TO GET THE ANSWER : ")
    time.sleep(3)
    print(" Riddle 1: Let's talk hypothetically.\n We change the North-East direction into the West direction such that \nall the directions change accordingly (like a wheel).")
    print("If that has been done, which direction to the South-East gets changed into? ")
    time.sleep(6)
    print("Riddle 2 : If 2 is a company and 3 a crowd what are 4 and 5? ")
    time.sleep(4)
    chances=2
    while(chances>0):
        print("for north :1 , for south : 2, for east : 3, for west: 4")

        d=int(input("enter direction : "))
        s=int(input("enter the no of steps "))
        if (d==1 and s== 9):
            print("!!!!congratulation correct answer!!!! ")
            break
        else:
            print("!!!!WRONG ANSWER!!!!")
            chances=chances-1

    if chances==0:
        print("!!!!game over!!!!")
        print("\nYOU LOST THE GAME BEFORE EVEN REACHING THE LABRYNITH ")
        time.sleep(3)
        print("DO YOU WANT TO PLAY AGAIN ")
        deathwish=input("ENTER YES OR NO ")
        if deathwish == 'yes':
            _maingame()
        else:
            print("thanks for playing")
            sleep.time(10000)
    print("Welcome to the great labrynith ")
    time.sleep(2)

    print("\nNow you can’t leave the labrynith without completing it or dying ")
    time.sleep(3)
    print("\n GATE GUARDIAN HUMAN IF YOU WANT TO ENTER THE LABRYNITH\n THEN YOU MUST ANSWER THIS QUESTION\n ELSE YOU MAY NOT ENTER ")
    time.sleep(6)
    print("\n I am always hungry and will die if not fed, the finger I lick  will soon turn red")
    chances = 3
    time.sleep(6)
    while chances > 0:
        a = input("enter the answer : ")
        if (a == 'fire'):
            print("!!!!congratulation correct answer!!!! ")
            time.sleep(3)
            print("you may enter the labrynith ")
            break
        else:
            print("!!!!WRONG ANSWER!!!!")
            chances = chances - 1

    if chances == 0:
        print("!!!!game over!!!!")
        print("\nYOU LOST THE GAME ")
        time.sleep(3)
        print("DO YOU WANT TO PLAY AGAIN ")
        deathwish = input("ENTER YES OR NO ")
        if deathwish == 'yes':
            _maingame()
        else:
            print("thanks for playing")
            sleep.time(100000)
    print("the game is a bit different from here ")
    time.sleep(3)
    print("\nyou will have to roll the dice and based on your number you will move ahead ")
    time.sleep(3)
    print("the ahead is unknown ")
    time.sleep(2)
    print(" GET READY FOR ROLLING THE DICE ")
    dicevalue = dice()
    dicesteps(dicevalue)
    print("\nNOW FROM HERE THE PATH DIVERGES INTO 3 PATH I.E LEFT ,RIGHT, AND STRAIGHT ")
    path=input("enter the path : ")
    if path == 'left':
        print("so you have chosen this path ")
        leftpath = dice()
        lefpath(leftpath)
    elif path == 'right':
        print("so you have chosen this path ")
        rightpath=dice()
        ritpath(rightpath)
    elif path == 'straight':
        print("so you don't want to diverge from your path ")
        stratpath=dice()
        strpath(stratpath)
    else:
        print("invalid choice")
        time.sleep(2)
        print("all the three paths rised and crused you ")
        print("!!!!!GAMEOVER!!!!!")
        time.sleep(3)
        print("DO YOU WANT TO PLAY AGAIN ")
        deathwish = input("ENTER YES OR NO ")
        if deathwish == 'yes':
            _maingame()
        else:
            print("thanks for playing")
            sleep.time(100000)
_maingame()
