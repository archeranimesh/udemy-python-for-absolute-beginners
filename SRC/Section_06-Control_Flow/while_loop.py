x = 1

while x < 10:
    if x == 4:
        x += 1
        continue

    print(x)
    x += 1

print("-" * 100)

x = 1
while x < 10:
    if x == 4:
        x += 1
        break

    print(x)
    x += 1
