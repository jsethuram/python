def get_names():
    n = 5
    i = 0
    elementNames = []

    while i < n:
        elementInput = input("Enter the name of an element:")
        if elementInput == "":
            print("please type a string element")
        else:
            if elementInput.lower() in elementNames:
                print(elementInput.lower(),"was already entered          <--no duplicates allowed")
            else:
                elementNames.append(elementInput.lower())
                i = i + 1
    return elementNames

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
elements1_20 = open('elements1_20.txt', 'r')


templist = []
templistElements = []
elements1_20.seek(0)
element_list = elements1_20.readline().strip().lower()

while element_list:
    templist.append(element_list) 
    element_list = elements1_20.readline().strip().lower()

element_length = len(templist)
templistElements = get_names()
templistNotFound = []
templistNotFound = list(templistElements)
p = 0
j = 0
templistFound = []

for i in templistElements:
    for j in range(0,element_length):
        if i == templist[j]:
            p = p + 20
            templistFound.append(i)
            templistNotFound.remove(i)
                      
        
print(p,"% correct")
print("Found:"," ".join(templistFound))
print("Not Found:"," ".join(templistNotFound))
elements1_20.close()

