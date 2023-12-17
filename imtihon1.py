list = [1, 3, 4, 5, 6, 7, 8, 9, 10]
num = []

def tushib_qoldirilgan_son(list, num):
    for x in range(1, 10 + 1):
        if x not in list:
            num.append(x)
            print(x)
tushib_qoldirilgan_son(list, num)