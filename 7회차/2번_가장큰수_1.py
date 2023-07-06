from functools import cmp_to_key
#compare 함수 생성
def compare(x, y):
    if x+y > y+x:
    	return -1
    elif x+y == y+x:
    	return 0
    else:
    	return 1

def solution(numbers):
    answer = ''
    # 리스트 내부 원소 문자열로 바꿈
    n = list(map(str, numbers))
   
    # cmp_to_key 이용
    new_numbers = sorted(n, key=cmp_to_key(compare))
    # 예외가 발생하였는데 '00' or '000'일 경우.
    if new_numbers[0] == '0':
        answer = "0"
    else:
        # 문자열로 병합
        answer = "".join(new_numbers)
    return answer
