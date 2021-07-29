# 현재 온도
cur_tem = 20                    

# 온도 설정 함수
def set_tem(des_tem):           
    """
    온도를 설정하는 함수
    set_tem(설정할 온도)
    """
    global cur_tem

    if des_tem > cur_tem : # 목표온도가 현재온도보다 높은경우
         while des_tem > cur_tem :
             cur_tem += 1
             print(f'현재 온도는 {cur_tem}도 입니다.')
    elif des_tem < cur_tem : # 목표온도가 현재온도보다 낮을경우
        while des_tem < cur_tem :
            cur_tem -= 1
            print(f'현재 온도는 {cur_tem}도 입니다')
    
    return cur_tem
            


    
print("에어컨을 작동합니다.")

while True : 
    tem = input("원하는 온도를 설정해 주세요 : ")
    if tem == '종료' :
        print("에어컨을 종료합니다.")
        break
    elif int(tem) < 18 or int(tem) > 30 :
        print("입력을 확인해 주세요") 
    else :
        print(f'현재 온도는 {cur_tem}도 입니다.')
        cur_tem = set_tem(int(tem))
        
    
