#Create an input that appends values to a list and has a parameter for length of list
def test1(length):
    i=int(1)
    while i<=length:
        val=int(input("Please enter a value: "))
        #check if the lists already exists to create if needed
        if 'vec' in locals():
            vec.append(val)
        else:
            vec=[val]
        i=int(i)+1
    #When length reached, return ordered list
    vec.sort()
    return(vec)
