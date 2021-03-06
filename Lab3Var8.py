var = input("Введите номер задания: ")
while not var.isnumeric():
    print ("Введите число")
    var = input("Введите номер задания: ")
var = int(var)
print(var)
if var == 1:
    newst = []
    words ="Наступило теплое лето. В саду поспела смородина. Даша и Таня собирают ее в ведерко. Затем девочки кладут смородину на блюдо. Мама будет варить из нее варенье. Зимой в холода дети будут пить чай с вареньем. "
    word.lower()
    point = words.find("наступило")
    for k in words:
        if (k!=" "):
            newst.append(k)
        else:
            print(newst)
            newst.clear()
            continue
    new_words = []
    new_words = words.split(" ")
    lst = []
    no_sign = [".", ",", "[", "]", ":", ";", "-" ]
    for wd in words.lower().split():
        if not wd in no_sign:
            new_words = wd
            if wd[-1] in no_sign:
                new_words = new_words[:-1]
            if wd[0] in no_sign:
                new_words = new_words[1:]
            lst.append(new_words)
    print (new_words)

    
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
        minKey = key[v.index(min(val))]
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
        print(type(slovar[k]))
    pprint(d)
    def get_min_max_keys(d:dict):
        return min(d, key = lambda k: d[k]), max(d, key = lambda k:d[k])
    #d.sort(key=lambda i: i[1])
    #for i in list_d:
        #print(i[0], ":", i[1])
    d.sort(key = lambda to_mean: d[key])
    print("Сортированный список", pprint(d))
#if var == 4:
    