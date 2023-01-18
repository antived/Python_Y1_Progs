# AdAstra 2022-23 problem-1
# program to find sum of smallest & biggest 6 numbers in a 7 number array & print them separated by a space
# - vedant dutta

def UnlockDoor(numArr):
    # first sort array smallest to largest
    numArr.sort()
    # sum the smallest 6 array elements from sorted array
    sumSmall = sum(numArr[:6])
    # sum the biggest 6 array elements from sorted array
    sumBig = sum(numArr[-6:])
    # prepare the unlock code by concatenating smallest & 
    # biggest number sums separated by space as asked
    return str(sumSmall) + " " + str(sumBig)

# main()

# initialize a alien code array of 7 digits
# same could be taken from user as input as well
codedNumArray = [-11, 13, 23, 1, 0, 5, 9]

unlockCode = UnlockDoor(codedNumArray)

print(unlockCode)
