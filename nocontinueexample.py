sum = 0
done = False
while not done:
    val = int(input("ENter positive integer (999 quits):"))
    if val < 0:
        print("Negative value", val, "ignored")
    else:
        if val != 999:
            print("Tallying", val)
            sum += val
        else:
            done = (val == 999)
print("sum =", sum)

