
def while_loop(num, steps):
    i = 0
    numbers = []

    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + steps
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for j in numbers:
        print(j)
    return j

print(while_loop(10, 2))