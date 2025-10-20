res = []

def andae(path):
    
    if len(path)==10**2:
        return None
    path = path + "!"
    res.append(path)
    andae(path)

andae('안돼')
print(res) 
