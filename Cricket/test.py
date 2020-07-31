"""list=['a','b','c']
tuple=('a','b','c')
dict = {
    
    'a' : 'c',
    'b' : 'd'

}
set=set(list)
print(list)
print(tuple)
print(dict)
print(set)

z = ( x*2 for x in list )
print(z)

for key,value in dict.items():

    print('key : {}, value: {}'.format(key,value))

class Parent1():   
    def __init__(self,name1='abc'):

        self.first_name = name1
class Parent2():
    def __init__(self,name1='abc'):

        self.last_name = name1

class MyClass(Parent1,Parent2):

    def __init__(self,firstname='abc',lastname='def'):

        Parent1.__init__(self,name1=firstname)
        Parent2.__init__(self,name1=lastname)

    def printName(self):
       
        print(self.first_name + self.last_name)


obj=MyClass('Tushar','Sable')
obj.printName()


list=[1,2,3,4,5,6]
z = ( x*2 for x in list )
#print(z)

for x in range(6):
    #print(next(z))

select cname from tables
groupby cname count
where cname  > 1


o/p = "d!@/c-=*b%^&a"

groupby cname 
"""

def logic(input_str):
    
    alpha_index=list()
    for index,x in enumerate(input_str):
        if x.isalpha():
            alpha_index.append(x)
        

    print(alpha_index)

    print(input_str[alpha_index])

z ='a!@/b-=*c%^&d'

x = logic(z)
