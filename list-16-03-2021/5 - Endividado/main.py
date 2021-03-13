while True:

    quantity = int(input())
    
    if quantity <= 0:
        break
    
    price = [int(value) for value in input().split()]
    total = 0
    count = 0
    
    for x in range(quantity):
        total += price[x]
        if(total % 100 == 0):
            count += 1
    
    print(count)
    