# 리스트
# 리스트 이름 = [요소 1,요소2,요소3,...]

#해달 프렌즈
Haedal_character = ["해달이","시라용","아리","메기","사스미"]

# 빈 리스트
mylist =[]
print(mylist)

# 파이썬 리스트 특징 = 요소들의 자료형을 통일하지 않아도 됨
mylist = [1,2,"해달이",True,['a','b','c']]
print(mylist)

#리스트 인덱싱
a= [1,2,3,4,5,6,7,8,9,10]
print(a[0])
print(a[5])
print(a[9])

# 음수 인덱싱
print(a[-1])
print(a[-5])

# 리스트 슬라이싱
print(a[0:3])
print(a[1:3])

print(a[:3])
print(a[7:])
print(a[:])
print(a[-4:-2])

# 리스트 수정
a[0] =100
print(a)

#리스트 삭제
del a[0]
print(a)

del a[3:]
print(a)

# 리스트 길이를 구하는 len()
a=[1,2,3,4]
print(len(a))

# 리스트의 값을 추가해주는 append()
mylist = ['a','b','c','d']
mylist.append('e')
print(mylist)

# 리스트의 값을 정렬해주는 sort()
mylist=[4,2,3,1]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)