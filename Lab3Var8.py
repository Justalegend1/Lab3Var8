from pprint import pprint
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
    words = """— Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites 1. Ну, здравствуйте, здравствуйте. Je vois que je vous fais peur 2, садитесь и рассказывайте.
Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина и приближенная императрицы Марии Феодоровны, встречая важного и чиновного князя Василия, первого приехавшего на ее вечер. Анна Павловна кашляла несколько дней, у нее был грипп, как она говорила (грипп был тогда новое слово, употреблявшееся только редкими). В записочках, разосланных утром с красным лакеем, было написано без различия во всех:
«Si vous n'avez rien de mieux à faire, Monsieur le comte (или mon prince), et si la perspective de passer la soirée chez une pauvre malade ne vous effraye pas trop, je serai charmée de vous voir chez moi entre 7 et 10 heures. Annette Scherer» 3.
— Dieu, quelle virulente sortie! 4 — отвечал, нисколько не смутясь такою встречей, вошедший князь, в придворном, шитом мундире, в чулках, башмаках и звездах, с светлым выражением плоского лица.
Он говорил на том изысканном французском языке, на котором не только говорили, но и думали наши деды, и с теми, тихими, покровительственными интонациями, которые свойственны состаревшемуся в свете и при дворе значительному человеку. Он подошел к Анне Павловне, поцеловал ее руку, подставив ей свою надушенную и сияющую лысину, и покойно уселся на диване.
— Avant tout dites-moi, comment vous allez, chère amie? 5 Успокойте меня, — сказал он, не изменяя голоса и тоном, в котором из-за приличия и участия просвечивало равнодушие и даже насмешка.
— Как можно быть здоровой... когда нравственно страдаешь? Разве можно, имея чувство, оставаться спокойною в наше время? — сказала Анна Павловна. — Вы весь вечер у меня, надеюсь?
— А праздник английского посланника? Нынче середа. Мне надо показаться там, — сказал князь. — Дочь заедет за мной и повезет меня.
— Я думала, что нынешний праздник отменен, Je vous avoue que toutes ces fêtes et tous ces feux d'artifice commencent à devenir insipides 6.
— Ежели бы знали, что вы этого хотите, праздник бы отменили, — сказал князь по привычке, как заведенные часы, говоря вещи, которым он и не хотел, чтобы верили.
— Ne me tourmentez pas. Eh bien, qu'a-t-on décidé par rapport à la dépêche de Novosilzoff? Vous savez tout 7.
— Как вам сказать? — сказал князь холодным, скучающим тоном. — Qu'a-t-on décidé? On a décidé que Buonaparte a brûlé ses vaisseaux, et je crois que nous sommes en train de brûler les nôtres 8.
Князь Василий говорил всегда лениво, как актер говорит роль старой пиесы. Анна Павловна Шерер, напротив, несмотря на свои сорок лет, была преисполнена оживления и порывов.
Быть энтузиасткой сделалось ее общественным положением, и иногда, когда ей даже того не хотелось, она, чтобы не обмануть ожиданий людей, знавших ее, делалась энтузиасткой. Сдержанная улыбка, игравшая постоянно на лице Анны Павловны, хотя и не шла к ее отжившим чертам, выражала, как у избалованных детей, постоянное сознание своего милого недостатка, от которого она не хочет, не может и не находит нужным исправляться.
В середине разговора про политические действия Анна Павловна разгорячилась.
— Ах, не говорите мне про Австрию! Я ничего не понимаю, может быть, но Австрия никогда не хотела и не хочет войны. Она предает нас. Россия одна должна быть спасительницей Европы. Наш благодетель знает свое высокое призвание и будет верен ему. Вот одно, во что я верю. Нашему доброму и чудному государю предстоит величайшая роль в мире, и он так добродетелен и хорош, что Бог не оставит его, и он исполнит свое призвание задавить гидру революции, которая теперь еще ужаснее в лице этого убийцы и злодея. Мы одни должны искупить кровь праведника. На кого нам надеяться, я вас спрашиваю?.. Англия с своим коммерческим духом не поймет и не может понять всю высоту души императора Александра. Она отказалась очистить Мальту. Она хочет видеть, ищет заднюю мысль наших действий. Что они сказали Новосильцеву? Ничего. Они не поняли, они не могли понять самоотвержения нашего императора, который ничего не хочет для себя и все хочет для блага мира. И что они обещали? Ничего. И что обещали, и того не будет! Пруссия уже объявила, что Бонапарте непобедим и что вся Европа ничего не может против него... И я не верю ни в одном слове ни Гарденбергу, ни Гаугвицу. Cette fameuse neutralité prussienne, ce n'est qu'un piège 9. Я верю в одного Бога и в высокую судьбу нашего милого императора. Он спасет Европу!.. — Она вдруг остановилась с улыбкой насмешки над своею горячностью.
— Я думаю, — сказал князь, улыбаясь, — что, ежели бы вас послали вместо нашего милого Винценгероде, вы бы взяли приступом согласие прусского короля. Вы так красноречивы. Вы дадите мне чаю?
— Сейчас. A propos, — прибавила она, опять успокоиваясь, — нынче у меня два очень интересные человека, le vicomte de Mortemart, il est allié aux Montmorency par les Rohans 10, одна из лучших фамилий Франции. Это один из хороших эмигрантов, из настоящих. И потом l'abbé Morio; 11 вы знаете этот глубокий ум? Он был принят государем. Вы знаете?
— А! Я очень рад буду, — сказал князь. — Скажите, — прибавил он, как будто только что вспомнив что-то и особенно-небрежно, тогда как то, о чем он спрашивал, было главной целью его посещения, — правда, что l'impératrice-mère 12 желает назначения барона Функе первым секретарем в Вену? C'est un pauvre sire, ce baron, à ce qu'il paraît 13. — Князь Василий желал определить сына на это место, которое через императрицу Марию Феодоровну старались доставить барону.
Анна Павловна почти закрыла глаза в знак того, что ни она, ни кто другой не могут судить про то, что угодно или нравится императрице.
— Monsieur le baron de Funke a été recommandé à l'impératrice-mère par sa soeur 14, — только сказала она грустным, сухим тоном. В то время как Анна Павловна назвала императрицу, лицо ее вдруг представило глубокое и искреннее выражение преданности и уважения, соединенное с грустью, что с ней бывало каждый раз, когда она в разговоре упоминала о своей высокой покровительнице. Она сказала, что ее величество изволила оказать барону Функе beaucoup d'estime 15, и опять взгляд ее подернулся грустью.
Князь равнодушно замолк, Анна Павловна, с свойственною ей придворною и женскою ловкостью и быстротою такта, захотела и щелкануть князя за то, что он дерзнул так отозваться о лице, рекомендованном императрице, и в то же время утешить его.
— Mais à propos de votre famille, — сказала она, — знаете ли, что ваша дочь, с тех пор как выезжает, fait les délices de tout le monde. On la trouve belle comme le jour 16.
Князь наклонился в знак уважения и признательности.
— Я часто думаю, — продолжала Анна Павловна после минутного молчания, придвигаясь к князю и ласково улыбаясь ему, как будто выказывая этим, что политические и светские разговоры кончены и теперь начинается задушевный, — я часто думаю, как иногда несправедливо распределяется счастие жизни. За что вам дала судьба таких двух славных детей (исключая Анатоля, вашего меньшого, я его не люблю, — вставила она безапелляционно, приподняв брови), — таких прелестных детей? А вы, право, менее всех цените их и потому их не сто́ите.
И она улыбнулась своею восторженной улыбкой.
— Que voulez-vous? Lafater aurait dit que je n'ai pas la bosse de la paternité 17, — сказал князь.
— Перестаньте шутить. Я хотела серьезно поговорить с вами. Знаете, я недовольна вашим меньшим сыном. Между нами будь сказано (лицо ее приняло грустное выражение), о нем говорили у ее величества и жалеют вас...
Князь не отвечал, но она молча, значительно глядя на него, ждала ответа. Князь Василий поморщился.
— Что ж мне делать? — сказал он наконец. — Вы знаете, я сделал для их воспитания все, что может отец, и оба вышли des imbéciles 18. Ипполит, по крайней мере, покойный дурак, а Анатоль — беспокойный. Вот одно различие, — сказал он, улыбаясь более неестественно и одушевленно, чем обыкновенно, и при этом особенно резко выказывая в сложившихся около его рта морщинах что-то неожиданно-грубое и неприятное.
— И зачем родятся дети у таких людей, как вы? Ежели бы вы не были отец, я бы ни в чем не могла упрекнуть вас, — сказала Анна Павловна, задумчиво поднимая глаза.
— Je suis votre верный раб, et à vous seule je puis l'avouer. Мои дети — ce sont les entraves de mon existence 19. Это мой крест. Я так себе объясняю. Que voulez-vous?.. 20 — Он помолчал, выражая жестом свою покорность жестокой судьбе.
Анна Павловна задумалась.
— Вы никогда не думали о том, чтобы женить вашего блудного сына Анатоля. Говорят, — сказала она, — что старые девицы ont la manie des mariages 21. Я еще не чувствую за собою этой слабости, но у меня есть одна petite personne, которая очень несчастлива с отцом, une parente à nous, une princesse 22 Болконская. — Князь Василий не отвечал, хотя с свойственной светским людям быстротой соображения и памятью движением головы показал, что он принял к соображению это сведенье.
— Нет, вы знаете ли, что этот Анатоль мне стоит сорок тысяч в год, — сказал он, видимо не в силах удерживать печальный ход своих мыслей. Он помолчал.
— Что будет через пять лет, ежели это пойдет так? Voilà l'avantage d'être père 23. Она богата, ваша княжна?
— Отец очень богат и скуп. Он живет в деревне. Знаете, этот известный князь Болконский, отставленный еще при покойном императоре и прозванный прусским королем. Он очень умный человек, но со странностями и тяжелый. La pauvre petite est malheureuse comme les pierres 24. У нее брат, вот что недавно женился на Lise Мейнен, адъютант Кутузова. Он будет нынче у меня.
— Ecoutez, chère Annette 25, — сказал князь, взяв вдруг свою собеседницу за руку и пригибая ее почему-то книзу. — Arrangez-moi cette affaire et je suis votre вернейший раб à tout jamais (рап — comme mon староста m'écrit des 26 донесенья: покой-ер-п). Она хорошей фамилии и богата. Все, что мне нужно.
И он с теми свободными и фамильярными грациозными движениями, которые его отличали, взял за руку фрейлину, поцеловал ее и, поцеловав, помахал фрейлинскою рукой, развалившись на креслах и глядя в сторону.
— Attendez 27, — сказала Анна Павловна, соображая. — Я нынче же поговорю Lise (la femme du jeune Болконский) 28. И, может быть, это уладится. Ce sera dans votre famille que je ferai mon apprentissage de vieille fille 29."""
    words = words.replace('.', "").replace('!', "").replace('?', "").replace(',', "").replace(':', "")\
        .replace(';', "").replace('(', "").replace(')', "").replace('"', "").replace("—", "").lower().split()
    pprint(dict((x, words.count(x)) for x in set(words)))
    
    
    

    
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
    for t in range(0, len(val)):
        count[t] = 0
    val1 = list(slovar.values())
    for t in range(0, len(val)):
        for n in range(t+1, len(val)):
            if val1[t]==val1[n]:
                count[t] = 1
                count[n] = 1
    sum1 = 0
    for op in count:
        sum1 = sum1+op
    if (sum1!=1) and (sum1!= 0):
        for m in range(0,len(count)):
            if (count[m]==1):
                print(str(key2[m])+ str(":") + str(val1[m]))
    elif(sum1 == 0) or (sum1 == 1):
        print("Нет ключей с одинаковыми значениями")
if var == 4:
    #import json
    #json_object = json.dumps(dic, indent = 3)
    #with open ("sample.json", "w") as outfile:
        #outfile.write(json_object)
    #with open('sample.json', 'r') as openfile: 
        #json_object = json.load(openfile) 
    #print(json_object)
    #это просто схема работы с json файлом
    dic = {"Aircraft": [{"ID": 2281337, "Number": 256, "Model": 47,"Route": 3, "The Date TO": "23.02.2019", "Spaciousness":7000}], "Passengers": [{"SNM": "Butilkin Pavel Adapterovich","History": [{"ID":2281338,"Data poleta": "28.03.2020", "Place": "3В","Ves bagage": "500 kg"}]}]}
    print("Исходный словарь")
    from pprint import pprint
    pprint(dic)
    while True:
        task = input("Что хотите сделать?\n1-Добавление элемента\n2-Удаление элемента\n3-Изменение данных\n4-Вывести данные по параметру\n")
        if not task.isnumeric():
            print("Введите цифру")
        else:
            task = int(task)
            if (task < 1) or (task>4):
                print("Выберите действие от 1 до 4")
            else:
                task = int(task)
                break
    if (task == 1):
        while True:
            keys2 = input("Введите категорию, в которую хотите добавить элемент\n1-Aircraft\n2-Passengers\n")
            if not key2.isnumeric():
                print("Введите цифру")
            else:
                if (keys2 < 1) or (key2>2):
                    print("Выберите действие от 1 до 2")
                else:
                    keys2 = int(keys2)
                    break
        if (keys2 == 1):
            keys2 = "Aircraft" 
            print("Введите категорию, которую хотите добавить: ")
            kategory = input()
            kategory = kategory.title()
            value3 = input("Введите значение: ")
            if value3.isalpha():
                value3= value3.title()
            elif(value3.isnumeric()):
                value3 = int(value3)
            dic[keys2][0][kategory] = value3
            print(dic)
        elif (keys2 == 2):
            keys2 = "Passengers"
            print("Введите категорию, которую хотите добавить: ")
            kategory = input()
            kategory = kategory.title()
            value3 = input("Введите значение: ")
            if value3.isalpha():
                value3= value3.title()
            elif(value3.isnumeric()):
                value3 = int(value3)
            dic[keys2][0][kategory] = value3
            print(dic)
    if (task == 2):
        while True:
            keys2 = input("Введите категорию, в которой хотите провести удаление\n1-Aircraft\n2-Passengers\n")
            if not keys2.isnumeric():
                print("Введите цифру")
            else:
                keys2 = int(keys2)
                if (keys2 < 1) or (keys2>2):
                    print("Выберите категорию от 1 до 2")
                else:
                    keys2 = int(keys2)
                    break
        if (keys2 == 1):
            while True:
                elem = input("1 - удалить всю категорию\n2 - удалить элемент внутри категории\n")
                if not elem.isnumeric():
                    print("Введите цифру")
                else:
                    elem = int(elem)
                    if (elem < 1) or (elem>2):
                        print("Выберите действие от 1 до 2")
                    else:
                        elem = int(elem)
                        break
            keys2 = "Aircraft" 
            if (elem == 1):
                del dic[keys2]
                print (dic)
            elif(elem == 2):
                while True:
                    elem1 = input("Выберите элемент, который хотите удалить:\n1 - ID\n2 - Number\n3 - Model\n4 - Route\n5 - The Date TO\n6 - Spaciousness\n")
                    if not elem1.isnumeric():
                        print("Введите число")
                    else:
                        elem1 = int(elem1)
                        if (elem1<1) or (elem1>6):
                            print("Введите цифру от 1 до 6")
                        else:
                            elem1 = int(elem1)
                            break
                if (elem1==1):
                    elem1 = "ID"
                    del dic[keys2][0][elem1]
                    print(dic)
                elif (elem1 == 2):
                    elem1 = "Number"
                    del dic[keys2][0][elem1]
                    print(dic)           
                elif(elem1 == 3):
                    elem1 = "Model"
                    del dic[keys2][0][elem1]
                    print(dic)
                elif(elem1 == 4):
                    elem1 = "Route"
                    del dic[keys2][0][elem1]
                    print(dic)
                elif(elem1 == 5):
                    elem1 = "The Date TO"
                    del dic[keys2][0][elem1]
                    print(dic)
                elif(elem1 ==6):
                    elem1 = "Spaciousness"
                    del dic[keys2][0][elem1]
                    print(dic)
        if (keys2 == 2):
            while True:
                elem = input("1 - удалить всю категорию\n2 - удалить элемент внутри категории\n")
                if not elem.isnumeric():
                    print("Введите цифру")
                else:
                    elem = int(elem)
                    if (elem < 1) or (elem>2):
                        print("Выберите действие от 1 до 2")
                    else:
                        elem = int(elem)
                        break
            keys2 = "Passengers"
            if (elem == 1):
                del dic[keys2]
                print (dic)
            elif(elem == 2):
                while True:
                    elem1 = input("Выберите элемент, который хотите удалить:\n1 - SNM\n2 - History\n")
                    if not elem1.isnumeric():
                        print("Введите число")
                    else:
                        elem1 = int(elem1)
                        if (elem1<1) or (elem1>2):
                            print("Введите цифру от 1 до 2")
                        else:
                            elem1 = int(elem1)
                            break
                if (elem1==1):
                    elem1 = "SNM"
                    del dic[keys2][0][elem1]
                    print(dic)
                elif (elem1 == 2):
                    elem1 = "History"
                    print("Данная категория содержит подкатегории, что вы хотите сделать:\n1 - удалить всю категорию\n2 - удалить элемент внутри категории")
                    while True:
                        elem2 = input()
                        if not elem2.isnumeric():
                            print("Введите число")
                        else:
                            elem2 = int(elem2)
                            if (elem2<1) or (elem2>2):
                                print("Введите цифру от 1 до 2")
                            else:
                                elem2 = int(elem2)
                                break
                    if (elem2 == 1):
                        del dic[keys2][0][elem1]
                        print(dic)
                    elif(elem2 == 2):
                        print("Выберите элемент, который хотите удалить\n1 - ID\n2 - Data poleta\n3 - Place\n4 - Ves bagage")
                        while True:
                            elem3 = input()
                            if not elem3.isnumeric():
                                print("Введите число")
                            else:
                                elem3 = int(elem3)
                                if (elem3<1) or (elem3>4):
                                    print("Введите цифру от 1 до 4")
                                else:
                                    elem3 = int(elem3)
                                    break
                        if (elem3==1):
                            elem3 = "ID"
                            del dic[keys2][0][elem1][0][elem3]
                            print(dic)
                        elif (elem3 == 2):
                            elem3 = "Data poleta"
                            del dic[keys2][0][elem1][0][elem3]
                            print(dic)           
                        elif(elem3==3):
                            elem3 = "Place"
                            del dic[keys2][0][elem1][0][elem3]
                            print(dic)
                        elif(elem3 == 4):
                            elem3 = "Ves bagage"
                            del dic[keys2][0][elem1][0][elem3]
                            print(dic)
    if (task == 4):
        counter = -1
        while (counter!=0):
            while True:
                keys2 = input("Введите категорию, в которой хотите осуществить вывод\n1-Aircraft\n2-Passengers\n")
                if not keys2.isnumeric():
                    print("Введите цифру")
                else:
                    keys2 = int(keys2)
                    if (keys2 < 1) or (keys2>2):
                        print("Выберите категорию от 1 до 2")
                    else:
                        keys2 = int(keys2)
                        break
            if (keys2 == 1):
                keys2 = "Aircraft" 
                while True:
                    elem = input("1 - вывести всю категорию\n2 - вывести элемент внутри категории\n")
                    if not elem.isnumeric():
                        print("Введите цифру")
                    else:
                        elem = int(elem)
                        if (elem < 1) or (elem>2):
                            print("Выберите действие от 1 до 2")
                        else:
                            elem = int(elem)
                            break 
                if (elem == 1):
                    print(dic[keys2])
                    while True:
                            counter = input("Введите\n1 - продолжить\n2 - остановить программу\n")
                            if not counter.isnumeric():
                                print("Введите цифру")
                            else:
                                counter = int(counter)
                                if counter<1 or counter >2:
                                    print("Введите 1 или 2")
                                elif (counter==2):
                                    counter = 0
                                    break
                                elif (counter == 1):
                                    break              
                elif(elem == 2):
                    while True:
                        elem1 = input("Выберите элемент, который хотите вывести:\n1 - ID\n2 - Number\n3 - Model\n4 - Route\n5 - The Date TO\n6 - Spaciousness\n")
                        if not elem1.isnumeric():
                            print("Введите число")
                        else:
                            elem1 = int(elem1)
                            if (elem1<1) or (elem1>6):
                                print("Введите цифру от 1 до 6")
                            else:
                                elem1 = int(elem1)
                                break
                    if (elem1==1):
                        elem1 = "ID"
                        print( dic[keys2][0][elem1])
                    elif (elem1 == 2):
                        elem1 = "Number"
                        print( dic[keys2][0][elem1])
                               
                    elif(elem1 == 3):
                        elem1 = "Model"
                        print( dic[keys2][0][elem1])
                    
                    elif(elem1 == 4):
                        elem1 = "Route"
                        print( dic[keys2][0][elem1])
                    
                    elif(elem1 == 5):
                        elem1 = "The Date TO"
                        print( dic[keys2][0][elem1])
                   
                    elif(elem1 ==6):
                        elem1 = "Spaciousness"
                        print( dic[keys2][0][elem1])
            if (keys2 == 2):
               while True:
                elem = input("1 - вывести всю категорию\n2 - вывести элемент внутри категории\n")
                if not elem.isnumeric():
                    print("Введите цифру")
                else:
                    elem = int(elem)
                    if (elem < 1) or (elem>2):
                        print("Выберите действие от 1 до 2")
                    else:
                        elem = int(elem)
                        break
               keys2 = "Passengers"
               if (elem == 1):
                   print( dic[keys2])
                   while True:
                            counter = input("Введите\n1 - продолжить\n2 - остановить программу\n")
                            if not counter.isnumeric():
                                print("Введите цифру")
                            else:
                                counter = int(counter)
                                if counter<1 or counter >2:
                                    print("Введите 1 или 2")
                                elif (counter==2):
                                    counter = 0
                                    break
                                elif (counter == 1):
                                    break              
               elif(elem == 2):
                   while True:
                       elem1 = input("Выберите элемент, который хотите вывести:\n1 - SNM\n2 - History\n")
                       if not elem1.isnumeric():
                           print("Введите число")
                       else:
                           elem1 = int(elem1)
                           if (elem1<1) or (elem1>2):
                               print("Введите цифру от 1 до 2")
                           else:
                               elem1 = int(elem1)
                               break
                   if (elem1==1):
                       elem1 = "SNM"
                       print(dic[keys2][0][elem1])
                   elif (elem1 == 2):
                       elem1 = "History"
                       print("Данная категория содержит подкатегории, что вы хотите сделать:\n1 - вывести всю категорию\n2 - вывести элемент внутри категории")
                       while True:
                           elem2 = input()
                           if not elem2.isnumeric():
                               print("Введите число")
                           else:
                               elem2 = int(elem2)
                               if (elem2<1) or (elem2>2):
                                   print("Введите цифру от 1 до 2")
                               else:
                                   elem2 = int(elem2)
                                   break
                       if (elem2 == 1):
                           print( dic[keys2][0][elem1])
                       elif(elem2 == 2):
                           print("Выберите элемент, который хотите удалить\n1 - ID\n2 - Data poleta\n3 - Place\n4 - Ves bagage")
                           while True:
                               elem3 = input()
                               if not elem3.isnumeric():
                                   print("Введите число")
                               else:
                                   elem3 = int(elem3)
                                   if (elem3<1) or (elem3>4):
                                       print("Введите цифру от 1 до 4")
                                   else:
                                       elem3 = int(elem3)
                                       break
                           if (elem3==1):
                               elem3 = "ID"
                               print( dic[keys2][0][elem1][0][elem3])         
                           elif (elem3 == 2):
                               elem3 = "Data poleta"
                               print( dic[keys2][0][elem1][0][elem3])      
                           elif(elem3==3):
                               elem3 = "Place"
                               print( dic[keys2][0][elem1][0][elem3])
                           elif(elem3 == 4):
                               elem3 = "Ves bagage"
                               print( dic[keys2][0][elem1][0][elem3])
                            
                   while True:
                            counter = input("Введите\n1 - продолжить\n2 - остановить программу\n")
                            if not counter.isnumeric():
                                print("Введите цифру")
                            else:
                                counter = int(counter)
                                if counter<1 or counter >2:
                                    print("Введите 1 или 2")
                                elif (counter==2):
                                    counter = 0
                                    break
                                elif (counter == 1):
                                    break               
              
    #Аэропорт
#{‘Самолеты’: [{‘id’: value, ‘Номер’: value, ‘Модель’:value, ‘Маршрут’: value, ‘Дата ТО’: value, ...}], ‘Пассажиры’: [{‘ФИО’: value, ‘История’:  [{‘id’ : value, ‘Дата полета’: date value, ‘Место’: value}, ...]}]}
#Структура данных пассажирова не должна содержать информации о самолетах кроме ID, при выводе истории необходимо выводить данные исходя из связки по ID.


    
    