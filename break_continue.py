for i in range(10):
    print("5 X", i + 1, "=", 5 * (i+ 1))
    if(i == 10):
        break

print("Out of loop")

for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("6 X", i, "=", 6 * (i))
