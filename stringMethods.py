# strings are inmutable ,,means we can't change it ,,but 
# when we apply any method it will create a new string and we can store it in 
# variable or print it
a="sheth"
print(a.upper())
print(a.lower())
b="mothi mansa!!!!!!!!!"
print(b.rstrip("!"))#it will cut the given characters from rear only
print(b.replace("mansa","loka"))
print(b.split(" "))#it will convert the string into the list 
print(b.capitalize())#convert first character of string into captial and other into small
print(b.center(45))#it will add the spaces at the begining 
print(b.count("m")) #it will count the occerence of the given string
print(b.endswith("!"))#it will check weather the string ends with given character or not
print(b.find("i"))#it will return the index of the first occourance of the given string
print(b.title()) 