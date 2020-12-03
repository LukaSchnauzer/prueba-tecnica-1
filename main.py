import matriz

def main():
    T = int(input())
    inputs = []
    for _ in range(T):
        inputs.append(str(input()))
    
    for nm in inputs:
        blank = nm.find(' ')
        n = int(nm[:blank])
        m = int(nm[blank+1:])
        print(matriz.getDirectionAtEndWalk(n,m))

if __name__ == '__main__':
    main()