# Given an array arr of size n−1 that contains distinct integers in the range of 1 to n (inclusive)
# , find the missing element. The array is a permutation of size n with one element missing.
# Return the missing element.

def missing(a,n):
    b=list(range(a[0],n+1))

    for i in range(n):
        if a[i] not in b:
            return a[i]



a=[1,2,3,5]
print(missing(a,len(a)))