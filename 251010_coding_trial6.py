#2022 AMC10B Problem 7

answer = [] # 비어있는 list 만들기

for a in range(-36,37):
    for b in range(-36,37):
        if a*b == 36 and a!=b:
            answer.append(a+b)

unique_k = set(answer) #set을 쓰면, 중복된 값들을 제거한 상태로 set을 주게 됨.

print(len(unique_k))
