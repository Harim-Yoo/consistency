nums = [1,2,3]

def f(path):
    if len(path) == len(nums):
        return None
    
    for i in range(len(nums)):
        if nums[i] in path:
            pass
        if nums[i] not in path:
            path.append(nums[i])
            print(path)
            f(path)
            path.pop()

f([])


-------------------------------------------------------------------
이틀동안 헤매다가 드디어 이해함!!!

(1) f([]) --> i=0 --> path.append(nums[0]) --> [1] --> f([1]) (여기서 pop-stage까지는 안 감.) 
(2) f([1]) --> i=0 --> pass --> i=1 --> path.append(nums[1]) --> [1,2] --> f([1,2]) (여기서 pop-state까지는 안 감.) 
(3) f([1,2]) --> i=0,1 pass --> i=2 --> path.append(nums[2]) --> [1,2,3] --> f([1,2,3]) 
(4) f([1,2,3]) --> len([1,2,3])=3 --> return None (5) f([1,2,3]) --> [1,2,3] pop --> [1,2] 
(6) (3) state가 받아서, f([1,2]) pop 이유는 f([1,2])는 loop 다 돌았거든. 그러니깐, 쓸수 있는 i도 없고, 이미 f([1,2,3])까지 다 갔었어!! 그러니깐, pop!!
(7) (2) state가 받았는데, i=2 안 했었음. 즉, (2) state에서 i=2 마지막까지 다 도는 것임. 그래서, 해봤더니, f([1,3]) 도전 
(8) f([1,3]) --> i=0 pass --> i=1--> [1,3,2] --> f([1,3,2])
(9) f([1,3]) --> i=2 pass --> pop 
(10) f([1]) --> (7)을 보니깐, 다 돌았네. pop --> f([])
(11) (1)으로 복귀 그런데, 1번은 i=0일때 멈췄었네, i=1일때 해봐야지. f([2]) 시작!!
