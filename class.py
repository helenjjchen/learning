import string

class total_word_count:

    text = "hello my name is helen."

    def __init__(self, text):
        self.text = text

    def text_clean(self):
        self.text.lower()
        self.text.translate(None, string.punctuation)
        self.text.split()

    def word_frequency(self, word):
        self.text.count(word)

    def unique_words(self):
        uniquewords = self.text
        for word in self.text:
            term = self.text.index(word) + 1
            for match in self.text[term:]:
                if word == match:
                    uniquewords.remove(match)
                num_uniquewords = len(uniquewords)

    def frequency_unique_words(self):
        list_frequency = {}
        for word in unique_words(self):
            list_frequency[word] = (self.text.count(word))

#Total word count
    def total_word_count(self):
        len(self.text)

    def total_wc(self):
        dict = frequency_unique_words(self)
        count = 0
        for key in dict:
            count += dict[key]








