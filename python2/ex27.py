from termcolor import colored
people = 20
cats = 30
dogs = 15

#An if statment is asking if this variable meets a sertian criteria then do
#a sertain thing and if it does not do something else or nothing atall
if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The worlds is saved!"
else:
    print "Okay the world realy is doomed then, hope the dogs will save us!"

if people < dogs:
    print "The world is drooled on!"
else:
    print colored('DOOMED', 'red')

if people > dogs:
    print "The world is dry:"

dogs += 5

if people >= dogs:
    print "People are greated than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

if cats > dogs:
    print "Cats are the best"

if dogs + people != cats:
    print "Cats are rubbish"
