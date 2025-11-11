accounts = {}

while True:
    user_input = input("명령어(개설,입금,출금,확인,종료)를 입력해주세요.")
    
    if user_input == "종료":
        break
    elif user_input == "개설":
        account_num = input("원하는 계좌번호를 입력해주세요: ")
        try: 
            account = int(account_num)
        except ValueError: 
            print("숫자로 입력해주세요.")
            continue 
        principal_amount = input("초기 입금액: ")
        try: 
            principal = int(principal_amount)
        except ValueError:
            print("숫자로 입력해주세요.")
            continue
        
        if account in accounts:
            print("이미 있는 계좌입니다.")
        else: 
            accounts[account] = principal
    
    elif user_input == "입금":
        account_to_add = input("입금할 계좌번호를 입력하세요: ")
        try: 
            account_to_add_num = int(account_to_add)
        except ValueError:
            print("숫자로 입력해주세요")
            continue
        amount_to_add = input("입금액: ")
        try: 
            amount_to_add_num = int(amount_to_add)
        except ValueError:
            print("숫자로 입력해주세요")
            continue
        if account_to_add_num not in accounts:
            print("없는 계좌입니다.")
        else:
            accounts[account_to_add_num] += amount_to_add_num 
    elif user_input == "출금":
        account_to_subtract = input("출금할 계좌번호를 입력하세요: ")
        try: 
            account_to_subtract_num = int(account_to_subtract)
        except ValueError:
            print("숫자로 입력해주세요")
            continue
        amount_to_subtract = input("출금액: ")
        try: 
            amount_to_subtract_num = int(amount_to_subtract)
        except ValueError:
            print("숫자로 입력해주세요")
            continue
        if account_to_subtract_num not in accounts:
            print("없는 계좌입니다.")
            
        elif accounts[account_to_subtract_num]<amount_to_subtract_num:
            print("잔액이 부족합니다.")
        else:
            accounts[account_to_subtract_num] -= amount_to_subtract_num 
    elif user_input == "확인":
        for account,amount in accounts.items():
            print(f"{account}에 해당되는 금액은 {amount}입니다.")
