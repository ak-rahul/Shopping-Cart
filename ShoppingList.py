#Declaring constants
choice = 0
shoppingList = []

#Function to check whether the list is empty
def isEmpty() :
    return shoppingList == []

#Function to create a new Shopping List
def createList(n):
    for i in range(n) :
        item = input("\n\t\t\tEnter your item name: ")
        n = input("\t\t\tEnter quatity: ")
        shoppingList.append([len(shoppingList),item.upper(),n])
        
#Function to display the list        
def displayList() :
    if isEmpty() :
        print("\n\t\t\tYour Shopping List is Empty...")
    else :
        print("\n")
        for i in range(len(shoppingList)) :
            print("\t\t\t" + str(i+1) + ". " + shoppingList[i][1] + " of quantity " + shoppingList[i][2])
    
#Function to edit the list
def editList() :
    if isEmpty() :
        print("\n\t\t\tYour Shopping List is Empty....")
    else :
        displayList()
        num = int(input("\n\t\t\tEnter the id of the item to edit: "))
        if num in range(1,len(shoppingList)+1) :
            print("\t\t\t1. Change quantity of the item.")
            print("\t\t\t2. Remove the item.")
            edit = int(input("\t\t\tEnter choice: "))
            if edit == 1:
                shoppingList[num-1][2] = input("\t\t\tEnter the new quantity of the item: ")
                print("\t\t\t" + "Quantity of " + shoppingList[num-1][1] + " updated successfully")
            elif edit == 2:
                print("\t\t\t" + shoppingList[num-1][1] + " removed from your Shopping List")
                remove = shoppingList.pop(num-1)
                if len(shoppingList) > 1 :
                    for i in range(num-1,len(shoppingList)) :
                        shoppingList[i][0] = i
            else :
                print("\t\t\tInvalid Entry.....")
        else :
            print("\t\t\tItem id provided by User invalid....")

#Menu Drive Part of the Program            
print("\t\t\t\tSupermarket App")
print("\t\t\t\t***************")
while(choice != 4) :
    print("\n\t\t\t1. Add items to your Shopping List")
    print("\t\t\t2. Display your Shopping List")
    print("\t\t\t3. Edit your Shopping List")
    print("\t\t\t4. Exit")
    choice = int(input("\t\t\tEnter your choice: "))
    if choice == 1:
        n = int(input("\n\t\t\tEnter the number of items to add: "))
        createList(n)
    elif choice == 2:
        displayList()
    elif choice == 3:
        editList()
    elif choice == 4:
        print("\n\t\t\t\tThank You..")
        print("\t\t\t\t^^^^^^^^^^^")
    else :
        print("\n\t\t\tInvalid Choice....Repeat again...")
        
        
    
    
