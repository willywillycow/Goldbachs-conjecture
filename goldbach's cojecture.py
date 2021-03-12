primelist = []
passed = []
primetag = 2
taged = 4

def isprime(number):
    isprime = None
    if not number == 2:
        for chosed in range(2,number):
            if number % chosed == 0:
                isprime = False
                break
            elif chosed == number-1:
                isprime = True
    elif number == 2:
        isprime = True
    return isprime

def detect(number):
    if isprime(number):
        primelist.append(number)

def check(number):
    accord = None
    success = None
    kill = None
    result_1 = None
    result_2 = None
    for chose_1 in primelist:
        for chose_2 in primelist:
            if not chose_1 >= number:
                if not chose_2 >= number:
                    kill = False
                    if chose_1 + chose_2 == taged:
                        print("\033[1;36m$!------------------------------!$")
                        print("tagging:" + " " + str(taged))
                        print("prime 1:" + " " + str(chose_1))
                        print("prime 2:" + " " + str(chose_2))
                        print("$!------------------------------!$ \033[m")
                        print("\n")
                        accord = True
                    else:
                        print("\033[m------------------------------")
                        print("tagging:" + " " + str(taged))
                        print("prime 1:" + " " + str(chose_1))
                        print("prime 2:" + " " + str(chose_2))
                        print("------------------------------\033[m")
                        print("\n")
                else:
                    kill = True
            else:
                result_1 = chose_1
                result_2 = chose_2
                success = True
            if accord or success or kill:
                break
        if accord or success:
            break
    if accord:
        pass
    elif success:
        print("\033[1;32m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!------------------------------!")
        print("tagging:" + " " + str(taged))
        print("!------------------------------!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[m")
        print("\n")
        passed.append(taged)

while True:
    detect(primetag)
    check(taged)
    primetag += 1
    taged += 2
    print("-\033[1;32m!--------------------------!-")
    print("passed: " + str(passed))
    print("-!--------------------------!-\033[m")
