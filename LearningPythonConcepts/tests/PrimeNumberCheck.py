#number = int(input("Enter a number: "))

# if number < 2:
#     print(number, "is NOT a prime number")
# else:
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(number, "is a PRIME number")
#     else:
#         print(number, "is NOT a prime number")
# def findSquar(numner):
#     square= numner*number
#     return(square)
# print(findSquar(number))

def change_number(num):
    num+=10
def change_list(num_list):
    num_list.append(20)
num_val=10
print("*********effect of pass by value*********")
print("num_val before function call:", num_val)
change_number(num_val)
print("num_val after function call:", num_val)
print("-----------------------------------------------")
val_list=[5,10,15]
print("*********effect of pass by reference*********")
print("val_list before function call:", val_list)
change_list(val_list)
print("val_list after function call:", val_list)

 