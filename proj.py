import string
import numpy as np
from numpy.linalg import norm
import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import streamlit as st

from sklearn.feature_extraction.text import CountVectorizer



corpus = st.text_input("Corpus")
plagiarized_text = st.text_input("Rephrased Text")

# """
# King Krishnadevaraya loved horses and had the best collection of horse breeds in the Kingdom. 
# Well, one day, a trader came to the King and told him that he had brought with him a horse of the best breed in Arabia.
# He invited the King to inspect the horse. King Krishnadevaraya loved the horse; so the trader said that the King could buy this one 
# and that he had two more like this one, back in Arabia that he would go back to get. The King loved the horse so much that he had to have the other two as well.
# He paid the trader 5000 gold coins in advance. The trader promised that he would return within two days with the other horses.
# Two days turned into two weeks, and still, there was no sign of the trader and the two horses. One evening, to ease his mind, the King went on a stroll in his garden.
# There he spotted Tenali Raman writing down something on a piece of paper. Curious, the King asked Tenali what he was jotting down.
# Tenali Raman was hesitant, but after further questioning, he showed the King the paper. On the paper was a list of names, the King’s being at the top of the list.
# Tenali said these were the names of the biggest fools in the Vijayanagara Kingdom! As expected, the King was furious that his name was at the top and asked Tenali Raman for an explanation.
# Tenali referred to the horse story, saying the King was a fool to believe that the trader, a stranger, would return after receiving 5000 gold coins.
# Countering his argument, the King then asked, what happens if/when the trader does come back? In true Tenali humour, he replied saying, in that case, the trader would be a bigger fool, 
# and his name would replace the King’s on the list!"""


# plagiarized_text = """ With the largest collection of horse breeds in the Kingdom, King Krishnadevaraya was an avid horse lover. 
# The King was informed one day by a dealer that he had brought a horse of the finest breed in Arabia.
# He asked the King to examine the steed. The seller responded that since King Krishnadevaraya adored the horse, he may purchase it and that he would return to Arabia to obtain the other two he had. The King had to have the other two horses also because he loved the first one so much.
# He gave the merchant five thousand gold coins in advance. The trader said he would bring the other horses back in two days.
# The trader and the two horses had not shown up after two days had passed into two weeks. The King took a stroll in his garden one evening to decompress. He saw Tenali Raman there, scribbling something down on a piece of paper. The King was curious and asked Tenali what he was writing down.Tenali Raman was reluctant to show the King the paper, but he eventually did so after more probing. A list of names was written on the paper, with the King's name at the top.These are the names of the biggest idiots in the Vijayanagara Kingdom, according to Tenali! The King demanded an explanation from Tenali Raman since he was understandably incensed to see his name at the top.
# Tenali brought up the horse incident and said the King was foolish to think the stranger trader would come back with five thousand gold coins.
# The King then questioned, rebutting his argument, "What happens if/when the trader does come back?" He responded with typical Tenali sarcasm, stating that the trader would be the greater idiot in that scenario and his name would take the place of the King's on the list!
# """

#Removing punctuations
corpus = corpus.translate(corpus.maketrans('' , '', string.punctuation))

#Removing punctuations from plagiarized text
plagiarized_text = plagiarized_text.translate(plagiarized_text.maketrans('' , '', string.punctuation))


#This is one large string. First, we'll tokenize it. This will store it in a list
word_tokens = word_tokenize(corpus)


#This is one large string. First, we'll tokenize it. This will store it in a list. Plagiarism
plagiarized_text_tokens = word_tokenize(plagiarized_text)


#Stopword_removal
filtered_sentence = []
for word in word_tokens:
     if word.lower() not in  stopwords.words('english'):
         filtered_sentence.append(word)

#Repeat steps for plagiarized text
plagiarized_filtered_sentence = []
for word in plagiarized_text_tokens:
     if word.lower() not in stopwords.words('english'):
          plagiarized_filtered_sentence.append(word) 




#Stemming
ps = PorterStemmer()
def stemming(word):
     return ps.stem(word)

result = map( stemming , filtered_sentence)
result_plagiarized = map(stemming, plagiarized_filtered_sentence)

filtered_sentence = list(result)
sentence = ' '.join(filtered_sentence)

plagiarized_filtered_sentence = list(result_plagiarized)
plagiarized_sentence = ' '.join(plagiarized_filtered_sentence)
# final = ''.join(filtered_sentence)



print(sentence)

print("*******************")
print('\n')
print('\n')
print('\n')

print(plagiarized_sentence)


final_list = [sentence, plagiarized_sentence ]
print("*******************")
print('\n')
print('\n')
print('\n')
print(final_list)

vectorizer = CountVectorizer()

corpus = vectorizer.fit_transform(final_list)



bag_of_words = corpus.toarray()


print(bag_of_words)

A =  np.array(bag_of_words[0]) 
B =  np.array(bag_of_words[1])


cosine =  np.dot(A,B)/(norm(A)*norm(B))
st.write(cosine)
print("Cosine Similarity : " , cosine)


#*************************************************************************#

