# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:40:42 2017

@author: OndineG
"""

class Hanoi:
    def __init__(self): #Initializes class.
        self.Hanoi = Hanoi
    
    def disc(): #Creates initial posts A, B, and C, and a copy of A. Puts n number of discs on post A.
        n = int(input('Enter number of discs: ')) #User enters number of discs.
        global A
        A = [i for i in reversed(range(1, n+1))] #Discs are added to post A in reverse decending order from n.
        global init_A
        init_A = list(A) #Creates a copy of post A.
        print(A)
        global B #Post B.
        B = []
        global C #Post C.
        C = []
        return
    
    def movedisc(): #Moves last disc on post A, B, or C to one of the other two posts.
        starting = input('Select post to take disc from: ') #User chooses where to remove disc from.
        if starting == 'A':
            starting = A
            singledisc = starting.pop(-1) #Removes last disc from post A.
        elif starting == 'B':
            starting = B
            singledisc = starting.pop(-1) #Removes last disc from post B.
        elif starting == 'C':
            starting = C
            singledisc = starting.pop(-1) #Removes last disc from post C.
        else:
            print('Select post to take disc from: ')
        destination = input('Select post to give disc too: ') #User chooses where to add above disc too.
        if destination == 'A':
            destination = A
            A.append(singledisc) #Adds above disc to the end of post A.
            print(A)
        elif destination == 'B':
            destination = B
            B.append(singledisc) #Adds above disc to the end of post B.
            print(B)
        elif destination == 'C':
            destination = C
            C.append(singledisc) #Adds above disc to the end of post C.
            print(C)
        else:
            print('Select post to give disc too: ')
        if C == init_A:
            print('You win!') #Prints the message when post C is the same as post A at the start.
            return
#To help the user get started, both functions are already called once.    
Hanoi.disc()
Hanoi.movedisc()
