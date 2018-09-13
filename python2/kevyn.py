from sys import exit
from termcolor import colored

def welcome_mesage():
    print "Welcome to this script."
    print "In this script we are going to play a litle game."
    print "This game is going to test kevyns coding skills."

def decision():
    print "You have just finishd school and you are about to enter the house."
    print "But you hear mum screaming and shouting."
    print "Do you 1 enter the house? or 2 walk away and come back later"

    kian = raw_input("> ")

    if kian == "1":
        print "as you walk in the door mum shouts asking did you take the vodka from the shed again"
        print "Do you #1 lie and say no"
        print "Or\nDo you #2 Tell the truth and accept your fait?"

        decision = raw_input("> ")

        if decision == "1":
            print "Mum knows you are lying straigh away and kicks you out the house for lying!!"
        elif decision == "2":
            print colored('Mum is very angry and kicks you out the house', 'red')
        else:
            print "you are stupid and did not answer the script correct"

    elif kian == "2":
        print "Mum sees you and comes to the door and shouts on you"
        print "Do you 1 run down the street and hope she doesnt catch you"
        print "Or do you 2 turn back around and ask her what is wrong?"

        decision2 = raw_input("> ")

        if decision2 == "1":
            print "Mum cathes up with you because you are slow and hits you with the empty bottle of vodka that you stole from the shed"
        elif decision2 == "2":
            print "You walk up to the door and mum flings an empty bottle of vodka that you stole from the shed"

    else:
        print "Your answer is not on the list STUPID! kevyn is going to come and hit you for not answering his script correctly"

    print "You are now trying to appoliges to mum becasue you have no where to go"
    print "She says that she will let you back into the house if you #1 clean her shoes or #2 clean the whole hosue?"

def appolige():
    print "You are now trying to appoliges to mum becasue you have no where to go"
    print "She says that she will let you back into the house if you 1 clean her shoes or 2 clean the whole hosue?"

    decision3 = raw_input("> ")

    if decision3 == "1":
        print "Kevyn comes along and laughs at you while you have to clean all the shoes"
        print colored('Kevyn has had enough he is going to bed', 'blue')
    elif decision3 == "2":
        print "You get lazy whilst cleaning the whole house and stop and get a smack on the head"
        print colored('Kevyn has had enough he is going to bed', 'blue')
    else:
        print "You are a fucking idiot"

decision()

appolige()
