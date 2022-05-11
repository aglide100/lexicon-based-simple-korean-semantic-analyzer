import pandas as pd
from konlpy.tag import Mecab
# import MeCab
# from eunjeon import Mecab
from emosent import *
import re
import os

def emoji_sentiment(text):
    
    return get_emoji_sentiment_rank(text)["sentiment_score"]

def check_emoji(str):
    # print(str)
    # emoji_pattern = re.compile("["
    #     u"\U0001F600-\U0001F64F"  # emoticons
    #     u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    #     u"\U0001F680-\U0001F6FF"  # transport & map symbols
    #     u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    #                        "]+", flags=re.UNICODE) 

    emoji_pattern = re.compile("["
        u"\U00010000-\U0010FFFF"  #BMP characters 이외
                           "]+", flags=re.UNICODE)
    emojiCheck = emoji_pattern.findall(str)

    # print(emojiCheck)
    if len(emojiCheck) >= 1:
        # print("!")
        return True
    else:
        return False

class Analyzer:
    def preprocessing(text):
        # print(text)
        text = text.rstrip().lstrip()
        return re.sub('[/[\{\}\[\]\/?|\)*~`!\-_+<>@\#$%&\\\=\(\'\"]+', '', text)

    def get_score_from_chunks(chunks, lexicons):
        scores = {'POS': 0, 'NEG': 0, 'NEUT': 0, 'COMP': 0, 'None': 0}

        for chunk in chunks:
            # print(chunk)  
            check = check_emoji(chunk)
            if check == True:
                try:
                    out = get_emoji_sentiment_rank(chunk)

                    scores['POS'] += out["positive"] / out["occurrences"]
                    scores['NEG'] += out["negative"] / out["occurrences"]
                    scores['NEUT'] += out["neutral"] / out["occurrences"]
                    # scores['NEUT'] += out["neutral"]
                except KeyError:
                    print("No sentiment data") 
            else:
                for index, row in lexicons.iterrows():
                    if row['ngram'] in chunk:
                        scores[row['max.value']] += row['max.prop']
            
        return Analyzer.scores_to_percentiles(scores)

    def calc_scores(scores):
        return scores['POS'] / ()

    def scores_to_percentiles(scores):
        sum_of_scores = sum(scores.values())
        if sum_of_scores == 0:
            # may be error... cause can't get score from n-gram
            return {'POS': 0, 'NEG': 0, 'NEUT': 0, 'COMP': 0, 'None': 1}

        for category in scores:
            scores[category] = scores[category] / sum_of_scores

        return scores

    def analyze_sentences_into_chunks(sentences):
        # kkma = Kkma()
        m = Mecab()
        
        analyzed_words = []

        for str in sentences:
            check = check_emoji(str)

            if check == True:
                analyzed_words.append(str)
                continue
            
            str = Analyzer.preprocessing(str)
            # analyzed_str = kkma.pos(str)
            analyzed_str = m.pos(str)
            tmp_arr = []

            for word in analyzed_str:
                tmp_arr.append("/".join(word))
            analyzed_words.append(";".join(tmp_arr))

        return analyzed_words
    
    def analyze_word(sentence):
        lexicon_dictionary = pd.read_csv('lexicon/polarity.csv')

        word_chunks = Analyzer.analyze_sentences_into_chunks(sentence)
        categorized_scores = Analyzer.get_score_from_chunks(word_chunks, lexicon_dictionary)
        
        print(categorized_scores)

    def analyze_from_array(sentences):
        lexicon_dictionary = pd.read_csv('lexicon/polarity.csv')

        for str in sentences:
            word_chunks = Analyzer.analyze_sentences_into_chunks(str)
            categorized_scores = Analyzer.get_score_from_chunks(word_chunks, lexicon_dictionary)
            # print(str)
            print(categorized_scores)
        return 