# there is no such thing like public private or protected in python but there are some covenctions used by developers
#
# this is the normal defination of access modifiers
#
# public: public variables can be access throwhout the code,
# 
# private: they can be access in the class in which they are declared in  
# 
# protected: they can be access in the class in which they are declared in and their 
#            inharited classes
# 
# by default all the variables are public in python

# public

class Employee:
    def __init__(self):
        self.a=34

a= Employee()

print(a.a)

# private 
# in python ,there is no strict concept of "private" access modifiers like in some
# outher programming languages ,,however ,a convention has been established to indicate that a 
# a variable or method should be consider as private by prefixing its name by double underscoure(__)

class student:
    __id=8

s=student()
# print(s.__id) cannot be access directly 
print(s._student__id)# can be access indirectly,,this is also called name mangling,,it is used 
                     # to protect private  attributes from being accidentally overwritten by subclass
print(a.__dir__())

# proctected 
# it is define by single (_) but it is same like public ,,it is just a covencation not enforced by python