def hanoi(n, begin, end, inter):
        n = int(input('Enter number of disks: '))
        begin = []
        begin.append(n)
        for n in begin:
            if n == 1:
                break
            else:
                begin.append(n)
                n -= 1
        if n < 0:
            print('Error.')
        else:
            hanoi(n - 1, begin, end, inter)
        if begin[0]:
            inter.append(begin.pop())
        hanoi(n - 1, inter, begin, end)
        return end
