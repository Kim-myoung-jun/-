#28 클래스 3

#클래스, 객체, oop

#1. 클래스 생성
class Person:
    #생성자
    def init(self):
        print('객체 생성')
        
#2 클래스 사용
p1 = Person()
p1.init()
'''
객체 생성
'''

# 위의 생성자 메서드를 이용해서 앞의 예제 구현
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_info(self):
        print(self.name, ", ", self.age)

p2 = Person2('kim', 27)
p2.print_info()

p3 = Person2('hong', 19)
p3.print_info()

'''
kim ,  27
hong ,  19
'''
#위에 반드시 __init__을 붙여줘야한다. __init__은 특별한 생성자


#소멸자
#생성자는 __init__ 소멸자는 __del__
class SmartPhone:
    #생성자
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(self.name+" 객체 생성")
        print("-"*40)
        print(self.name+"스마트폰의 가격은 "+str(self.price)+"원 입니다")
        print("-"*40)
        
    #소멸자
    def __del__(self):
        print(self.name+" 객체 소멸")
        
s1 = SmartPhone("Apple", 1000000)
del s1
'''
Apple 객체 생성
----------------------------------------
Apple스마트폰의 가격은 1000000원 입니다
----------------------------------------
Apple 객체 소멸
'''

#클래스 메서드 안에서 다른 메서드 호출
class Test:
    def a_method(self):
        print("a_method create")
    
    def b_method(self):
        self.a_method() #self사용해서 a_method호출
        
t1 = Test()
t1.a_method()
t1.b_method()
'''
a_method create
a_method create
'''
    
    
#만약 위의 b_method에서 self.a_method의 self를 지우면 외부의 a_method 가르킴
class Test2:
    def a_method2(self):
        print("a_method create")
    
    def b_method2(self):
        a_method2() #self사용해서 a_method호출
    

def a_method2():
    print("클래스 외부에 정의된 a_method")    
t2 = Test2()
t2.a_method2()
t2.b_method2()

'''
a_method create
클래스 외부에 정의된 a_method
'''

#클래스 변수
class Test3:
    a_var = 0
    
    def a_method3(self):
        Test3.a_var = 6000
        
    def b_method3(self):
        self.a_var = 300
    
print("1. 초기값 : ", Test3.a_var)
#1. 초기값 :  0

Test3.a_var = 3000
print("2. 변경", Test3.a_var)
#2. 변경 3000

t3 = Test3()
t3.a_method3()
print("3 클래스 내 메서드 호출로 변경", Test3.a_var)
#3 클래스 내 메서드 호출로 변경 6000

#print(Test3.a_method3())
#직접 호출은 에러 발생

#값이 변경 안되는 경우

class Test4:
    
    var_4 = 0
    
    def method_4(self):
        self.var_4 = 300

print("초기값 : ", Test4.var_4)

t4 = Test4()
t4.method_4()
print("4. 300으로 변경", Test4.var_4) #변경안된 앞의 값인 0 출력됨
#method_4 의 self.var_4 를 사용했기 때문에 값 변경이 안됨
#t4 에는 300이 저장됨
print("check : ", t4.var_4)
# check : 300

#혹은 위의 self.var_4를 Test4.var_4로 변경


#특정 클래스의 인스턴스 유무 확인 -> isinstance( [인스턴스 객체명], [클래스명] )
class Test5:
    pass

class Test6:
    pass

t5 = Test5()
result = isinstance(t5, Test5)
print("Test5 클래스의 인스턴스 객체가 맞는가?", result)
#True

result2 = isinstance(t5, Test6)
print("Test6 클래스의 인스턴스 객체가 맞는가?", result2)
#False




#객체의 개수
class Test7:
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.increase_obj()
        
    def increase_obj(self):
        Test7.count += 1

t7 = Test7('kim', 20)
print('count - ', Test7.count)
#count - 1
