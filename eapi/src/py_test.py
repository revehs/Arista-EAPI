response = "1 shutdown"
if 'shutdown' in response:
    print 'interface ethernet 1 shutdown'
        
        
'''
for i in range(0,10):

    for j in range(0,10):

        print str(i) + str(j)

grades = {'ego': 10, 'k8805': 6, 'sorialgi': 80}
for key in grades:
    print("key : %s \t value : %s" % (key, grades[key]))
    
'''

#import tkMessageBox
#tkMessageBox.showinfo('slogan', 'Cod!!')
'''
from tkMessageBox import showinfo
showinfo('slogan', 'Coding Evy!!')
'''

'''
f = open('myfile','w')
f.write('hi there\n') 

'''
'''      
class Person:
    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Genter = gender
    def aboutMe(self):
        print("name is"+self.Name+"!!, my age is "+self.Age+"!!")

class Employee(Person):
    def __init__(self, name, age, gender, salary, hiredate):
        Person.__init__(self, name, age, gender)
        self.Salary = salary
        self.Hiredate = hiredate
    def dowork(self):
        print("work hard")
    def aboutMe(self):
        Person.aboutMe(self)
        print("my name's "+self.Name)

t = Person("han","33", "male")
t.aboutMe()

t2 = Employee("han","33","male","7000","2010.01")
t2.aboutMe()
t2.dowork()

'''







