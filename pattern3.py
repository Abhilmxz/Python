# Reverse pyramid pattern
size = int(input("Enter the size: "))

for i in range(size):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing stars
    for j in range(2 * (size - i - 1) + 1):
        print('*', end='')
    print()