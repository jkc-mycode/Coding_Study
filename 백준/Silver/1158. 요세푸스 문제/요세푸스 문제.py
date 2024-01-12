n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
result = []

i = k-1
while len(arr) > 1:
    while i >= len(arr):
        i -= len(arr)
    
    result.append(arr[i])
    arr.remove(arr[i])
    i += k-1

result += arr

print("<" + str(result)[1:-1] + ">")