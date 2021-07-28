# return이 발생하면 함수가 종료
def return_example(a,b) :
    if a > b :
        print("해달이")
        return
    else :
        print("부기")
    print("아리")

return_example(10,20)
return_example(20,10)