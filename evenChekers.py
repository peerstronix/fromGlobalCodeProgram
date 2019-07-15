#This is a list of integer numbers
numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]


#This is an empty even numbers list
evenNumbers = []

#This is an empty odd numbers list
oddNumbers = []


#This is a function to check for even and odd numbers.
#The function does not use a for loop bcos it will use the map function
def isEvenOrOdd(num):
    if(num % 2 == 0):
        evenNumbers.append(num)
        return  True
    oddNumbers.append(num)
    return False



list(map(isEvenOrOdd, numbers))

evenNumbers.sort()
print(evenNumbers)
oddNumbers.sort()
print(oddNumbers)

