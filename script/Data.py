import sqlite3

class Manager:
    def get_mock_raw_data():

        raw_data = []

        # URL포함 건은 거르기로....
        content1 = "이거 결과값이 이상한데 확인해주세요..."
        
        content2 = "기아우승 확신 100% 😂"
        content3 = "부상부위도 특이하네"
        content4 = "Hello world, Greeting!! "
        content5 = "어린이날입니다 아이돌 여러분들은 이날만을 위해 묵혀둔 과거사진을 준비해주시고 소속사에서는 n년전 비하인드영상을 풀어주시기 바랍니다 아무것도없으면 정신을좀차리시길바랍니다"
        content6 = "싸늘하다. 가슴에 비수가 날아와 꽂힌다."
        content7 = "어린이날🫶🏻🍓🌱"

        raw_data.append(content1)
        raw_data.append(content2)
        raw_data.append(content3)
        raw_data.append(content4)
        raw_data.append(content5)
        # raw_data.append(content6)
        # raw_data.extend(content7)

        return raw_data
    def get_from_csv():

        raw_data = []

        return raw_data

    def create_sqlite():
        conn = sqlite3.connect("./db/data.db")

        cur = conn.cursor()

        conn.execute('CREATE TABLE data(postID TEXT, content TEXT, postedDate TEXT)')

        # cur.executemany()

        conn.commit()
        conn.close()

        return
