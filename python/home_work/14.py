def rot(arr): return arr[-1:] + arr[:-1]
input() 
print(*rot(input().split()))