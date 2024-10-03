def PigeoholePrinciple(oddNumber: int):
    stringOf1s = 1 ## (10^1 -1)/9 where k = 1
    k = 2

    while stringOf1s % oddNumber != 0:
        stringOf1s = ((10**k) - 1) // 9
        k += 1
    return int(stringOf1s)

print(PigeoholePrinciple(7), 'has length ', len(str(PigeoholePrinciple(7))))
print(PigeoholePrinciple(9), 'has length ', len(str(PigeoholePrinciple(9))))
print(PigeoholePrinciple(1729), 'has length ', len(str(PigeoholePrinciple(1729))))