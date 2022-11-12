class Return(object):
    def __init__(self):
        self.user_name=''
        self.listOfCostume=[]
        self.dict={1:None,2:None,3:None,4:None,5:None}
        self.count=0
        self.Bill=0
        self.extraCharge=0
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
        noDays=int(input("After how many days you are returning the item ?"))
        #if no of day exceed more than 5 days extra charge will be included
        if (noDays>5):
            self.extraCharge+=5*(noDays-5)
        print("\nNote : Returning after 5 days will be charged 5$ per day for overall items.\n")
        name=input("Enter your Name :")
        addmore='Y'
        while addmore.lower()=='y':
            print("\nHello {}".format(name)+', ')
            #asking user to choose items to be returned
            for key in self.dict:
                print("please choose {} for returning {} : ".format(key,self.dict[key][0]))

                #selecting item as per key of dictionaries
            choose=int(input('Enter to choose :'))
            #if user chooses the number not contained in dictionary
            while self.dict.get(choose)==None: #checking if user enters a number not contain in dictionary
                print("The number do not contains in our System ! choose again")
                choose=int(input('Enter to choose :'))
                
            numbersOfItem=0
            while (numbersOfItem<=0):
                numbersOfItem=int(input("How many Quantity you want to return : "))
                if (numbersOfItem<=0):
                    print("\nDo not Enter negative or NULL Quantity\n")
                    print(f"\nSorry 🙏,{numbersOfItem} numbers of {self.dict[choose][0]} is not available in our List\n")

            for i in range(len(self.listOfCostume)):
                self.listOfCostume[i][3]=int(self.listOfCostume[i][3])
                if self.dict[choose][0] in self.listOfCostume[i]:
                    self.listOfCostume[i][3]+=numbersOfItem
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
            print(f"Notice & Invoice :\nDear {name} You have successfully returned {numbersOfItem} Quantity Of `{self.dict[choose][0]}` brand Name-->{self.dict[choose][1]}\n")
            addmore=input("Do you want to return more Items ?\nIf yes press `Y` else press any key : ")

            self.count+=numbersOfItem
            if addmore.lower()=='y':
                continue
            else: break

            
        print("-"*75)
        print("\t\tInformation about returned Items")
        print("-"*75)
        print(f"\tTotal returned Items |\tPrice Amount |\tExtra charge |\tTotal Amount")
        print('\t\t',self.count,'\t\t',self.Bill,'$\t\t',self.extraCharge,'$\t\t',self.Bill+self.extraCharge,'$')
        print('-'*75)
      