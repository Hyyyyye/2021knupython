class Friends :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def hello(self) :
        print(f'안녕 난 {self.name}이야. 나이는 {self.age}살 이야!')
    
def add_to_N(n) :
    result = 0
    for i in range(n) :
        result += i
       
    return result

if __name__ == '__main__':
    print("여기는 모듈1")