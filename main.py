my_list = [1, 2, 15, 4, 10, 44, 100, 101, 6, 2, 9]
len_my_list = len(my_list)
print(len_my_list)
#
# Write your code here.
#
my_list_1 = 0
for ele in range(0, len_my_list-1):
    if my_list_1 < my_list[ele]:
        my_list_1 = my_list[ele]

        # my_list.remove(ele)
print(sum(my_list))
print(f"The list with unique elements only: + {my_list_1}")

