#27 클래스 2

class Pet:
    def dog(self):
        print("멍")
        
    def cat(self):
        print("냥")
    
    def hamster(self):
        print("찍")
        
p1 = Pet()
p1.dog()

p2 = Pet()
p2.cat()

p3 = Pet()
p3.hamster()
'''
멍
냥
찍

위에 self가 없으면 에러가 난다.
'''


#이름과 나이를 전달받아 객체를 생성하는 Person클래스

class Person:
    def create_info(self, name, age):
        self.name = name
        self.age = age
        
    def print_info(self):
        print(self.name, ", ", self.age)

p1 = Person()
p1.create_info('kim', 27)
p1.print_info()

'''
kim ,  27
'''        

