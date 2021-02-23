lis = ['в', '5', 'часов', '17', 'минут', 'температура',
       'воздуха', 'была', '+5', 'градусов']


for i, val in enumerate(lis):
    if val.isdigit():
        lis[i] = f'"{val}"'
    if val.startswith('+' or '-') and len(val) != 2:
        lis[i] = f'"{val}"'
    if val.startswith('+' or '-') and len(val) == 2:
        lis[i] = f'"{val[0]}0{val[-1]}"'
    if val.isdigit() and len(val) == 1:
        lis[i] = f'"0{val}"'

result = ' '.join(lis)
print(result)
