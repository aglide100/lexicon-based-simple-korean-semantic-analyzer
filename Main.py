from Data import Manager
from Lexicon import Analyzer

raw_data = Manager.get_mock_raw_data()
Analyzer.analyze_from_array(raw_data)




# # print(emoji_pattern.sub(r'', '😡aaa'))
# result = emoji_pattern.findall('😡😡😡😡aaa')
# print(result)
# print(len(result))



# Manager.create_sqlite()
