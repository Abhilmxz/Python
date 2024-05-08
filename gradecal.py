mark=int(input('Enter your Marks'))


if mark>=90:
    print("Youre grade is  A+")
elif 80<=mark<90:
    print('Youre grade is B+')
elif 70<=mark<80:
    print('Youre grade is C+')
elif 60<=mark<70:
    print('Youre grade is D+')
elif 50<=mark<60:
    print('Youre grade is  E')
else:
    print('Youre Not Eligible for Higher Studies')