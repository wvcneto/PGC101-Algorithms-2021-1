quantity = int(input())

message = []

if quantity >= 1:
    message.append("K")
    for x in range(1,quantity):
        message.append("k")
    message.append("!")

print("".join(message))
