#创建三个字典，将这三个字典存储在一个名为people的列表中，并打印出来
alien_0 = {'color':'green0','points':5}
alien_1 = {'color':'green1','points':15}
alien_2 = {'color':'green2','points':25}

peoples = [alien_0,alien_1,alien_2]
for people in peoples:
    print(people)


#创建多个字典，对每个字典都用一个宠物名命名，答案同上

#遍历这个字典，并将每个人以及喜欢的地方打印出来
favorite_places = {
    'cuihua':['sushi','Grilled fish store','Stone bowl fish'],
    'zhaoqing':['Stone bowl fish','crab'],
    'pangzi':['Hot pepper','Carbon roast shrimp'],
}
for name,places in favorite_places.items():
    print('\n'+name.title())
    for place in places:
        print('\t'+place.title())


#字典储存字典-城市
cities = {
    'guangzhou':{
        '所属国家':'中国',
        '人口':'10w',
        '描述':'什么都吃的（除了辣椒）城市',
    },
    'chengdu':{
        '所属国家':'中国',
        '人口':'12w',
        '描述':'吃麻辣的城市',
    },
    'changsha':{
        '所属国家':'中国',
        '人口':'5w',
        '描述':'吃辣椒城市',
    }
}
for cities_name,cities_info in cities.items():
    print("\n"+cities_name)
    full_country = cities_info['所属国家']
    full_population = cities_info['人口']
    full_fact = cities_info['描述']
    print('\tFull_country:'+full_country)
    print('\tFull_population:' + full_population)
    print('\tFull_fact:' + full_fact)