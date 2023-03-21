Food=500
Days=0
while True:
    if Food<=1: 
        break
    Food=Food/2
    Days=Days+1
    print(Food)
    print(f"{Days}:Days")