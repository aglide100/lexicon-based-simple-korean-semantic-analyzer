import logging 
import pandas as pd
# from konlpy.tag import Mecab
from konlpy.tag import Kkma
from emosent import *
import re
import emoji
import logging
import sys
from iteration_utilities import deepflatten
from hanspell import spell_checker
#from pykospacing import Spacing
# import twitter_korean
import time
#from numba import jit

def emoji_sentiment(text):
    return get_emoji_sentiment_rank(text)["sentiment_score"]

#@jit(cache=True)
def calc_score(textPosed, dictionary, scores):
    temp = ""
    #result
    for idx, chunk in enumerate(textPosed):
        if chunk.startswith(":") and chunk.endswith(":"):
              try:
                  out = get_emoji_sentiment_rank(emoji.emojize(chunk))
                  scores['POS'] += out["positive"] / out["occurrences"]
                  scores['NEG'] += out["negative"] / out["occurrences"]
                  scores['NEUT'] += out["neutral"] / out["occurrences"]
              except KeyError:
                  pass
        else:
            result = ""

            if temp == "":
                result = dictionary.loc[(dictionary['ngram'] == chunk+";")]

                if result.empty:
                    # ECS 등 체크
                    result = dictionary.loc[(dictionary['ngram'] == chunk[:-1]+";")]

                if result.empty:
                    # ; 체크
                    result = dictionary.loc[(dictionary['ngram'] == chunk)]

                if result.empty:
                    pass
                    #print("맞는 값이 없음....")
                else:
                    temp = temp + chunk
                
            else:
                check = temp + ";" + chunk

                result = dictionary.loc[(dictionary['ngram'] == check+";")]

                if result.empty:
                    #print("check!!!", check[:-2]+";")
                    result = dictionary.loc[(dictionary['ngram'] == check[:-1]+";")]
                
                if result.empty:
                    # ; 체크
                    result = dictionary.loc[(dictionary['ngram'] == check)]

                if result.empty:
                    #print("이전 값 추가")
                    result = dictionary.loc[(dictionary['ngram'] == temp + ";")]
                    temp = ""
            
            if result.empty:
                pass
            else:
                scores[result.iloc[0]['max.value']] += result.iloc[0]['max.prop']

    return scores

class Analyzer:
    def remove_unnecessary_word(text):
        text = re.sub('[/[\{\}\[\]\/?|\)*~`!\-_+<>@\#$%&\\\=\(\'\"]+', '', str(text))
        text = re.sub('[a-zA-Z]' , ' ', str(text))
        text = re.sub(' +', ' ', str(text))
        text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ', str(text)) # http로 시작되는 url
        text = re.sub(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ', str(text)) # http로 시작되지 않는 url
        
        text = text.rstrip().lstrip()
        
        #spacing = Spacing()
        #text = spacing(text) 
        #Analyzer.get_logger().info(f"after text: " + text)

        text.replace(" " , "")

        spelled_sent = spell_checker.check(text)
        hanspell_sent = spelled_sent.checked
        text = hanspell_sent
        
        return text

    def preprocessing(text):
        # text = ' '.join(text.split())
        # text = re.sub('[#]+[0-9a-zA-Z_]+', ' ', text)
        # text = text.replace('\n',' ')
        # return text
        only_BMP_pattern = re.compile("[" + u"\U00010000-\U0010FFFF" + "]+", flags=re.UNICODE)
        onlyKorean = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+') 
        BMP_list = only_BMP_pattern.findall(text)
        
        only_BMP_list= list(deepflatten(BMP_list))
        # for value in BMP_list:
        #     print("######", value)
        #     print("___", list(value))
        #     only_BMP_list.append(list(value))

        return onlyKorean.sub('', text), only_BMP_list

    
    #@jit
    def get_score_from_chunks(chunks, lexicons):
        scores = {'POS': 0, 'NEG': 0, 'NEUT': 0, 'COMP': 0, 'None': 0}
        scores = calc_score(chunks, lexicons, scores)

        return Analyzer.scores_to_percentiles(scores)

    def scores_to_percentiles(scores):
        sum_of_scores = sum(scores.values())
        if sum_of_scores == 0:
            # may be error... cause can't get score from n-gram
            return {'POS': 0, 'NEG': 0, 'NEUT': 0, 'COMP': 0, 'None': 1}

        for category in scores:
            scores[category] = scores[category] / sum_of_scores

        return scores

    def analyze_sentences_into_chunks(sentences, m):
        #m = Kkma()
        #o = Okt()
        # m = Mecab()
        
        analyzed_words = []
        preprocessed, only_BMP_pattern = Analyzer.preprocessing(sentences)
        if len(preprocessed) == 0:
            pass
        else:
            result = m.pos(preprocessed)
            for value in result:
                analyzed_words.append(value[0]+"/"+value[1])

            for i in range(len(only_BMP_pattern)):
                analyzed_words.append(emoji.demojize(only_BMP_pattern[i]))
            

        return analyzed_words
    
    def analyze_word(row, dictionary):
        m = Kkma()
        start = time.time()

        word_chunks = Analyzer.analyze_sentences_into_chunks(Analyzer.remove_unnecessary_word(row), m)
        
        categorized_scores = Analyzer.get_score_from_chunks(word_chunks, dictionary)
        
        Analyzer.get_logger().info(f"-------------------------------------------------\nsentence: {row}\n\nsocre: {categorized_scores}")
       
        Analyzer.get_logger().info(f"점수 계산 시간 {time.time() - start}")
        result = pd.DataFrame({'text': row, 'pos': categorized_scores['POS'], 'neg': categorized_scores['NEG'], 'neut': categorized_scores['NEUT'], 'comp': categorized_scores['COMP'], 'none': categorized_scores['None'], 'max': max(categorized_scores, key=categorized_scores.get)}, index=['text'])
        return result

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
