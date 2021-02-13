#Welcome to Magic 8 Ball
import random
import time



def Magic8Ball():
    play_again = "yes"
    while play_again == "yes":
        print("Welcome to Magic 8 Ball!")
        question = input("Please ask the Magic 8 Ball your question: ")
        print("SHAKE")
        time.sleep(2)
        print("SHAKE")
        time.sleep(2)
        print("SHAKE")
        time.sleep(2)
        
        fortunes = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes – definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        answer = random.choice(fortunes)
        print(answer)
    
        play_again = input("Do you want to ask another question? ")
        play_again.lower()
    
Magic8Ball() 
