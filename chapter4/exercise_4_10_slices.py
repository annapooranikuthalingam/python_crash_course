"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program
that do the following:

Print the message The first three items in the list are:. Then use a slice to print the first three items from
that program’s list.
Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle
of the list.
Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
"""
my_list=[]
for i in range(3,31,3):
    my_list.append(i)
print(my_list)
print(f'The first three items in the list are: {my_list[:3]}')
print(f'Three items from the middle of the list are: {my_list[int(len(my_list)/2)-2:int(len(my_list)/2)+1]}')
print(f'The last three items in the list are: {my_list[-3:]}')