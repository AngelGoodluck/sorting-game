#here, we get the user's input and convert them to numbers in the form of float, then they are stored in a list.
#i converted to float because someone may want to use float numbers instead of just integers.
def getUserInput (*numbers):
    try:
        numbers = input("Enter numbers you want to sort [Separate them with spaces]: ")
        return list(map(float, numbers.split()))
    except ValueError: #if the user enters something that is not a number, this is shown here.
        print("Invalid input. Please enter valid numbers.")
        return []

enteredNumbers = getUserInput()

#the sorting can either be ascending or descending so the user must specify here.
def sortingTechnique(sortMethod):
    try:
        sortMethod = int(input("What type of sorting do u want to use? "))
        print("""
              1. Descending Order
              2. Ascending Order
               """)
        if sortMethod == 1:
           temp = numj
           numj = enteredNumbers[i]
           for i in range(len(enteredNumbers)):
               if temp < enteredNumbers[i]:
                   numj = temp
                   temp = enteredNumbers[i]
        elif sortMethod ==2:
            pass
        return
    except ValueError: #if the user enters something that is not a number, this is shown here.
        print("Invalid input. Please enter either 1 or 2")
        return

sortingTechnique(sortMethod= 1)
print(f'The sorted numbers are: {sortingTechnique}')