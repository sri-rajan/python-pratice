a= [10,20,23,11,17]
b= [13,43,24,36,12]
total_lis = []
def total_li(l1,l2):
    for num in l1:
        if num%2 != 0:
            total_lis.append(num)
    for num in l2:
        if num%2 == 0:
            total_lis.append(num)
    return total_lis
print(total_li(a,b))
