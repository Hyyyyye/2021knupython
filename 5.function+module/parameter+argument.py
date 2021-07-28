# 매개변수와 인수의 차이를 알아보자
def add_two_num(a,b) : # 매개변수
    print("덧셈중...")
    result = a + b # 지역변수
    return result

a = 10
b = 13

value = add_two_num(a,b) # 인수
print(value)