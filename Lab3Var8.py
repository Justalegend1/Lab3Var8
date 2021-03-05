var = input("Введите номер задания: ")
while not var.isnumeric():
    print ("Введите число")
    var = input("Введите номер задания: ")
var = int(var)
print(var)
if var == 1:
    newst = []
    words = "Наступило теплое лето. В саду поспела смородина. Даша и Таня собирают ее в ведерко. Затем девочки кладут смородину на блюдо. Мама будет варить из нее варенье. Зимой в холода дети будут пить чай с вареньем. "
    for k in words:
        if (k!=" "):
            newst.append(k)
        else:
            print(newst)
            newst.clear()
            continue
    #import collections
    #c = collections.Counter()
    #for word in newst:
        #c[word]+=1
    #print(c)
    #print((set(words.replace('.', "").replace('!', "").replace('?', "").replace(',', "").replace(':', "")
    #.replace(';', "").replace('(', "").replace(')', "").replace('"', "").lower().split())))
    counter = {}
    for i in range(int(input())):
        line = input().split()
        for word in line:
            counter[word] = counter.get(word, 0) + 1
         
    max_count = max(counter.values())
    most_frequent = [k for k, v in counter.items() if v == max_count]
    print(min(most_frequent))
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
    #note = {"Буфорд":2000, "Хум":23, "Рабштейн": 25, "Мелник":390, "Калласте": 953, "Дюрбюи": 11000, "Иннополис":96, "Панемуне":265, "Чекалин":965, "Шеффилд":551800,"Лидс":751485,"Кроли":100547, "Сент-Хеленс": 102629, "Олдем": 103544, "Блэкберн":105085}
    print ("Выберите метод")
    var1 = input()
    
    while not var1.isnumeric():
        print ("Введите число")
        var = input("Введите номер метода от 1 до 4: ")
    var1 = int(var1)
    if var1 == 1:
        from pprint import pprint
        import random
        spisok = ["Буфорд","Хум","Рабштейн", "Мелник", "Калласте", "Дюрбюи", "Иннополис", "Панемуне","Чекалин",  "Шеффилд", "Лидс", "Кроли", "Сент-Хеленс","Олдем","Блэкберн"]
        slovar = dict()
        for t in range (0, len(spisok)):
            a = random.randint(23, 106000)
            slovar [t] = {spisok[t]:a}
        pprint(slovar)
    elif var1==2:
        for k in range(0,2):
            key = input("Введите название города ")
            population = input("Введите кол-во жителей ")
            while not population.isnumeric():
                population = input("Введите целое число: ")
            population = int(population)
            if (population<=0):
                while (population<=0):
                    print("Мне кажется, ты что-то перепутал, нужно ввести положительное число")
                    population = input()
            population = int(population)
            slovar1 = dict()
            slovar1 [k] = {key:population}
            print(k)
        from pprint import pprint
        pprint(slovar1)
    