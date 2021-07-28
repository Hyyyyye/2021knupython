# 변수와 인수


# 전역변수와 지역변수의 차이를 알아보자
def add_two_num(a,b) :
    print("덧셈중...")
    result = a + b # 지역변수
    return result

result = 0 #전역변수 
add_two_num(10,13)
print(result)