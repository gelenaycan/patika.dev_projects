"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

"""


def flatten_list(lst):
    flatten_lst = []
    for i in lst:
        if type(i) == list:
            flatten_lst.extend(flatten_list(i))
        else:
            flatten_lst.append(i)
    return flatten_lst

example_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_list(example_list))

def reverse_list(lst):
    if type(lst) == list:
        return list(map(reverse_list, reversed(lst)))
    else:
        return lst

example_list = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse_list(example_list))

