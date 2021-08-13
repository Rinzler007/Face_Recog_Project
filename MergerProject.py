import Recognize
import SavePerson

while True:
    choice = int(input('Enter 1 to Recognize Person 2 to Save a New Person:'))
    if choice == 1:
        Recognize.detectFace()
    elif choice == 2:
        print('Enter Name of New Person')
        SavePerson.newPerson()
    elif choice == 0:
        break