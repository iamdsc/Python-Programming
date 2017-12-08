#Author:
#Dilpreet Singh Chawla
#Indian Institute of Information Technology Kalyani


#Using Natural Language Toolkit (nltk) in python

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter

#Reading text from file

fr=open('sample.txt','r')
s=fr.read()
fr.close()
s1=s.lower()            #converting everything to lowercase


#Removing symbols

for symbol in ['.' , ',' , '-' , '"' , '(' , ')' , '/' , '!', ':' , ';','?',]:
    s1=s1.replace(symbol,' ')    


#Removing stopwords (eg: 'is', 'am', 'the')

stop_words=set(stopwords.words('english'))
word_tokens=word_tokenize(s1)
filtered_sentence =[w for w in word_tokens if not w in stop_words]
#print(filtered_sentence)


#Stemming the words (eg: changing 'running' to 'run')

stemmer=PorterStemmer()
stemmed_sentence = [stemmer.stem(w) for w in filtered_sentence]
#print(stemmed_sentence)


#counting frequency of each word
counts=dict(Counter(filtered_sentence))
#print(counts)


#Checking the type of document - Sports or Political 

try:
    if counts['sports']==max(counts.values()):
        print("Sports Document")
        fw=open("Sports.txt","w")
        fw.write(s)
        fw.close()
        
except KeyError:
    print("No Sports Document")


try:    
    if counts['politics']==max(counts.values()):
        print("Political Document")
        fw=open("Politics.txt","w")
        fw.write(s)
        fw.close()
        
except KeyError:
    print("No Political Document")    
   

