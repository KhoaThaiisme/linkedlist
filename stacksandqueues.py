# list - time complexity 
# search list O(N)
[12, 3, 58, 4,19].index(4)

# index into a list O(1)
[3,6,19,10][3]

# copy list O(N)
[3,1,9][:]

# adding to list O(1)
[1,2,3].append(4)

# removing from end O(1)
[1,2,3].pop()

# removing from specific position O(N)
[1,2,3,4,5,6,7].pop(2)
# stack - last in first out ex: can of pringles
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
# implement stack we .pop() > popping last element
stack.pop()

# queues - first in first out: carnival line or waiting list
queues = []
queues.append(1) # O(1)
queues.append(2) # O(1)
queues.append(3) # O(1)

# remove first
queues.pop(0) # O(N)

queues2 = []
queues2.insert(0, 1) # O(N)
queues2.insert(0, 2) # O(N)
queues2.insert(0, 3) # O(N)

# remove first 
queues2.pop(0) # O(1)