# 간단한 파일 입력
print('# read() 함수')
f = open('haedal.txt','r')
a = f.read()
print(a)
f.close()

print('# readlines() 함수')
f = open('haedal.txt','r')
b = f.readlines()
print(b)
f.close()

print('# readline() 함수')
f = open('haedal.txt','r')
c = f.readline()
print(c)
f.close