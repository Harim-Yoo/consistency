inventory = {}

print("재고 시스템 시작")
print("명령: 추가, 수정, 제거, 확인, 종료")

while True:
    command = input("명령어를 입력하세요: ")
    
    if command == "종료":
        break
    
    if command == "추가":
        item = input("추가할 아이템 이름: ")
        
        if item in inventory:
            print("또 추가할순 없어요. 수정을 활용하세요.")
        else: 
            try:
                quantity = int(input("추가할 수량: "))
                inventory[item] = quantity
                print("추가 완료.")
                
            except ValueError:
                print("숫자를 넣어야지요.")
    elif command == "수정":
        item = input("수정할 아이템 이름: ")
        
        if item not in inventory:
            print("수정할 아이템이 없어요. 추가하세요.")
        else:
            try:
                quantity = int(input("수정할 수량: "))
                inventory[item] = quantity
                print("수정완료")            
            except ValueError:
                print("숫자를 입력하세요")
    elif command == "제거":
        item = input("제거할 아이템 이름: ")
        try:
            del inventory[item]
            print(f"{item}을 제거했어요.")
        except KeyError:
            print(f"{item}이 없어요.")
    elif command == "확인":
        print(inventory)
        if not inventory:
            print("아무것도 없어요.")
    else:
        print("명령어를 제대로 입력하세요.")


            
        
