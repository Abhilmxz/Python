from library_fun.addbook import library

def delete():
    id=int(input('Enter ID of the book'))
    for i in library:
        if id==i[0]:
            library.remove(i)



            print('Book Deleted')