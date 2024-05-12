# Hollow pyramid using star
size = int(input("Enter the size: "))

for i in range(size):
    # Printing spaces
    for j in range(size - i - 1):
        print(' ', end='')

    # Printing stars
    for k in range(2 * i + 1):
        # Print star at the start and end of the row
        if k == 0 or k == 2 * i:
            print('*', end='')
        else:
            if i == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
    print()