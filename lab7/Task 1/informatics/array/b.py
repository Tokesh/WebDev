arr = input().split()
for i in range(0,len(arr)):
    if(int(arr[i]) % 2 ==0):
        print(arr[i], end = ' ')