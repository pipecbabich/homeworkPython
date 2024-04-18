my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def rev(my_list):
    if my_list == []:
        return print('Конец списка')
    print(my_list[0])
    my_list.pop(0)

    rev(my_list)
    
rev(my_list)
