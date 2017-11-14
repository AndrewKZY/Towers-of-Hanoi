def hanoi(n):
        n = int(input('Enter number of disks: '))
        if n <= 0:
            print('Error.')
        else:
            begin = [range(n)] #starting pole
            end = [] #end pole
            inter = [] #intermediate pole
            subsq_n = begin.pop(range(1,n)) #everything except the 1st disk
            inter = inter[subsq_n]
            base_n = begin(0)
            for base_n in begin:
                base_n = begin.pop(base_n)
                end = end[base_n]
            if (inter[subsq_n]) and (end[base_n]):
                subsq_n = inter.pop(subsq_n)
                end = end.append(subsq_n)
            return end
        print(end)

