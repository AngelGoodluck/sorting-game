#here, we get the user's input and convert them to numbers in the form of float, then they are stored in a list.
#i converted to float because someone may want to use float numbers instead of just integers.
def getUserInput (*numbers):
    try:
        numbers = input("Enter numbers you want to sort [Separate them with spaces]: ")
        return list(map(float, numbers.split()))
    except ValueError: #if the user enters something that is not a number, this is shown here.
        print("Invalid input. Please enter valid numbers.")
        return []
    
#the sorting can either be ascending or descending so the user must specify here.
def sortingTechnique(numbers_list):
    print("""
    What type of sorting do u want to use?
    1. Ascending Order [Low to High]
    2. Descending Order [High to Low]
    """)
    
    try:
        sortMethod = int(input("Enter choice (1 or 2): ")) #accepts either 1 or 2 then changes it into an integer to be used int the match statement.
        sorted_list = list(numbers_list)
        n = len(sorted_list) #this is the length or number of characters in the list i.e list(numbers_list).
        match sortMethod:
            case 1:
                # Ascending order
                for i in range(n):
                    for j in range(0, n - i - 1): #starts at the first number and ends at the last but one since the first largest number will be at the end of the list.
                        # with the if statement, the computer swaps if the current number is larger than the next
                        if sorted_list[j] > sorted_list[j + 1]: #if current is > next, temp stores current, sorted_list[j]'s position stores next and the next now stores current till current is at the end of the list.
                            temp = sorted_list[j]
                            sorted_list[j] = sorted_list[j + 1]
                            sorted_list[j + 1] = temp
                return sorted_list
                
                 
            case 2:
                # Descending Order (Manual Bubble Sort)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        # IF-ELSE Statement: swap if the current number is smaller than the next
                        if sorted_list[j] < sorted_list[j + 1]:
                            temp = sorted_list[j]
                            sorted_list[j] = sorted_list[j + 1]
                            sorted_list[j + 1] = temp
                return sorted_list

            case _:
                print("You selected an invalid option. Returning the original list.")
                return numbers_list    

    except ValueError:
        print("You entered an invalid input. Please enter either 1 or 2.")
        return numbers_list

# Running the program
enteredNumbers = getUserInput()
if enteredNumbers:
    finalSortedNumbers = sortingTechnique(enteredNumbers)
    print(f'The original numbers were: {enteredNumbers}')
    print(f'The sorted numbers are: {finalSortedNumbers}')
