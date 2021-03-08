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
    for k in words:
        if (k!=" "):
            newst.append(k)
        else:
            print(newst)
            newst.clear()
            continue
    prin()
    

    
if var == 2:
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
    with open ("Output.txt", "w") as file:
        new_dictionary1 = "".join(new_dictionary)
        file.write(new_dictionary1)
    print("Задание 5")
    with open ("nya.txt","r") as nya:
        nya1 = nya.read()
        print (nya1)
        print ("OK")
    with open ("helloworld.exe","w") as world:
        print("Access denied")
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
    e = []
    for l in range(0,len(d)-1):
        e.append(list(d[l].values()))
    print (e)
    
        #if p.isdigit():
            #del(p)
    while True:
        key1 = input("Введите значение ключа: ")
        if not keyfor.isalpha():
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
    count = 0
    val1 = list(slovar.values())
    for t in range(0, len(val)):
        for n in range(t+1, len(val)):
            if val1[t]==val1[n]:
                print (key[t])
                print (key[n])
    
    