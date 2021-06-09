passed = []
primetag = 2
taged = 4
current = 2

def isprime(number):
    isprime = None
    if number != 2:
        for chosed in range(2,number):
            if number % chosed == 0:
                isprime = False
                break
            elif chosed == number - 1:
                isprime = True
    elif number == 2:
        isprime = True
    return isprime

def check(number):
    accord = None
    for chose_1 in range(2,number):
        if isprime(chose_1):
            for chose_2 in range(2,number):
                if isprime(chose_2):
                    if chose_1 + chose_2 > number:
                        break
                    if chose_1 + chose_2 == taged:
                        print("\033[1;36m$!------------------------------!$")
                        print("tagging:" + " " + str(taged))
                        print("prime 1:" + " " + str(chose_1))
                        print("prime 2:" + " " + str(chose_2))
                        print("$!------------------------------!$ \033[m")
                        print("\n")
                        accord = True
                        break
                    elif chose_1 + chose_2 != taged:
                        print("\033[m------------------------------")
                        print("tagging:" + " " + str(taged))
                        print("prime 1:" + " " + str(chose_1))
                        print("prime 2:" + " " + str(chose_2))
                        print("------------------------------\033[m")
                        print("\n")
        if accord:
            break
    if accord == None:
        print("\033[1;32m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!------------------------------!")
        print("tagging:" + " " + str(taged))
        print("!------------------------------!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[m")
        print("\n")
        passed.append(taged)

while True:
    check(taged)
    primetag += 1
    taged += 2
    print("\033[1;32m%!%-----------------------%!%")
    print("passed: " + str(passed))
    print("%!%------------------------%!%\033[m")
