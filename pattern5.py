# Hollow reverse pyramid pattern
size = int(input("Enter the size: "))

for i in range(size):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # Printing stars Reverse
    for k in range(2 * (size - i - 1) + 1):
        if k == 0 or k == 2 * (size - i - 1):
            print('*', end='')
        else:
            # Print only stars in the first row
            if i == 0:
                print('*', end='')
            else:
                print(' ', end='')
    print()