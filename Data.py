import sqlite3

class Manager:
    def get_mock_raw_data():

        raw_data = []

        # ! 분석 불가 문장
        content = "하하 호호"
        content2 = "문장이 아니면 문제가 생기는듯"
        content3 = "집에 가고 싶다"
        content4 = "답이 없네"
         
        # raw_data.append(title)
        raw_data.append(content)
        raw_data.append(content2)
        raw_data.append(content3)
        raw_data.append(content4)
        
        # raw_data.extend(comments)

        return raw_data
    def get_from_csv():

        raw_data = []

        return raw_data

    def create_sqlite():
        conn = sqlite3.connect("./db/data.db")

        cur = conn.cursor()

        # cur.executemany()

        conn.commit()
        conn.close()

        return