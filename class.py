# -*- coding: utf-8 -*-
import string

class total_word_count:

    def __init__(self, text):
        self.text = text
        self.word_array = []
        self.unique_words = []
        self.list_frequency = {}

    def text_clean(self):
        self.text = self.text.lower()
        self.text = self.text.translate(None, string.punctuation)
        self.word_array = self.text.split()

    def word_frequency(self, word):
        return self.word_array.count(word)

    # def get_unique_words(self):
    #     self.unique_words = self.word_array
    #     for word in self.word_array:
    #         index_word = self.word_array.index(word) + 1
    #         for match in self.word_array[index_word:]:
    #             if word == match:
    #                 self.unique_words.remove(match)
    #     return len(self.unique_words)

    def get_unique_words(self):
        """
        Implement get_unique_words using try
        :return: int, # of unique words
        """
        for word in self.word_array:
            try:
                self.unique_words.index(word)
            except ValueError:
                self.unique_words.append(word)
        return len(self.unique_words)

    def get_unique_words2(self):
        """
        Implement get_unique_words using set()
        :return: int, # of unique words
        """
        self.unique_words = list(set(self.word_array))
        return len(self.unique_words)

    def frequency_unique_words(self):
        for word in self.unique_words:
            self.list_frequency[word] = (self.word_array.count(word))
            print word, self.word_array.count(word)

    # Total word count
    def total_word_count(self):
        len(self.text)

    def total_wc(self):
        dict = self.frequency_unique_words()
        count = 0
        for key in dict:
            count += dict[key]

def main():

    text = """
    After tech stocks were pummeled on Friday, the sector is selling off again to start the week.

    Just before noon Eastern, the Nasdaq was down 0.6%, or down about 40 points. The Dow and S&P 500 had also pared some losses, with the Dow off 40 points and the S&P down about 6.

    Shortly after the market open, the Nasdaq had been down more than 1.3%, or 85 points, far outpacing losses from the Dow and the benchmark S&P 500. Near 9:50 a.m. ET the Dow was off 62 points, or 0.3%, and the S&P 500 was down 9 points, or 0.4%. On Friday, the Nasdaq fell 1.8% while the Dow actually finished in the green.

    Major tech names selling off early Monday included Nvidia (NVDA), down over 4%, AMD (AMD), down 5%, Microsoft (MSFT), down about 3%, and Amazon (AMZN) also off about 3%. Near noon Eastern, Nvidia shares had erased all of their early losses while AMD, Microsoft, and Amazon were still in the red.

    Tech stocks in the U.S. were also taking their lead from European equities, as Europe’s tech index fell 3.5% on Monday, its biggest drop since the day after Brexit in June 2016.
    """
    text = text.replace('\n', ' ').replace('\r', '')

    twc = total_word_count(text)
    twc.text_clean()
    print "This is the frequency of the word near: %s." % twc.word_frequency("near")
    print "This is the total number of unique words: %d." % twc.get_unique_words()
    # for x in sorted(twc.unique_words):
    #     print x
    twc.frequency_unique_words()

if __name__ == "__main__":
    main()







