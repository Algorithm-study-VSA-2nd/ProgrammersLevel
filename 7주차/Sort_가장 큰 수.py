"""
def radix_sort(numbers):
    max_num = max(list(map(str, numbers)), key=len)
    digit_length = len(max_num)

    for i in range(digit_length):
        digit_dict = {}
        for num in numbers:
            digit = num // (10 ** i) % 10
            if digit in digit_dict:
                digit_dict[digit].append(num)
            else:
                digit_dict[digit] = [num]
        numbers = []
        for key in range(9, -1, -1):
            if key in digit_dict:
                numbers += sorted(digit_dict[key], key=lambda x: x // (10 ** i) % 10, reverse=True)
    return numbers
"""   
#기수 정렬(O(kn)+O(nlogn))은 오히려 시간복잡도가 증가함. 내장함수 sorted()(O(nlogn))가 더 효율적.

def solution(numbers):
    sorted_nums = sorted(numbers)
    sorted_nums.sort(key=lambda x: (str(x) * 4)[:4], reverse=True)
    sorted_str = ''.join(map(str, sorted_nums))
    
    return str(int(sorted_str))
