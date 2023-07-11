# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aOZAqRrN_i_MnrHTXlhLsHzsKh1NsTGd
"""

import nltk
nltk.re_show(r'[a-zA-Z]+', 'Artificial Intelligence (AI) is a branch of Computer Science concerned with making computers behave like humans. The term was coined in 1956 by John McCarthy at the Massachusetts Institute of Technology. Artificial intelligence aims to understand the nature of intelligence and to engineer systems that exhibit such intelligence by utilizing vision, language, and knowledge. The resultant knowledge has diverse applications particularly for designing and developing humanoid robots.The objective of the AI lab is to identify and develop technologies to enable computers to learn, think, see, and understand the scenes like humans, communicate with human beings, and self-monitor/protect their systems. More specifically, we focus on:Machine Learning Computer VisionNatural Language Processing Computer Security and Malware Detection')

nltk.re_show(r'[A-Z][a-z]*', 'Artificial Intelligence (AI) is a branch of Computer Science concerned with making computers behave like humans. The term was coined in 1956 by John McCarthy at the Massachusetts Institute of Technology. Artificial intelligence aims to understand the nature of intelligence and to engineer systems that exhibit such intelligence by utilizing vision, language, and knowledge. The resultant knowledge has diverse applications particularly for designing and developing humanoid robots.The objective of the AI lab is to identify and develop technologies to enable computers to learn, think, see, and understand the scenes like humans, communicate with human beings, and self-monitor/protect their systems. More specifically, we focus on:Machine Learning Computer VisionNatural Language Processing Computer Security and Malware Detection')

nltk.re_show(r'p[aeiou]{,2}t', 'Artificial Intelligence (AI) is a branch of Computer Science concerned with making computers behave like humans. The term was coined in 1956 by John McCarthy at the Massachusetts Institute of Technology. Artificial intelligence aims to understand the nature of intelligence and to engineer systems that exhibit such intelligence by utilizing vision, language, and knowledge. The resultant knowledge has diverse applications particularly for designing and developing humanoid robots.The objective of the AI lab is to identify and develop technologies to enable computers to learn, think, see, and understand the scenes like humans, communicate with human beings, and self-monitor/protect their systems. More specifically, we focus on:Machine Learning Computer VisionNatural Language Processing Computer Security and Malware Detection')

nltk.re_show(r'\d+(\.\d+)?', 'Artificial Intelligence (AI) is a branch of Computer Science concerned with making computers behave like humans. The term was coined in 1956 by John McCarthy at the Massachusetts Institute of Technology. Artificial intelligence aims to understand the nature of intelligence and to engineer systems that exhibit such intelligence by utilizing vision, language, and knowledge. The resultant knowledge has diverse applications particularly for designing and developing humanoid robots.The objective of the AI lab is to identify and develop technologies to enable computers to learn, think, see, and understand the scenes like humans, communicate with human beings, and self-monitor/protect their systems. More specifically, we focus on:Machine Learning Computer VisionNatural Language Processing Computer Security and Malware Detection')

nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', 'Artificial Intelligence (AI) is a branch of Computer Science concerned with making computers behave like humans. The term was coined in 1956 by John McCarthy at the Massachusetts Institute of Technology. Artificial intelligence aims to understand the nature of intelligence and to engineer systems that exhibit such intelligence by utilizing vision, language, and knowledge. The resultant knowledge has diverse applications particularly for designing and developing humanoid robots.The objective of the AI lab is to identify and develop technologies to enable computers to learn, think, see, and understand the scenes like humans, communicate with human beings, and self-monitor/protect their systems. More specifically, we focus on:Machine Learning Computer VisionNatural Language Processing Computer Security and Malware Detection')

# library for fethching a URL
from urllib import request
from bs4 import BeautifulSoup

def utility(url):
	link = url
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html).get_text()
	print(raw)
utility('http://nltk.org')

#14
words = ['Soheila', 'Nastaran', 'IASBS', 'music','best']
sorted(words)

output=words.sort()
print(output)

import nltk
nltk.download('words')

#21
import nltk
import re
import pprint
import random
from urllib import request
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
def unknown(url):
    html = request.urlopen(url).read().decode('utf8')
    lowers = re.findall(r'\b[a-z]+', html)
    unknowns = [w for w in lowers if w not in nltk.corpus.words.words()]
    return unknowns
unknown('https://en.wikipedia.org')

import nltk
nltk.download('re')

#39

import nltk
import re
import pprint
import random
from urllib import request
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.corpus import wordnet as wn


def soundex(word):
    word = word.upper()         # convert the word to upper case for convenience
    
    # Step 1
    sound = word[0]

    # Step 2
    word = re.sub(r'([BFPV])[BFPV]', r'\1', word)             
    word = re.sub(r'([CGJKQSXZ])[CGJKQSXZ]', r'\1', word)
    word = re.sub(r'([DT])[DT]', r'\1', word)
    word = re.sub(r'LL', r'L', word)
    word = re.sub(r'([MN])[MN]', r'\1', word)
    word = re.sub(r'RR', r'R', word)
    
    # Step 3
    word = re.sub(r'([BFPV])([HW])[BFPV]', r'\1\2', word)
    word = re.sub(r'([CGJKQSXZ])([HW])[CGJKQSXZ]', r'\1\2', word)
    word = re.sub(r'([DT])([HW])[DT]', r'\1\2', word)
    word = re.sub(r'L([HW])L', r'L\1', word)
    word = re.sub(r'([MN])([HW])[MN]', r'\1\2', word)
    word = re.sub(r'R([HW])R', r'R\1', word)
    
    # Replace consonants with digits as follows (after the first letter)
    word = re.sub(r'[AEIOUYHW]', r'', word)
    word = re.sub(r'[BFPV]', '1', word)
    word = re.sub(r'[CGJKQSXZ]', '2', word)
    word =5 re.sub(r'[DT]', '3', word)
    word = re.sub(r'L', '4', word)
    word = re.sub(r'[MN]', '5', word)
    word = re.sub(r'R', '6', word)

    #Step 4
    
    if sound in 'AEIOUYHW':
        sound = (sound + word + '000')[:4]
    else:
        sound = (sound + word[1:] + '000')[:4]
    return sound

soundex('Soheila')