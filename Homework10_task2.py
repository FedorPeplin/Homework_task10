import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='utf-8')

tree=ET.parse(r"C:\Users\Фёдор\Desktop\homework10\newsafr.xml", parser)

root=tree.getroot()

channel = root.find('channel')
items = channel.findall('item')

alltexts=[]
for elements in items:
    a= (elements.find('description').text)
    alltexts.append(a)
# print (alltexts) checking

alltextsunited = []
for elements in alltexts:
    a = (elements.split())
    alltextsunited.extend(a)

# print (alltextsunited) checking

allelemsmore6=[]
for elements in alltextsunited:
    if len(elements) >= 6:
        allelemsmore6.append(elements)

# print (sorted(allelemsmore6)) checking

from collections import Counter
def most_frequent():
    occurence_count = Counter(allelemsmore6).most_common(10)
    # print (occurence_count) check
    print (f'Топ 10 встречающихся слов более 6 букв и количество их упоминаний:')
    i = 0
    for elems in occurence_count:
        print((occurence_count[i][0]),'-', (occurence_count[i][1]))
        i += 1

most_frequent()
