
def solution(phone_book):
    # key값의 길이 순으로 정렬
    phone_book.sort(key=len)
    hash_table = {}
    # 기준이 될 접두사
    pref = len(phone_book[0])

    for number in phone_book:               # hash_table 만들기
        # ex) h_t={'hashing1':'119','h2':'1195~~', etc}
        hash_table[hash(number)] = number
        for i in range(pref, len(number)):
            # if문 안에 number가 slicing 된 게 pref랑 같으면 hash 값이 존재.(=True)  -> return False
            try:
                if hash_table[hash(number[0:i])]:
                    return False
            except KeyError:  # hash_table에 인덱스가 없는 경우에 KeyError 발생하기 때문에 넘겨줘야함.
                pass
    return True
