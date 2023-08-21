import random
def main():
    level = get_level()
    score=solve2(level)
    print("Score: ", score)
def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level in [3,2,1]:
                break
        except:
            pass
    return level
def generate_integer(level):
    if level ==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
    elif level==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
    else:
        x=random.randint(100,999)
        y=random.randint(100,999)
    return x,y

def solve(x,y):
    count = 1
    while count<=3:
        try:
            javab=int(input(f"{x} + {y} ="))
            if javab ==(x+y):
                return True
            else:
                count+=1
                print("EEE")
        except:
            count+=1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

def solve2(level):
    count =1
    score = 0
    while count<=10:
        x,y =generate_integer(level)
        z=solve(x,y)
        if z ==True:
            score+=1
        count+=1
    return score
if __name__ == "__main__":
    main()