list=[[1,'Expluse',50000,2,'Hero Honda'],[2,'Piaggio Ape Auto DX',500000,3,'Piaggio'],[3,'Mahindra Thar',1100000,4,'Mahindra']]
while True:
    print('1.Add Vehicle')
    print('2.Delete Vehicle')
    print('3.Vehicle Price')
    print('4.Update Vehicle info')
    print('5.Display Vehicle')

#Add Vehicle and Update Vehicle info
    c=int(input('Enter your Choice:'))
    if c==1:
        vehicle_number=int(input('Enter Number of the Vehicle'))
        vehicle_name=input('Enter Vehicle Name')
        vehicle_price=int(input('Enter Vehicle Price'))
        vehicle_wheels=input('Enter Wheels')
        vehicle_brand=input('Enter Vehicle Brand')
        l=[]
        l.append(vehicle_number)
        l.append(vehicle_name)
        l.append(vehicle_price)
        l.append(vehicle_wheels)
        l.append(vehicle_brand)
        list.append(l)
        print('Vehicle added')

    if c==2:

        id=int(input('Enter Number of the Vehicle'))
        for i in list:
            if id==i[0]:
                list.remove(i)



                print('Vehicle Deleted')


    if c==3:
        id=int(input('Enter Number of the Vehicle'))
        for i in list:
            if id==i[0]:
                print('price=',i[2])

#Update Vehicle detials
    if c==4:
        while True:
            print('1.Vehicle Name')
            print('2.Vehicle Price')
            print('3.Vehicle Wheels')
            print('4.Vehicle Brand')
            print('5.Break')

            n=int(input('Enter your choice:'))

            if n==1:
                c=int(input('Enter Number of the Vehicle:'))
                for i in list:
                    if c==i[0]:
                        t=input('Enter New Name:')
                        i[1]=t
            if n==2:
                c=int(input('Enter ID'))
                p=int(input('Enter New Price:₹'))
                for i in list:
                    if c==i[0]:
                        i[2]=p
            if n==3:
                c=int(input('Enter ID'))
                a=input('Enter Wheels:')
                for i in list:
                    if c==i[0]:
                        i[3]=a

            if n==4:
                c=int(input('Enter ID'))
                a=input('Enter Brand:')
                for i in list:
                    if c==i[0]:
                        i[4]=a

            if n==5:
                break

#Display Vehicles List

    if c==5:
        wheel_no = input("Enter no of wheels (all/wheel number):")
        for i in list:
            if str(i[3]) == str(wheel_no) or str(wheel_no)=="all":    
                print('ID:',i[0])
                print('Vehicle Name:',i[1])
                print('Vehicle Price:₹',i[2])
                print('Vehicle Wheels:',i[3])
                print('Vehicle Brand:',i[4])
