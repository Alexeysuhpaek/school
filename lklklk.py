import random
fcyif = random.randint(1,100)
# print (fcyif)
while True:
    print ("ваше предположение")
    minute = int (input())
    if  fcyif ==  minute:
        print ("Вы угадали верно!!!")
        break
    if minute>fcyif:
        print ("Попробуйте число меньше ")
    if minute<fcyif:
        print ("Попробуйте число больше ")