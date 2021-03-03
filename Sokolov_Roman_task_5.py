#----------------------"В лоб"-----------------------
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for number in src:
    if src.count(number) == 1:
        result.append(number)
print(result)

#--------------------Оптимизированно--------------------------
sor_src = [number for number in src if src.count(number) == 1]
print(sor_src)
