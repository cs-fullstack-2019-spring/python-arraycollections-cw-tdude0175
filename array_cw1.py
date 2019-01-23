def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    problem5()


# Create a function with the variable below. After you create the variable do the instructions below that.
#
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
#
#     b) Print the size of the array
#
# c) Delete the second element.
#
#     d) Print the 3rd element.

# list is already built
# it is a list NOT AN ARRAY
# brackets [] are used to locate via index
# remove can be used for a specific value


def problem1():
    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem2[2])

    arraysize = 0
    for x in arrayForProblem2:
        arraysize+=1
    print(arraysize)

    arrayForProblem2.remove("Kevin")
    print(arrayForProblem2[2])


# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q',
# ask them to input another string.

# wow

def problem2():
    while(True):
        userinput = input("literally just type q")
        if(userinput.lower() == "q"):
            break

# Create a function that contains a collection of information for the following.
# After you create the collection do the instructions below that.
#
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# a) Print the collection
#
# b) Print William's nickname

# you can do multi line lists and dictionaries
#using a loop to print out each element
#  print(Dictionary[stuff in dictionary]

def problem3():
    nicknamelist ={"Jonathan":"John",
        "Michael":"Mike",
        "William":"Bill",
        "Robert":"Rob"}
    for x in nicknamelist:
        print(f"{x} {nicknamelist[x]}")
    print(nicknamelist["William"])

# Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function
# length will count from 1
# an array will count from 0

def problem4():
    list = [5, 4, 3, 2, 1, 0]
    llength = len(list)
    for x in range(llength-1,-1,-1):
        print(list[x])

# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.

def problem5():
    listofnumbers = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    userinput = int(input("give me a number between 0,12"))

    numgreat = 0
    numequal = 0
    numsmall = 0

    for element in listofnumbers:
        if(element > userinput):
            numgreat+=1
        elif(element == userinput):
            numequal+=1
        elif(element < userinput):
            numsmall+=1
    print(f"{numgreat} are bigger, {numequal} are equal, {numsmall} aresmaller.")



if __name__ == '__main__':
    main()