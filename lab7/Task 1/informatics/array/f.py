arr = input().split()
cnt = 0
for i in range(1,len(arr)-1):
    if(int(arr[i]) > int(arr[i+1]) and int(arr[i]) > int(arr[i-1])):
        cnt += 1
print(cnt)