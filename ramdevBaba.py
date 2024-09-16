def sol(arr,n,s):
    for ind1,i in enumerate(arr):
        for ind2,j in enumerate(arr,ind1+1):
            if i+j==s:
                print(ind1,ind2)
                return
    
    print("no ans found")
a=[12,45,23,54,23]
sol(a,len(a),35)