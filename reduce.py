# my_list = ['s', 'n', 'e', 'n', 's', 'e', 's', 'e', 'n', 'w']

# def reduce_direction(alist):
#     cancel_pair = {
#         'n': 's',
#         's': 'n',
#         'w': 'e',
#         'e': 'w'
#     }

#     i = 0
#     did_pop = False
#     while i < len(alist) - 1:
#         if cancel_pair[alist[i]] == alist[i+1]:
#             del alist[i]
#             del alist[i]
#             did_pop = True
#         else:
#             i += 1
#     if did_pop:
#         reduce_direction(alist)
#     return alist

# thru = reduce_direction(my_list)
# print(thru)


def reduce_direction(alist):
    opposite_directions = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }
    
    direction_stack = []
    for direction in alist:
        if direction_stack and direction_stack[-1] == opposite_directions[direction]:
            direction_stack.pop()
        else:
            direction_stack.append(direction)
    return direction_stack

print(reduce_direction(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']))