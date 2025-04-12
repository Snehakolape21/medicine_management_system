# Clear options for each CRUD operation.

# Proper use of import and class objects (medicine, medicineopration).

# while loop for continuous execution until exit.

# All necessary user inputs are handled.

from admin import medicineopration
from paramter import medicine
import sys


opr=medicineopration()
choice=0
while choice !=6: 
    print('''
          1. add medicine
          2. update medicine
          3. delete medicine
          4. get medicine by id
          5. show all medicine 
          6. exit
          ''')   
    choice=int(input('plz enter your choice')) 
    if choice==1:
        i=int(input('enter the medicine id'))
        t=input('enter the medicine name')
        a=input('enter the manufacturer')
        p=int(input('enter the price'))
        medicine1=medicine(i,t,a,p)
        opr.add(medicine1)
    elif choice==2:
        i=int(input('enter the medicine id to be updated'))
        t=input('enter the medicine name')
        a=input('enter the manufacturer')
        p=int(input('enter the price'))
        medicine1=medicine(i,t,a,p)
        opr.update(medicine1) 
    elif choice==3:
        i=int(input('enter the medicine id to delete'))
        opr.delete(i)
    elif choice==4:
        i=int(input('enter the medicine id'))
        opr.view(i)
    elif choice==5:
        opr.getall()
    elif choice==6:
        print('exiting the application')
        sys.exit()