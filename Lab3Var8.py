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


    