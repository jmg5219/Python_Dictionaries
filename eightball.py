import random 

eightball_choices = {
    "destiny1": "It is certain",
    "destiny2": "It is decidedly so",
    "destiny3": "Without a doubt",
    "destiny4": "Yes - definitely",
    "destiny5": "You may rely on it",
    "destiny6": "As I see it, yes",
    "destiny7": "Most likely",
    "destiny8": "Outlook good",
    "destiny9": "Yes",
    "destiny10": "Signs point to yes",
    "destiny11": "Reply hazy, try again",
    "destiny12": "Ask again later",
    "destiny13": "Better not tell you now",
    "destiny14": "Cannot predict now",
    "destiny15": "Concentrate and ask again",
    "destiny16": "Don't count on it",
    "destiny17": "My reply is no",
    "destiny18": "My sources say no",
    "destiny19": "Outlook not so good",
    "destiny20": "Very doubtful"
}

eightball_questions = {
    "question1":"Are you meeting your goals?",
    "question2":"Are your habits healthy?",
    "question3":"Are you making changes?",
    "question4" : "Am I going to get a job/internship?",
    "question5" : "Do you need my help?"
}
ask_eightball = "Y" 
while ask_eightball == "Y":
    ask_eightball = input("Do you want to ask the Magic Eightball a question (Y or N):").upper()
    if ask_eightball == "Y":
        print()
        #This is another way to get the random value from dictionary
        print(random.choice(list(eightball_questions.values())))
        print(random.choice(list(eightball_choices.values())))
        print()
    elif ask_eightball != "Y":
        print("Thanks")
