def selection_sort(num):
    for i in range(len(num)):
        lowest_num=i
        for j in range(i+1,len(num)):
            if num[j]<num[lowest_num]:
                lowest_num=j
        num[i],num[lowest_num]=num[lowest_num],num[i]
            
        

# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4,3,7,6]
selection_sort(random_list_of_nums)
print(random_list_of_nums)























