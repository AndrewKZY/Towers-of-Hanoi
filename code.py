def hanoi(n, begin, end, inter):
        n = int(input('Enter number of disks: '))
        begin = []
        begin.append(n)
        for n in begin: #trying to make it so 'n' enters the list 'begin' in
            if n == 1:  #decreasing intervals of 1 (ex: if n=5, begin=[5,4,3,2,1]
                break
            else:
                n -= 1
        if n < 0:
            print('Error.')
        else:
            hanoi(n - 1, begin, end, inter)
        if begin[0]:
            inter.append(begin.pop())
        hanoi(n - 1, inter, begin, end)
        print(end)
        return
