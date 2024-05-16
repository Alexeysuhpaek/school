# numbers = list(range(20))
# gteaater_five = []
# for i in numbers:
#     if i > 5:
#         gteaater_five.append(i)
# print(gteaater_five)
 
# numbers= int(input())
# secret=[]
# for i in range(1,numbers + 1):
#     if numbers % i == 0:
#         secret.append(i)
# print(secret) 


def is_div(x, y, z):
    if x % y == 0 and x % z == 0:
        return True
    else:
        return False
print(is_div(x=4,y=2,z=1))
