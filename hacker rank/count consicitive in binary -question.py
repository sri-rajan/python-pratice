n = int(input())
count=str(bin(n)[2:]).split("0")
print(len(max(count)))
    
