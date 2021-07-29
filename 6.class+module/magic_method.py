#  클래스 - 붕어빵 틀 만들기
class FishBread :
    
    # 메소드 만들기
    # 붕어빵 굽기
    def __init__(self, ingredients, price) : # 초기화
        self.__ingredients = ingredients #언더바 두개 입력하면 클래스 외부에서 접근 불가능
        self.__price = price

    # 붕어빵 살펴보기
    def __str__(self) : # 살펴볼때 
        return '{}붕어빵, 가격 {}원'.format(self.__ingredients,self.__price)

    def __add__(self, other) : #add 연산자에 추가한 기능
        return self.__price + other.__price
    

# 객체(인스턴스) - 붕어빵 만들기
a = FishBread("팥 ",400)
b = FishBread("슈크림 ",500)

print(a)
print(b)

print("붕어빵 a,b 합쳐 %d 원" % (a+b))