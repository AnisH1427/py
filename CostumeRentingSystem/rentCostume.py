class Rent(object):
    def __init__(self):
        self.user_name=''
        self.listOfCostume=[]
        self.dict={1:None,2:None,3:None,4:None,5:None}
        self.count=0
        self.Bill=0
    def addvalue(self):
        #opening a file in readmode and appending the information in a list
        with open('rentList.txt') as fp:
            for i in fp:
                self.listOfCostume.append(i.split())
        #addding list value into dictionary       
        for key in self.dict:
            for i in range(len(self.listOfCostume)):
                if (key-1)==i: #because array index starts from 0 but not in case of dictionary
                    self.dict[key]= self.listOfCostume[i]

    def ChooseItem(self):
        name=input("Enter your Name :")
        addmore='Y'
        while addmore.lower()=='y':
            print("\nHello {}".format(name)+', ')
            for key in self.dict:
                print("please choose {} for renting {} : ".format(key,self.dict[key][0]))

                #selecting item as per key of dictionaries
            choose=int(input('Enter to choose :'))
            while self.dict.get(choose)==None: #checking if user enters a number not contain in dictionary
                print("The number do not contains in our System ! choose again")
                choose=int(input('Enter to choose :'))
                
            numbersOfItem=0
            while (numbersOfItem<=0 or numbersOfItem>int(self.dict[choose][3])):
                numbersOfItem=int(input("How many Quantity you need : "))
                if (numbersOfItem<=0):
                    print("\nDo not Enter negative or NULL Quantity\n")
                if (numbersOfItem>int(self.dict[choose][3])):
                        print(f"\nSorry 🙏,{numbersOfItem} numbers of {self.dict[choose][0]} is not available in our List\n")
            for i in range(len(self.listOfCostume)):
                self.listOfCostume[i][3]=int(self.listOfCostume[i][3])
                if self.dict[choose][0] in self.listOfCostume[i]:
                    self.listOfCostume[i][3]-=numbersOfItem

                    #calculating price amount i.e quantity * price per unit
                    self.Bill+=numbersOfItem*int(self.listOfCostume[i][2])
            print("\nUpdated List :")
            print("-"*74)
            print("Costume\t\t |Brand Name\t |Price(in$)5days|QuantityinStock|")
            print("-"*74)
            for i in self.listOfCostume:
            #adding each details in dictionary
                for j in i:
                    # j.split()
                    print(j,end="\t\t |")
                print("\n")
                print("-"*74)
            print(f"Notice & Invoice :\nDear {name} You have successfully rent {numbersOfItem} Quantity Of `{self.dict[choose][0]}` brand Name-->{self.dict[choose][1]}\n")
            addmore=input("Do you want to rent more Items ?\nIf yes press `Y` else press any key : ")

            self.count+=numbersOfItem
            if addmore.lower()=='y':
                continue
            else: break

        print("-"*674)
        print("\t\tInformation about Rented Items")
        print("-"*74)
        print(f"\tTotal rented Items | Price Amount")
        print('\t\t',self.count,'$\t\t',self.Bill,'$')
        print('-'*74)
        print("Note : Extra Charge will be charged in Case of returning after more than 5 days.")
        print("*"*74)

