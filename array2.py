# find the maximum and minimum element in an array

def findSum(A,N):
    if N == 1:
        return A[0]
        
    if A[0] > A[1]:
        maxi = A[0]
        mini = A[1]
    else:
        mini = A[0]
        maxi = A[1]
        
    for i in range(2,N):
        if A[i] > maxi:
            maxi = A[i]
        elif A[i] < mini:
            mini = A[i]
    return maxi + mini

N = 5
A = [-2,1,-4,5,3]

max = findSum(A,N)
print(min)