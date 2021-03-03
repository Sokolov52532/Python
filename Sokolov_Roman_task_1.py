def odd_nums(max):
    for num in range(1, max + 1, 2):
        yield num

odd_to_15 = odd_nums(15)
print(*odd_to_15)
