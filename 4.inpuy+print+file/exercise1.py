# 해달이의 집에서 학교까지의 거리
# 숫자 두개를 입력 받아 둘 중 큰 값에서 작은 값을 빼서 거리를 구하는 프로그램 작성

input1 = input("첫 번째 수를 입력하세요 : ")
input2 = input("두 번째 수를 입력하세요 : ")

if input1 > input2 :
    result = int(input1) - int(input2)
else :
    result = int(input2) - int(input1)

print(result)