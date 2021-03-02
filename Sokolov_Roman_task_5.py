from sys import argv
from Utils import currency_rates

n, s_1 = argv
s_1 = str(s_1)

result = (currency_rates(s_1))
result1 = result[0]
result2 = str(result[1])
print(result1, result2)



