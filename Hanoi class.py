# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:40:42 2017

@author: OndineG
"""

class Hanoi:
    def __init__(self):
        self.Hanoi = Hanoi
    
    def disc():
        n = int(input('Enter number of discs: '))
        global A
        A = [i for i in reversed(range(1, n+1))]
        print(A)
        global B
        B = []
        global C
        C = []
        return
    
    def movedisc():
        starting = input('Select post to take disc from: ')
        if starting == 'A':
            starting = A
            singledisc = starting.pop(-1)
        elif starting == 'B':
            starting = B
            singledisc = starting.pop(-1)
        elif starting == 'C':
            starting = C
            singledisc = starting.pop(-1)
        else:
            print('Select post to take disc from: ')
        destination = input('Select post to give disc too: ')
        if destination == 'A':
            destination = A
            A.append(singledisc)
            print(A)
        elif destination == 'B':
            destination = B
            B.append(singledisc)
            print(B)
        elif destination == 'C':
            destination = C
            C.append(singledisc)
            print(C)
        else:
            print('Select post to give disc too: ')
        return
    
Hanoi.disc()
Hanoi.movedisc()