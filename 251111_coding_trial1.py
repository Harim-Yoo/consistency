def get_digit_sum(number_string):
    total_sum = 0
    for num in number_string:
        total_sum += int(num)
    return total_sum

while True:
    user_input = input("숫자를 넣으세요. 끝내려면 done을 입력하세요")
    
    if user_input == 'done':
        print("수고하셨습니다.")
        break
    
    if not user_input.isnumeric():
        print("양의 정수를 넣어주세요.")
        continue 
    
    my_sum = get_digit_sum(user_input)
    
    print(f"{user_input}의 자리수 합은 {my_sum}입니다.")
