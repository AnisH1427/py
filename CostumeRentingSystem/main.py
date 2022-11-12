from rentCostume import Rent #importing rent class from rentCostume module
from returnCostume import Return #importing Return class from returnCostume module 
class CostumeRentingSystem(object):
    #constructor for initializing required lis and dictionaries
    def __init__(self):
        self.listOfCostume =[] #stores Costume from teext file
        self.dict={1:None,2:None,3:None,4:None,5:None}

    #method for working with our text file 'rentList.txt'
    def getFromTextFile(self):
        with open('rentList.txt') as fp:
            for i in fp:
                self.listOfCostume.append(i.split())
   
    def display(self):
        print()
        print("Welcome To My System ❤ 🙏🙏\nPlease see The list, So that we can provide service as per Your choice🥰🥰🥰")
        print()
        print("-"*74)
        print("Costume\t\t |Brand Name\t\t |Price(in$)5days|QuantityinStock|")
        print("-"*74)
        
        for i in self.listOfCostume:
            for j in i:
                j.split()
                print(j,end="\t\t |")
            print("\n")
            print("-"*74)
'''
making new class to Interact with User by inheriting our previous Class
This child class is also accessing another two module that contains Rent and return of a item.
'''
class InteractWithUsers(CostumeRentingSystem):
    def AskWithUsers(self):
        while True:
            confirmation=input("Do you want to use our System or not? \nType `Y` if {yes} else Press any key :")
            if confirmation.lower()!='y':
                print("See You Next Time... ")
                break
            print("You want to take COSTUME in Rent or Return it back ?")
            user_inp=input("Enter 'T' for rent and 'R' for Returning :")

            if user_inp.lower()=='t':
                callRent=Rent()
                callRent.addvalue()
                callRent.ChooseItem() 
                break
            elif user_inp.lower()=='r':
                callReturn=Return()
                callReturn.addvalue()
                callReturn.ChooseItem()
                break
        print("Thanks for Using my Program 🙏🙏🥰")
if (__name__=='__main__'):   #making a main function   
    myObj=InteractWithUsers()
    myObj.getFromTextFile()
    myObj.display()
    myObj.AskWithUsers()
