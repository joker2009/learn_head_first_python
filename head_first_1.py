__author__ = 'joker_jiang'
movies = ['the Holy Grail', 1975, 'Terry Jones', 91,
            ['Graham Chapman',
            ['Michael Palin', 'John Clees', 'Terry Gilliam', 'Eeic Idle', 'Terry Jones']]]


# for each_item in movies:
#     print(each_item)

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)

# 循环迭代
