#Welcome to Magic 8 Ball
import random
import time
def Magic8Ball():
    print("Welcome to Magic 8 Ball!")
    input("Please ask the Magic 8 Ball your question: ")
    print("SHAKE")
    time.sleep(3)
    print ("SHAKE")
    time.sleep(3)

    fortunes = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes – definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
    random.choice(fortunes)
    print(random.choice) # print random response

    play_again = input("Do you want to ask another question? ")

    def play_again():
        if play_again == "yes":
            #run
        elif play_again == "no": # I'm getting an indent error here! 
            #quit
        else: print("Please answer yes or no.")    
