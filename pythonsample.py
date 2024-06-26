"""QUESTION:
Given a list of integers, write a program to identify contiguous sub list that has the largest
sum and print the sub-list. A non-empty slice of the list with step size 1 can be considered
as contiguous sub-list.
Output should be space-integrated integers."""

a = list(map(int, input().split()))

if not a:
    print(0)
else:
    sum_dict = {}
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            sum_dict[tuple(a[i:j])] = sum(a[i:j])
    keys = list(sum_dict.keys())
    values = list(sum_dict.values())
    max_sum_index = values.index(max(values))
    print(*keys[max_sum_index])
