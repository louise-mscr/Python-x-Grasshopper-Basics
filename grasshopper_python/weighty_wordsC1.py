import rhinoscriptsyntax as rs

#x is in Item Access, TypeHint = str


number_words_list = []
number_letters = []

def sentence_rythm(*args):
    new_list = list(args)
    length_words=[]
    print(new_list)
    for small_list in new_list:
        print(small_list)
        words_single = small_list.split()
        number_words = len(words_single)
        number_words_list.append(number_words)
        for units in words_single:
            length_words = len(units)
            number_letters.append(length_words)

sentence_rythm(x)