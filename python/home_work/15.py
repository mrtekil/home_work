max_weight, n = int(input()), int(input())
fishers = sorted((int(input()) for _ in range(n)), reverse=True) 
cnt, l, r = 0, 0, len(fishers) - 1 
while r >= l: 
    if fishers[l] + fishers[r] <= max_weight: 
        r -= 1  
    l += 1  
    cnt += 1  
print(cnt)