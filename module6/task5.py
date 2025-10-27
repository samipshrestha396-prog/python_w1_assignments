# Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list
# -except that all uneven numbers have been removed.
# testing, write a main program where you create a list, call the function,
# -and then print out both the original as well as the cut-down list.


def num_list(parametr):
    even=[]
    for i in parametr:
        if i % 2==0:
            even.append(i)
    return even

new=[1,2,3,4,5,6,7,8,9]
final=num_list(new)
print(final)
print(new)