
import logging 
import pandas as pd
# from konlpy.tag import Mecab
from konlpy.tag import Kkma
from emosent import *
import re
import emoji
import logging
import sys

def emoji_sentiment(text):
    return get_emoji_sentiment_rank(text)["sentiment_score"]

class Analyzer:
    def remove_unnecessary_word(text):
        text = re.sub('[/[\{\}\[\]\/?|\)*~`!\-_+<>@\#$%&\\\=\(\'\"]+', '', text)
        text = re.sub('[a-zA-Z]' , ' ', text)
        text = re.sub(' +', ' ', text)
        text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ', text) # http로 시작되는 url
        text = re.sub(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ', text) # http로 시작되지 않는 url
   
        text = text.rstrip().lstrip()
        # print("in remove_unnecessary_word", text)
        return text


    def preprocessing(text):
        # print(text)
        
        # text = re.sub('[a-zA-Z]' , ' ', text)
        # text = re.sub('[/[\{\}\[\]\/?|\)*~`!\-_+<>@\#$%&\\\=\(\'\"]+', '', text)
        
        # text = re.sub('[#]+[0-9a-zA-Z_]+', ' ', text)
        # text = text.replace('\n',' ')
        
        text = ' '.join(text.split())
        # print(text)
       
        return emoji.demojize(text)

    def get_score_from_chunks(chunks, lexicons):
        scores = {'POS': 0, 'NEG': 0, 'NEUT': 0, 'COMP': 0, 'None': 0}

        for chunk in chunks:
            # print(chunk)
            
            if chunk.startswith(":") and chunk.endswith(":"):
                try:
                    out = get_emoji_sentiment_rank(emoji.emojize(chunk))
                    
                    scores['POS'] += out["positive"] / out["occurrences"]
                    scores['NEG'] += out["negative"] / out["occurrences"]
                    scores['NEUT'] += out["neutral"] / out["occurrences"]
                    # scores['NEUT'] += out["neutral"]
                except KeyError:
                    pass 
            else:
                for index, row in lexicons.iterrows():
                    if row['ngram'] in chunk:
                        scores[row['max.value']] += row['max.prop']
            
        return Analyzer.scores_to_percentiles(scores)

    # def calc_scores(scores):
    #     return scores['POS'] / ()

    def scores_to_percentiles(scores):
        sum_of_scores = sum(scores.values())
        if sum_of_scores == 0:
            # may be error... cause can't get score from n-gram
            return {'POS': 0, 'NEG': 0, 'NEUT': 0, 'COMP': 0, 'None': 1}

        for category in scores:
            scores[category] = scores[category] / sum_of_scores

        return scores

    def analyze_sentences_into_chunks(sentences):
        m = Kkma()
        # m = Mecab()
        
        analyzed_words = []

        Analyzer.get_logger().info(f"in analyze_sentences_into_chunks {sentences}")
        # print("in analyze_sentences_into_chunks", sentences)
        for str in sentences:
            str = Analyzer.preprocessing(str)
          
            if len(str) > 2:
                analyzed_words.append(str)
                continue

            # analyzed_str = kkma.pos(str)
            analyzed_str = m.pos(str)
            tmp_arr = []

            for word in analyzed_str:
                tmp_arr.append("/".join(word))
            analyzed_words.append(";".join(tmp_arr))

        return analyzed_words
    
    def analyze_word(sentence):
        lexicon_dictionary = pd.read_csv('lexicon/polarity.csv')

        word_chunks = Analyzer.analyze_sentences_into_chunks(Analyzer.remove_unnecessary_word(sentence))
        categorized_scores = Analyzer.get_score_from_chunks(word_chunks, lexicon_dictionary)
        
        Analyzer.get_logger().info(f"sentence: {sentence}, socre: {categorized_scores}")

        # print(categorized_scores)

    # def analyze_from_array(sentences):
    #     lexicon_dictionary = pd.read_csv('lexicon/polarity.csv')

    #     for sentence in sentences:
    #         word_chunks = Analyzer.analyze_sentences_into_chunks(Analyzer.remove_unnecessary_word(sentence))
    #         categorized_scores = Analyzer.get_score_from_chunks(word_chunks, lexicon_dictionary)
    #         print(sentence)
    #         print("/")
    #         print(categorized_scores)
    #     return

    def get_logger():
        logger = logging.getLogger()
        if not logger.hasHandlers():
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter("[%(process)d/%(processName)s] %(message)s")
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
        return logger