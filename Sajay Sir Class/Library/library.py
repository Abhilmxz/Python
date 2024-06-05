
library=[[1,'Ram C/O Anandhi',499,'Akhil P Daharmajan','DC Books'],[2,'Orikkal',500,'N Mohanan','DC Books'],[3,'Daivathinte Charanmar',284,'Joseph Annamkutty Jose'
,'DC Books']]
while True:
    print('1.Add book')
    print('2.Delete book')
    print('3.Price of Book')
    print('4.Update book')
    print('5.Display Books')

#Add book and Update book info
    c=int(input('Enter your Choice:'))
    if c==1:
        id=int(input('Enter ID of the Book'))
        title=input('Title of Book')
        price=int(input('Enter the Price'))
        author=input('Enter Authors name')
        publisher=input('Enter Publisher')
        l=[]
        l.append(id)
        l.append(title)
        l.append(price)
        l.append(author)
        l.append(publisher)
        library.append(l)
        print('Book added')

    if c==2:

        id=int(input('Enter ID of the book'))
        for i in library:
            if id==i[0]:
                library.remove(i)



                print('Book Deleted')


    if c==3:
        id=int(input('Enter ID of book'))
        for i in library:
            if id==i[0]:
                print('price=',i[2])

#Update Book detials
    if c==4:
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

#Display Books List

    if c==5:
        for i in library:
            print('ID:',i[0])
            print('Title:',i[1])
            print('Price:₹',i[2])
            print('Author:',i[3])
            print('Publisher:',i[4])












