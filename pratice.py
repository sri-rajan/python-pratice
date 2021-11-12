#merge sort algorithms

def merge_sort(list):

    if len(list) <= 1:
        return list
    left_half,right_half = split(list)
    print("done")
    left = merge_sort(left_half)
    print("finish left")
    right = merge_sort(right_half)
    print("finish right")

    return merge(left,right)

def split(list):
    
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left,right):

    l = []
    i = 0
    j = 0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            l.append(left[i])
            print(l,1)
            i+=1
        else:
            l.append(right[j])
            print(l,2)
            j+=1

    while i<len(left):
        l.append(left[i])
        print(l,3)
        i+=1

    while j<len(right):
        l.append(right[j])
        print(l,4)
        j+=1
        
    return l

ans = merge_sort([1, 4,3, 2])
print(ans)

















