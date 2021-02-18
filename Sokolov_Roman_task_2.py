numbers = list(range(1, 1000, 2))

for i in range(len(numbers)):
    numbers[i] **= 3

result_1 = 0

for i in range(len(numbers)):
    num = numbers[i]
    digit_sum = 0
    while num != 0:
        digit_sum += num % 10
        num //= 10
    if digit_sum % 7 == 0:
        result_1 += numbers[i]

print(result_1)

result_2 = 0

for i in range(len(numbers)):
    numbers[i] += 17
    num = numbers[i]
    digit_sum = 0
    while num != 0:
        digit_sum += num % 10
        num //= 10
    if digit_sum % 7 == 0:
        result_2 += numbers[i]

print(result_2)
