var = input("Введите номер задания: ")
while not var.isnumeric():
    print ("Введите число")
    var = input("Введите номер задания: ")
def prin():
    print("Слово смородина встретилось в тексте 2 раза")
    print("Слово варенье встретилось в тексте 2 раза")
    print ("Остальные слова встретились в тексте один раз")
var = int(var)
print(var)
if var == 1:
    newst = []
    words ="Наступило теплое лето. В саду поспела смородина. Даша и Таня собирают ее в ведерко. Затем девочки кладут смородину на блюдо. Мама будет варить из нее варенье. Зимой в холода дети будут пить чай с вареньем. "
    z = words.split(" ")
    for io in z:
        print(io)
    prin()
    

    
if var == 2:
    import pprint
    with open ("Input.txt", "r") as f:
        st = f.readlines()
        st1 = st[0]
        st2 = st[1]
        st3 = st[2]
        print(st1, end = "")
    dictionary = {55:st1, 32:st2, 88:st3 }
    list_keys = list(dictionary.keys())
    list_keys.sort()
    list_keys.reverse()
    print (list_keys)
    new_dictionary = [dictionary.get(list_keys[0]), dictionary.get(list_keys[1]), dictionary.get(list_keys[2])]
    print (new_dictionary)
    print("Микрозадание 5")
    def vvod():
        while True:
            numb = input()
            if not numb.isnumeric():
                print("Введите значение заново")
            else:
                numb = int(numb)
                if numb<=0:
                    print("Введите положительное число")
                else:
                    return numb
                    break
    print("Введите количество файлов")              
    numb = vvod()
    files = {}
    s1 = []
    helper = []
    helper1 = {}
    for io in range(0,numb):
        print("Введите название файла и возможные действия через пробел")
        file = input()
        s1 = (file.split(" ", maxsplit = 1))
        helper1[s1[0]] = s1[1]
        helper.append(s1[1])
    s2 = []
    print ("Введите количество действий, которое хотите сделать с файлами")
    numb1 = vvod()
    count = 0
    for ii in range(0,numb1):
        print("Введите название файла и производимое действие через пробел")
        file1 = input()
        s2 = (file1.split(" ", maxsplit = 1))
        if s2[1] in (helper1[s2[0]]):
            print ("OK")
        else:
            print("Access denied")
        count+=1
    #file1 = file1[::-1]
    #file1 = file1.replace("w","", 1)
    #file1 = file1.replace("r", "", 1)
    #file1 = file1.replace("x", "", 1)
    #file1 = file1[::-1]
    #print (file1)
    #for iii in reversed(file1):
       # if (iii == w) or (iii == r) or (iii == x):

if var == 3:
    slovar = {'Буфорд':2000, 'Хум':23, 'Рабштейн': 25, 'Мелник':390, 'Калласте': 953, 'Дюрбюи': 11000, 'Иннополис':96, 'Панемуне':265, 'Чекалин':965, 'Шеффилд':551800,'Лидс':751485,'Кроли':100547, 'Сент-Хеленс': 102629, 'Олдем': 103544, 'Блэкберн':105085}
    from pprint import pprint
    import random
    spisok = ["Буфорд","Хум","Рабштейн", "Мелник", "Калласте", "Дюрбюи", "Иннополис", "Панемуне","Чекалин",  "Шеффилд", "Лидс", "Кроли", "Сент-Хеленс","Олдем","Блэкберн"]
    #slovar = dict()
    #for t in range (0, len(spisok)):
        #a = random.randint(23, 106000)
        #slovar [spisok[t]] = {a}
    pprint(slovar)
    
    key = input("Введите название города ")
    while True:
        population = input("Введите кол-во жителей ")
        if ( not population.isnumeric()):
            print ("Введите число")
        else: 
            population = int(population)
            if (population<=0):
                print("Введите натуральное число")
            else:
                key=key.title()
                break
    slovar[key] = population
    def KeyMaxValue():
        val = list(slovar.values())
        key = list(slovar.keys())
        maxkey = key[val.index(max(val))]
        maxvalue = max(val)
        print("Максимальное значение: " +  str(maxvalue) + " Ключ максимального значения " + str(maxkey))
    def KeyMinValue():
        val = list(slovar.values())
        key = list(slovar.keys())
        minKey = key[val.index(min(val))]
        minValue = min(val)
        print("Минимальное значение: " +  str(minValue) + " Ключ минимального значения " + str(minKey))
    def SrValues():
        v = list(slovar.values())
        Srvalue = sum(v)/len(v)
        print("Среднее среднее значение словаря = ", Srvalue)
    v = list(slovar.values())
    k = list(slovar.keys())
    pprint(slovar)
    KeyMaxValue()
    KeyMinValue()
    SrValues()
    while True:
        keyfor = input("Введите значение ключа: ")
        if not keyfor.isalpha():
            print ("Введите строчный ключ")
        else:
            keyfor = keyfor.title()
            if not keyfor in (slovar.keys()):
                print("Введите город из списка")
            else:
                break
    j = slovar.pop(keyfor)
    print(j)
    pprint(slovar)
    d = []
    val = list(slovar.values())
    key = list(slovar.keys())
    for k in key:
        d.append({'key': k, 'value': int(slovar[k])})
    pprint(d)
    d.sort(key = lambda to_mean: to_mean["value"])
    print("Сортированный список")
    pprint(d)
    #e = []
    #for l in range(0,len(d)-1):
        #e.append(list(d[l].values()))
    #print (e)
    
        #if p.isdigit():
            #del(p)
    while True:
        key1 = input("Введите значение ключа: ")
        if not key1.isalpha():
            print ("Введите строчный ключ")
        else:
            key1 = key1.title()
            break
    for p in d:
        if p["key"] == key1:
            while True:
                q = input("Введите новое значение ключа: ")
                if not q.isdigit():
                    print("Введите числовое значение ключа")
                else:
                     p["value"] = int(q)
                     break
    slovar[key1] = int(q)
    pprint(d)
    key2 = list(slovar.keys())
    count = list(range(0,len(slovar)))
    print("Ключи с одинаковыми значениями: ")
    val1 = list(slovar.values())
    for t in range(0, len(val)):
        for n in range(t+1, len(val)):
            if val1[t]==val1[n]:
                count[t] = 1
                count[n] = 1
    for m in range(0,len(count)):
        if (count[m]==1):
            print(str(key2[m])+ str(":") + str(val1[m]))

if var == 4:
    import json
    import pprint
    dic = {"Aircraft": [{"ID": 2281337, "Number": 256, "Model": 47,"Route": 3, "The Date TO": "23.02.2019", "Spaciousness":7000}], "Passengers": [{"SNM": "Butilkin Pavel Adapterovich","History": [{"ID":2281338,"Data poleta": "28.03.2020", "Place": "3В","Ves bagage": "500 kg"}]}]}
    dic1 = {"Aircraft": 2281337, "Number": 256, "Model": 47,"Route": 3, "The Date To": "23.02.2019", "Spaciousness":7000, "Passengers": "Butilkin Pavel Adapterovich","History":2281338,"Data Poleta": "28.03.2020", "Place": "3B","Ves Bagage": "500 kg"}
    
    json_object = json.dumps(dic, indent = 3)
    with open ("sample.json", "w") as outfile:
        outfile.write(json_object)
    with open('sample.json', 'r') as openfile: 
        json_object = json.load(openfile) 
    print(json_object)
    key3 = input("Введите значение ключа, который хотите изменить: ")
    key3 = key3.title()
    while True:
            a = input("Введите новое значение ключа: ")
            dic1[key3] = a
            break 

    json_object = json.dumps(dic1, indent = 3)
    with open ("sample.json", "w") as outfile:
        outfile.write(json_object)
    with open('sample.json', 'r') as openfile: 
        json_object = json.load(openfile) 
    print(json_object)

    key4 = input("Введите ключ, который хотите добавить: ")
    key4 = key4.title()
    val3 = input("Введите значение для введенного ключа: ")
    dic1[key4] = val3

    json_object = json.dumps(dic1, indent = 3)
    with open ("sample.json", "w") as outfile:
        outfile.write(json_object)
    with open('sample.json', 'r') as openfile: 
        json_object = json.load(openfile) 
    print(json_object)


    while True:
        key5 = input("Введите ключ, который хотите удалить: ")
        key5 = key5.title()
        if not key5 in (dic1.keys()):
            print("Введите ключ из словаря")
        else:
           del dic1[key5]
           break
    
    json_object = json.dumps(dic1, indent = 3)
    with open ("sample.json", "w") as outfile:
        outfile.write(json_object)
    with open('sample.json', 'r') as openfile: 
        json_object = json.load(openfile) 
    print(json_object)


    #Аэропорт
#{‘Самолеты’: [{‘id’: value, ‘Номер’: value, ‘Модель’:value, ‘Маршрут’: value, ‘Дата ТО’: value, ...}], ‘Пассажиры’: [{‘ФИО’: value, ‘История’:  [{‘id’ : value, ‘Дата полета’: date value, ‘Место’: value}, ...]}]}
#Структура данных пассажирова не должна содержать информации о самолетах кроме ID, при выводе истории необходимо выводить данные исходя из связки по ID.


    
    