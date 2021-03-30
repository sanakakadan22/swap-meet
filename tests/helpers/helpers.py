class Helpers:

    @staticmethod
    def strip_words_from_string(words_list, string):
        for word in words_list:
            string = string.replace(word, "")
        return string