inventory = []

print("재고 관리 시작합니다.")
print("명령어: 추가, 제거, 종료, 확인")

while True:
    command = input("명령어를 입력하세요.")
    
    if command == "종료":
        break
    
    if command == "추가":
        item = input("추가할 아이템 이름: ")
        inventory.append(item)
    elif command == "제거":
        try: 
            item = input("제거할 아이템 이름: ")
            inventory.remove(item)
        except ValueError:
            print("제거할 아이템이 없어요.")
    elif command == "확인":
        if not inventory:
            print("inventory가 비어있어요.")
        else: 
            print(inventory)
    else: 
        print("명령어를 제대로 입력하세요.")

print(f"최종 inventory는 다음과 같습니다. {inventory}")
        
