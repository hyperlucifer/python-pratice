s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2)) # this will print or store the union of 2 sets but the orignal sets is untouched

s1.update(s2) #to add set s2 at the end of s1 update function is used
print(s1)

city={"mumbai","pune","nashik","nagpur","delhi"}
city2={"mumbai","delhi","japur","lacknow","goa"}
# city3=city.intersection(city2) # it will print or store all the common elements of both of the sets
# print(city3)
# city.intersection_update(city2)# it will store only common elements of both the sets in city and delet others
# print(city)

# symetric_difference will print only uncommon elements of both the elements
city3=city.symmetric_difference(city2)
print(city3)

# difference will return the elements that are only present in setA 
city4=city.difference(city2)
print(city4)