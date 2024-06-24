library = [[1,'Ram C/O Anandhi',499,'Akhil P Daharmajan','DC Books'],[2,'Orikkal',500,'N Mohanan','DC Books'],[3,'Daivathinte Charanmar',284,'Joseph Annamkutty Jose'
,'DC Books']]

def addbook():
    l = []
    id = int(input('Enter ID of the Book'))
    title = input('Title of Book')
    price = int(input('Enter the Price'))
    author = input('Enter Authors name')
    publisher = input('Enter Publisher')

    l.append(id)
    l.append(title)
    l.append(price)
    l.append(author)
    l.append(publisher)
    library.append(l)
    print(library)