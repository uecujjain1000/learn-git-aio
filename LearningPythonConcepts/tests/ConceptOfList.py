num_list=[10,20,30,40,50]
#print(num_list)
num_list.append(60)
#print(num_list)#
print("-----------------------------------------------------------------")


num_list=[10,20,30,40,50]
num_list.insert(3,60)## Insurt value at index 3
#print(num_list)

print("-----------------------------------------------------------------")

def proper_divisors(num):
    if num < 2:
        return []
    divisors = [1]
    i = 2
    while i * i <= num:
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
        i += 1
    return sorted(divisors)


print(proper_divisors(220))   # [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
print(proper_divisors(28))    # [1, 2, 4, 7, 14]
print(proper_divisors(1))     # []
