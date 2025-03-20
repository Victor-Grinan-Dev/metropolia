# BUBBLE SORT
def bubble_sort(num_list):
    list_length = len(num_list)
    for i in range(list_length):
        if num_list == sorted(num_list):
            break
        for j in range(list_length - 1):
            if num_list[j] > num_list[j + 1]:
                middleman = num_list[j + 1]
                num_list[j + 1] = num_list[j]
                num_list[j] = middleman
    return num_list


a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element : " % i))
    a.append(value)
print("The Sorted List in Ascending Order : ", bubble_sort(a))
