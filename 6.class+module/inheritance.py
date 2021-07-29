class Student : #부모 클래스 
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def __str__(self) :
        return '안녕하세요 저는 {}이고, 학생입니다.'.format(self.name)

class EStudent(Student) : #부모 클래스를 상속받지만 부모에게 보낼수는 없다
    def __str__(self) :
        return '안녕하세요 저는 {}이고, 초등학생입니다'.format(self.name)
    def print_age(self) :
        print('{}의 나이는 {}살 입니다'.format(self.name , self.age))

class MStudent(Student) :
    def __str__(self) :
        return '안녕하세요 저는 {}이고, 중학생 입니다.'.format(self.name)

sasumi = Student('사스미' , 4)
haedal = EStudent('해달이' , 1)
boogie = MStudent('부기' , 5)

print(sasumi)
print(haedal)
print(boogie)

haedal.print_age()
