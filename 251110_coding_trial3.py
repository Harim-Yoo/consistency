answer = 42

while True:
    
    try:
        user_input = input("1과 100 사이의 숫자를 입력하세요")
        user_num = int(user_input)
        
    except ValueError:
        print("숫자를 입력해야지요")
        continue
        
    if user_num == answer:
        print("성공했어요!")
        break
    else:
        print("숫자가 달라요. 다른 숫자를 입력해보세요.")
        if user_num > answer:
            print("Down!")
        else:
            print("Up!")
        continue

