entry = 0
sum = 0

print("Enter numbers to sum, negatvie number end list:")

while entry >= 0:
    entry = int(input())
    if entry >= 0:
        sum += entry
print("Sum =", sum)
