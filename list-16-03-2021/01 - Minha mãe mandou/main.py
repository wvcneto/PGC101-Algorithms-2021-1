numberOfChoices = int(input())

result = []

for choice in range(numberOfChoices):
    n, k = [int(value) for value in input().split()]
    
    foodOneCount = 0
    chosenFood = ((k*29) % n) + 1
    
    for song in range(k*29):
        if(song % n == 0):
            foodOneCount += 1
        
    result.append(str(foodOneCount) + " " + str(chosenFood)) 

for value in result:
    print(value)
    
