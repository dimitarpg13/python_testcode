size = int(input("Please enter the table size: "))
for row in range(1, size+1):
    for column in range(1, size+1):
        product = row*column
        print(product, end=' ')
    print()
