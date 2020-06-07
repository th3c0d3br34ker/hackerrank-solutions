if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr.sort()
    max_score=max(arr)
    while(max_score in arr):
        arr.remove(max_score)
    print(arr[-1])


