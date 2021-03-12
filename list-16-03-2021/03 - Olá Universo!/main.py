class Planet:
    def __init__(self, name, contactYear, timeSpend):
        self.name = name
        self.contactYear = contactYear
        self.timeSpend = timeSpend

while True:
    count = int(input())

    planets = []

    if count == 0:
        break
    
    for x in range(count):
        name, contactYear, timeSpend = [value for value in input().split()]
    
        p = Planet(name, int(contactYear), int(timeSpend))
        
        planets.append(p)
    
    planets.sort(key = lambda p: (p.contactYear - p.timeSpend))
    print(planets[0].name)
   