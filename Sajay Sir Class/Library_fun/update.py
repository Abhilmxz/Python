from library_fun.addbook import library


def update():
     while True:
        print('1.Title')
        print('2.Price')
        print('3.Author')
        print('4.Publisher')
        print('5.Break')

        n=int(input('Enter your choice:'))

        if n==1:
            c=int(input('Enter Book ID:'))
            for i in library:
                if c==i[0]:
                    t=input('Enter New Title:')
                    i[1]=t
        if n==2:
            c=int(input('Enter ID'))
            p=int(input('Enter New Price:₹'))
            for i in library:
                if c==i[0]:
                    i[2]=p
        if n==3:
            c=int(input('Enter ID'))
            a=input('Enter Author:')
            for i in library:
                if c==i[0]:
                    i[3]=a

        if n==4:
            c=int(input('Enter ID'))
            a=input('Enter Publisher:')
            for i in library:
                if c==i[0]:
                    i[4]=a

        if n==5:
            break