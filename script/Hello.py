from operator import contains
from konlpy.tag import Kkma
import pandas as pd

dictionary = pd.read_csv('lexicon/polarity.csv')

k = Kkma()

#text = "메시지는 차치하고 감각적으로(시각, 청각) 황홀했다. 영화는 가능하고, 소설은 불가능한 것. 영화는 도달할 수 있고, 소설은 도달할 수 없는 것. 영화는 체험시킬 수 있고, 소설은 체험시킬 수 없는 것. 더 확장하면..."
text ="개봉일을 기다려, 모처럼 팔순의 친정어머니와 롯데 시네마에서 보았어요. 잔잔한 시냇물이 흐르는 계곡에 미나리 밭을 일구는 우리들의 어머니 또는 할머니의 강인한 생존력이란! 대지의 후손들이라면 누구나 배꼽 아래 단전으..."

#print(dictionary.index[dictionary(['ngram'] == '가/JKC')])
scores = {'POS': 0, 'NEG': 0, 'NEUT': 0, 'COMP': 0, 'None': 0}

textPos = k.pos(text)
print(textPos)
temp = ""
for chunk in textPos:
    print("---------------")    

    check = temp + chunk[0]+'/'+chunk[1]
    result = dictionary.loc[(dictionary['ngram'] == check)]
    print("첫번쨰", result)
    if result.empty and temp != "":
        
        temp = ""
        result = dictionary.loc[(dictionary['ngram'] == check)]
        print("두번째", result)
        # 꼬꼬마에서 EFN, EFQ등 긍정, 부정 어미등으로 더 추가가 되 있는 경우가 있음.
        if result.empty:
            print("seach contained", check[:-1])
            result = dictionary.loc[(dictionary['ngram'] == check[:-1])]
            print("세번째", result)
    elif result.empty and temp == "":
        print("seach contained", check[:-1])
        result = dictionary.loc[(dictionary['ngram'] == check[:-1])]
        print("네번째",result)
    else:
        temp = temp + check + ";"
    
    print(result)

    if result.empty:
        pass
    else:
        scores[result.iloc[0]['max.value']] += result.iloc[0]['max.prop']
    

    #scores[result['max.value'].values] += result['max.prop']
    #print(check)
    
    
#
    #if (dictionary['ngram'] == check).all():
    #    test = dictionary.loc[(dictionary['ngram'] == chunk[0]+'/'+chunk[1])]
    #    scores[test['max.value']] += test['max.prop']
   

    

#test = dictionary.loc[(dictionary['ngram'] == '남편/NNG;은/JX')]
#print("!!", test['max.value'].values)
#scores[test['max.value']] += test['max.prop']

print(scores)
#print (dictionary.loc[(dictionary['ngram'] == '가/JKC')])