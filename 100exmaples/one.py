#!/usr/bin/python
# -*- coding=utf-8 -*-
# 列表转换为字典

#list define
lista = ['A',"B"]
#tuple define
tuplea = [1,2]

def  listconverttuple(a,b):
    c = dict([a,b])
    return  c

if __name__ == '__main__':
    result =listconverttuple(lista,tuplea)
    print result