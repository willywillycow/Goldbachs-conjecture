primelist = []
taged = 3

def isprime(number):
    isprime = None
    for chosed in range(2,number):
        if number % chosed == 0:
            isprime = False
            break
        elif chosed == number-1:
            isprime = True
    return isprime

def detect(number):
    if isprime(number):
        primelist.append(number)

def check(number):
    success = None
    for chose_1 in primelist:
        for chose_2 in primelist:
            if chose_1 + chose_2 == taged:
                print("\033[1,32,39m !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("------------------------------")
                print("tagging:" + " " + str(taged))
                print("prime 1:" + " " + str(chose_1))
                print("prime 2:" + " " + str(chose_2))
                print("------------------------------")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033")
                print("\n")
                success = True
    if success == True:
        pass
    else:
        print("\033 ------------------------------")
        print("tagging:" + " " + str(taged))
        print("prime 1:" + " " + str(chose_1))
        print("prime 2:" + " " + str(chose_2))
        print("------------------------------ \033")
        print("\n")

while True:
    detect(taged)
    print("prime list: " + str(primelist))
    print("\n")
    check(taged)
    taged += 2
    
