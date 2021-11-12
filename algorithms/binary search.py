#binary search by recurtion

def binary_search_rec(sorted_collection, item, left, right):
    
    if right < left:
        print("value not found")
        return None

    midpoint = left + (right - left) // 2
    print("midpoint is",midpoint)
    
    if sorted_collection[midpoint] == item:
        return midpoint
    
    elif sorted_collection[midpoint] > item:
        print("want smaller so right side = midpoint -1",end="\n\n")
        return binary_search_rec(sorted_collection, item, left, midpoint - 1)

    else:
        print("want bigger so left sidee = midpoint + 1",end="\n\n")
        return binary_search_rec(sorted_collection, item, midpoint + 1, right)

answers = binary_search_rec([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7, 0, 10)
if answers == None:
    print("Answer is not found")
else:
    print("the value is found at",answers)
print("binary search recursion is done",end="\n\n")



#binary search by loop
def binary_search(collection,item):
    left, right = 0,len(collection)-1
    
    while left <= right:
        midpoint =(left +right)//2
        print("midpoint is",midpoint)
        if collection[midpoint]==item:
            return midpoint
        elif collection[midpoint] < item:
            left = midpoint + 1
            print("want bigger so left side = midpoint +1 ",end="\n\n")
        else:
            right = midpoint - 1
            print("want smaller so right side = midpoint -1 ",end="\n\n")

answer = binary_search([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],18)
if answer == None:
    print("Answer is not found")
else:
    print("the value is found at",answer)
print("binary search done")


    
    
    


