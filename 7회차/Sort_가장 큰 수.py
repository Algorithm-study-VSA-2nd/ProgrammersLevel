def solution(numbers):
    # numbers의 요소들을 문자형으로 변경한 뒤 리스트에 넣는다.
    numbers = list(map(str, numbers))

    # 3번 이어붙여서 그 값을 기준으로 내림차순으로 정렬한다.
    numbers.sort(key=lambda x: x*3, reverse=True)

    # '000' '00'을 피하기 위해 str->int->str
    return str(int(''.join(numbers)))


