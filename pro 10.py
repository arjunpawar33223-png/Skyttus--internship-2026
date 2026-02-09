def is_armstrong(n):
    temp = n
    sum = 0
    digits = len(str(n))
    
    while temp > 0:
        d = temp % 10
        sum += d ** digits
        temp //= 10
    
    return sum == n

print(is_armstrong(153))