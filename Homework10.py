import json
from pprint import pprint

with open (r"C:\Users\Фёдор\Desktop\homework10\newsafr.json", 'r', encoding='utf-8') as f:
    json_data=json.load(f)

    a = (json_data['rss']['channel']['items'])

    alltexts=[]
    for elements in a:
        a=(elements['description'].split())
        alltexts.extend(a)

    # print (alltexts[0]) checking

    elementsmore6symbols=[]
    for elements in alltexts:
        if len(elements) >= 6:
            elementsmore6symbols.append(elements.capitalize())

    # print (sorted(elementsmore6symbols)) checking

    from collections import Counter
    def most_frequent():
        occurence_count = Counter(elementsmore6symbols).most_common(10)
        print (f'Топ 10 встречающихся слов более 6 букв и количество их упоминаний:')
        i = 0
        for elems in occurence_count:
            print((occurence_count[i][0]),'-', (occurence_count[i][1]))
            i += 1

most_frequent()