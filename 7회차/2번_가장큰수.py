def solution(numbers):
    answer = ''
    # 리스트 내부 원소 문자열로 바꿈
    n = list(map(str, numbers))
    
    # 문자열에서의 숫자는 앞자리수의 대소로 비교가 된다. 문자열*3 : ex) 1 -> 111 이다.
    # lambda는 x*3을 대신 넣겠다는 이야기 이며 key에 할당하였으므로 정렬할때 문자열*3 위주로 정렬하겠다는 의미
    # 내림차순이어야 하므로 reverse = True
    new_numbers = sorted(n, key=lambda x:x*3, reverse=True)
    #print(new_numbers)
    # 예외가 발생하였는데 '00' or '000'일 경우.
    if new_numbers[0] == '0':
        answer = "0"
    else:
        # 문자열로 병합
        answer = "".join(new_numbers)
    return answer
