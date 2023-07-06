def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 0으로만 이루어진 배열인 경우 처리
    if numbers[0] == '0':
        return '0'
    
    return ''.join(numbers)