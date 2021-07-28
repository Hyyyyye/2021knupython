# for문 활용한 파일 출력(쓰기)
f = open('haedal.txt','w')

for i in range(100):
    f.write(f"Hello Haedal! {i}\n")
f.write("Good Morning")

print("쓰기 종료")

f.close()