def foundevenoddnumber(start, end):
    """foundevenoddnumber - reports on even / odd number occurences in predefined range"""
    for num in range(start, end):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)
