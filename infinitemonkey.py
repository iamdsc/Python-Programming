#Author:
#Dilpreet Singh Chawla
#Indian Institute of Information Technology Kalyani.

#Infinite Monkey Theorem

import random

#Random String Generator  
def generate(length):
    new_string = ""
    template = "qwertyuiopasdfghjklzxcvbnm "
    
    for i in range(length):
        n=random.randrange(27)
        new_string += template[n]

    return new_string

#Scoring each trial
def scoring(new_string,original,length):
    score=0
    
    for i in range(length): #Comparing the two strings
        if new_string[i]==original[i]:
            score += 1

    return score

#Repetitively calling
def repeated_call(original,trials):
    length=len(original)
    maxscore=0
    
    for i in range(trials):
        new_string=generate(length)
        score=scoring(new_string,original,length)
        if  score > maxscore:
            maxscore=score
            closest=new_string
            
    print("Closest sentence in",trials,"tries is :",closest," Maximum Score :",maxscore,"out of",length)    


#Taking input from user
original=input("Enter a sentence: ")
trials=int(input("Enter number of tries: "))          
repeated_call(original,trials)

