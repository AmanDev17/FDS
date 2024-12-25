'''
AIM:
A) Write a Python program 

1) Store names and mobile numbers 
of your friends in sorted order on names
2) Search friend name using Binary Search (recursive and nonrecursive)
3) Insert new friend in phonebook list

B) Write a Python program 

1) Store names and mobile numbers 
of your friends in sorted order on names
2) Search friend name using Fibonacci search
3) Insert new friend in phonebook list

INPUT: 
    1. Number of Friends in PhoneBook
    2. Name and mobile of Friends 

OUTPUT:
    1. Display Friend list
    2. Search friend using Binary Search
    3. Search friend using Fibonacci Search

AUTHOR: Aman Singh
DATE: 16.08.2024
'''
class Friend:
    def _init_(self):
        name=None
        mobile=0

#Implementation class
class PhoneBook:
    def _init_(self):
        self.N=0 # Number of friends in phonebook
        self.friendList=[] #friends in phonebook
       
    #1. Read friends name and mobile
    def getFriendDetails(self,nof):
        self.N=nof
        for i in range(self.N):
            friend=Friend()
            print("Enter Friend name and mobile for Friend-",i+1)
            name=input("Enter Name of friend::")
            mobile=int(input("Enter mobile no. of friend::"))
            friend.name=name
            friend.mobile=mobile
            self.friendList.append(friend)
        
    #2. Display Friend Details
    def displayFriendList(self):
        print("\nThe Friend PhoneBook is")
        for i in range(self.N):
            print(self.friendList[i].name,"  ",self.friendList[i].mobile )

    #3. Search friend name using Binary Search
    def binarySearchNonrecursive(self,key):
        l=0
        u=self.N-1
        while(l<=u):
            mid=(l+u)//2
            if(key==self.friendList[mid].name):
                print("\nName found in Friend list at location ",mid+1)
                break
            elif(key>self.friendList[mid].name):
                l=mid+1
            else:
                u=mid-1
        if(l>u):
            print("Name not found")


    #4.search a friend name using using binaary recursion
    def binarySearchRecursive(self,key,l,u):
        if(l<=u):
            mid=(l+u)//2
            if(key==self.friendList[mid].name):
                print("\nName found in Friend list at location ",mid+1)
                return
            elif(key>self.friendList[mid].name):
                self.binarySearchRecursive(key,mid+1,u)
            else:
                self.binarySearchRecursive(key,l,mid-1)
        else:
            print("Name not found")
    
    def bubbleSort(self):
        for i in range(self.N-1):
            for j in range(0,self.N-i-1):
                if self.friendList[j].name > self.friendList[j+1].name:
                    temp=self.friendList[j]
                    self.friendList[j] = self.friendList[j+1] 
                    self.friendList[j+1]=temp
#Driver Code
frn=PhoneBook()
choice=0

while(choice != 6):
    print("\n******FRIEND PHONE BOOK*****")
    print("1. Read Friend name and mobile details")
    print("2. Display Friend details")
    print("3. Search friend name using Binary Search")
    print("4. Search friend name using Fibonacci Search")
    print("5. Insert new friend details")
    print("6. Exit Application")
    choice=int(input("What operation::"))
    
    if (choice ==1):
        n=int(input("Enter number of Friends::"))
        frn.getFriendDetails(n)
    elif (choice ==2):
        frn.displayFriendList()
    elif (choice ==3):
        print("1. Search name using Non Recurssive")
        print("2. Search name using Recurssive")
        choice1=int(input("What operation::"))
        if(choice1==1):
            name=input("Enter the name to be searched:")
            frn.bubbleSort()
            frn.binarySearchNonrecursive(name)
        elif(choice1==2):
            name=input("Enter the name to be searched:")
            frn.bubbleSort()
        #frn.binarySearchrecursive(name)
        else:
            print("Wrong Choice")
    elif (choice ==4):
        pass
    elif (choice ==5):
        pass
    elif (choice ==6):
        print("Good By")
        break
    else:
        print("Wrong Choice")