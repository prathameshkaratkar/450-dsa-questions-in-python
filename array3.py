# find the 'kth' max and min element of an array

def kthsmallest(arr,k):
    if len(arr) == 1:
        return arr[0]

    arr.sort()          # it will sort the array inbuilt function
    return arr[k-1]

arr = [7,10,4,3,20,15]
k = 3
print(kthsmallest(arr,k))