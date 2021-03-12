with open('logs.txt', 'r', encoding='utf-8') as f:
    dict1 = {i.replace('- - ', '').split(' ')[0]: 0 for i in f}

with open('logs.txt', 'r', encoding='utf-8') as source:
    with open('sorted_logs.txt', 'w', encoding='utf-8') as f:
#----Если памяти нехватает, можем читать, и записывать по одной строке в файл
        # for line in source:
        #     f.write(f"({line.replace('- - ', '').split(' ')[0]}"
        #             f"{line.replace('- - ', '').split(' ')[3]}"
        #             f"{line.replace('- - ', '').split(' ')[4]})\n")
#------------Для получения непосредственно списка кортежей, возможна нехватка памяти
        cut_log = [(line.replace('- - ', '').split(' ')[0],
                line.replace('- - ', '').split(' ')[3],
                line.replace('- - ', '').split(' ')[4])
               for line in source]
        for line in cut_log:
            f.write(f'{line}\n')

with open('logs.txt', 'r', encoding='utf-8') as f:
    for i in f:
        if i.replace('- - ', '').split(' ')[0] in dict1:
            dict1[i.replace('- - ', '').split(' ')[0]] += 1

spammer = dict([max(dict1.items(), key=lambda key_val: key_val[1])])
print('spammer is:', *spammer.keys(), *spammer.values(), 'requests')

