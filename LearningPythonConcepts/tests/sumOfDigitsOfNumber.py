number = input("Enter the number to find the sum of digits: ")

total = 0
for digit in number:
    total = total + int(digit)

print("Sum of digits:", total)
