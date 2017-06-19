# -*- coding: utf-8 -*-
import string

"""
Input: string
Output: array
This funtion takes a string of text, lowercases it, gets rid of punctuation, and turns it into an array
"""
def text_clean(str):
    str = str.lower()
    str = str.translate(None, string.punctuation)
    arr = str.split()
    return arr

#2.1

'''Input: string1, string2
Output: integer
This funtion takes string1, turns it into the array in the first function,
and counts the number of times string2 shows up in string1.
'''
def word_frequency(str, word):
    arr = text_clean(str)
    return arr.count(word)


#2.2

'''Input: string
Output: array
This funtion takes a string of text, turns it into the array in the first function,
matches terms and deletes repeats to create array of unique words.  '''
def unique_words(str):
    arr = text_clean(str)
    for word in arr:
        term = arr.index(word) + 1
        for match in arr[term:]:
            if word == match:
                arr.remove(match)
    return arr
'''
Input: array
Output: integer
This funtion takes the array of unique words and calculates how many of them there are.
'''
def num_unique_words(text):
    return len(unique_words(text))

#2.3
'''
Input: string
Output: dictionary
This funtion takes a string of text, turns it into an array of unique words,
and pairs this to each of their frequencies to create a dictionary.
'''
def frequency_unique_words(str):
    arr = unique_words(str)
    array = text_clean(str)
    list_frequency = {}

    for word in arr:
        list_frequency[word] = (array.count(word))

    return list_frequency

#Total word count
def total_word_count(str):
    return len(text_clean(str))

def total_wc(str):
    dict = frequency_unique_words(str)
    count = 0
    for key in dict:
        count += dict[key]
    return count


text = """
After tech stocks were pummeled on Friday, the sector is selling off again to start the week.

Just before noon Eastern, the Nasdaq was down 0.6%, or down about 40 points. The Dow and S&P 500 had also pared some losses, with the Dow off 40 points and the S&P down about 6.

Shortly after the market open, the Nasdaq had been down more than 1.3%, or 85 points, far outpacing losses from the Dow and the benchmark S&P 500. Near 9:50 a.m. ET the Dow was off 62 points, or 0.3%, and the S&P 500 was down 9 points, or 0.4%. On Friday, the Nasdaq fell 1.8% while the Dow actually finished in the green.

Major tech names selling off early Monday included Nvidia (NVDA), down over 4%, AMD (AMD), down 5%, Microsoft (MSFT), down about 3%, and Amazon (AMZN) also off about 3%. Near noon Eastern, Nvidia shares had erased all of their early losses while AMD, Microsoft, and Amazon were still in the red.

Tech stocks in the U.S. were also taking their lead from European equities, as Europe’s tech index fell 3.5% on Monday, its biggest drop since the day after Brexit in June 2016.
"""
text = text.replace('\n', ' ').replace('\r','')

'''print "Here is the text: %s." %text
print "\n \n"
print "Here are the number of unique words: %s" %num_unique_words(text)
print "\n \n"
print "Here are each of the unique words and their frequencies: %s." %frequency_unique_words(text)'''

print total_word_count(text)
print total_wc(text)











