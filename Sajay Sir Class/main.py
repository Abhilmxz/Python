from library_fun import addbook,display,update,delete


while True:
    print('1.Add book')
    print('2.Display book')
    print('3.Update book')
    print('4.Delete book')

    c=int(input('Enter your choice:'))
    if c==1:
        addbook.addbook()
    if c==2:
        display.display()
    if c==3:
        update.update()
    if c==4:
        delete.delete()
    # if c==5:
    #     break