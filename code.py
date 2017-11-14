def hanoi(n, begin, end, intermidiate):
        n = int(input('Enter number of disks: '))
        begin = [range(n)]
        end = []
        intermidiate = []
        if n <= 0:
            print('Error.')
        else:
            subsq_n = begin.pop(1:)
            intermediate = intermidiate.append(subsq_n)
            base_n = begin(0)
            for base_n in begin:
                base_n = begin.pop(base_n)
                end = [base_n]
            if (intermediate = intermidiate.append(subsq_n)) and (end = begin.pop(base_n)):
                subsq_n = intermediate.pop(subsq_n)
                end = end.append(subsq_n)
            return
print(end)
