#coding:utf-8
__author__ = 'marvin'

with open("../../gold.csv") as f:
    with open("../../amount.txt",'w') as wt:
        for x in f.readlines():
            x = x.split(" ")
            wt.write('%s\n'%x[1].split('"')[1])

