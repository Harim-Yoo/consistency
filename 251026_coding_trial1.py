men = ['m'+str(i) for i in range(1,7)]
women = ['w'+str(i) for i in range(1,7)]
people = men+women 

res = []

def dfs(idx, selected, m_count, w_count):
    if len(selected)==5:
        if m_count>=2 and w_count>=2:
            res.append(selected.copy())
        return None
    if idx == len(people):
        return None 
    
    person = people[idx]
    
    if person.startswith('m'):
        dfs(idx+1,selected+[person],m_count+1,w_count)
    else:
        dfs(idx+1,selected+[person],m_count,w_count+1)
    
    dfs(idx+1,selected, m_count, w_count)

dfs(0,[],0,0)
print(res[:3])
