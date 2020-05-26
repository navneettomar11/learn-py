
def listCompreshensions(x:int, y:int, z:int, n:int):
    notEqSumList = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k) != n:
                    notEqSumList.append([i,j, k])
    return notEqSumList

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(listCompreshensions(x,y,z,n))
