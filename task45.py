def delem(arr):
    for i in range(len(arr)-1):
        j = i + 1
        while(j < len(arr)):
            if arr[i] == arr[j]:
                print(arr[i])
                arr.pop(j)
                j -= 1
            j += 1
    return arr
a = [4,'gredf',5,5,'qw',1,2,'qw','tr',2,1]
print(delem(a))
'''
# Если в задании набор только скобок правильно расставленных например ({[({[]})]}) или ([{}[]]) работает
# Если это какой-то пример например (2-3+[5-4]*{65+45}) тоже работает, предварительно удалив не скобки
# Если же просто набор открывающих и закрывающих скобок в хаотичном порядке, без смысла, то эта не работает, но несложно написать другую,
# как предидущем дз подсчитать каждый символ(скобку) и сравнить
'''
def correct(str):
    while True:
        if str[0] == '(':
            k = ')'
        elif str[0] == '[':
            k = ']'
        elif str[0] == '{':
            k = '}'
        else: 
            return False
        #i = str.rfind(k,0,len(str))
        if len(str) !=1 and str[1] == k:
            str = str[2:len(str)]
        elif k == str[len(str)-1]:
            str = str[1:len(str)-1]
        else:
            return False
        if len(str) == 0:
            return True

#str = '([[[][]])'
#print(correct(str))

while True:
    n = input(
"""
Выберите задачу.
1. Удалить из списка элементы, значения которых уже встречались в этом же списке в предыдущих элементах.
2. Вводится текст, содержащий различные скобки, необходимо определить, все ли скобки расставлены корректно.
Выход:                                              Enter
"""
    )
    if n == "1":
        _list = [int(i) for i in input('Введите значения элементов массива через пробел ').split()]
        print(f'После удаления повторяющихся элементов получим получим: {delem(_list)}')
    elif n == "2":
        str = input('Введите строку: ')
        for i in (range(len(str))):
            if str[i]!='(' or str[i]!=')' or str[i]!='[' or str[i]!=']' or str[i]!='{' or str[i]!='}':
                str.replace(str[i],'')
        print(f'Определите, все ли скобки расставлены корректно - {correct(str)}')
    elif not n:
        print("Goodbye!")
        break
    else:
        print("Неверный символ")