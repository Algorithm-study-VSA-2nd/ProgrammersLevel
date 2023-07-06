numbers = [3, 30, 34, 5, 9]
numbers.sort(reverse=True)  # [34,30,9,5,3]
answer = ''
i = 0

for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        # 앞 숫자 첫번째 수가 뒷숫자 첫번째 수보다 작을 때
        if str(numbers[i])[0] < str(numbers[j])[0]:
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp
        # 첫번째 수가 동일할 때 300,30,3 / 30,3
        elif str(numbers[i])[0] == str(numbers[j])[0] :
            if str(numbers[i])[1] < str(numbers[j])[1] and len(str(numbers[j])) >= 1:
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp

                if len(str(numbers[i])) > len(str(numbers[j])):
                    tmp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = tmp

            
