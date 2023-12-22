import json

text = open('data11.txt', 'r')
text2 = open('data12.txt', 'r')
data = text.read()
data2 = text2.read()

labels = json.load(open('imagenet_class_index1.json'))
new_json = {}
myList = data.split('; ')
myList2 = data2.split('; ')
print(myList)
ranger = len(labels.keys())

i=0
for i in range(ranger):
    new_json[i] = [myList2[i], myList[i]]
    print (new_json[i])
    i+=1

with open('imagenet_class_index2.json', 'w', encoding='utf-8') as file: ############смещенный датасет, починить
    json.dump(new_json, file, ensure_ascii=False)

