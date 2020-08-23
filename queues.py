class Node:

    def __init__(self, num_of_people, next = None):

        self.num_of_people = num_of_people
        self.next = next

    def get_num_of_people(self):
        return self.num_of_people


    def get_next(self):
        return self.next


    def set_next(self, next):
        self.next = next

class Queue:
    def __init__(self, limit=20, front=None, back=None):
        self.front = front
        self.back = back
        self.limit = limit
        self.length = 0
        self.waiting_time = 0

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.limit

    def peek(self):
        return self.front

    def insert_node(self, number_of_people):

        new_node = Node(number_of_people)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.set_next(new_node)
        self.back = new_node
        self.length += 1
        self.waiting_time += (30 * number_of_people)

    def enqueue(self, num_of_people):
        max_num = 12
        num_of_people = int(num_of_people)

        if self.is_full():
            print("Sorry, can you wait? the queue to see the amusement park is full!")
        else:
            if num_of_people > 12:

                while num_of_people > max_num:
                    num_of_people = num_of_people - max_num
                    self.insert_node(max_num)

            self.insert_node(num_of_people)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            node_to_remove = self.front
            self.front = node_to_remove.get_next()
            self.length -= 1
            self.waiting_time -= 30 * node_to_remove.get_num_of_people()
            return f"The size of the group that went into the ride: {node_to_remove.get_num_of_people()}"


    def get_waiting_time(self):
        if self.waiting_time > 59:
            return f"The waiting time for the queue is: {int(self.waiting_time / 60)} minutes"
        else:
            return f"The waiting time for the queue is: {int(self.waiting_time)} seconds"




visitors = Queue()
print("-"*45)
print(visitors.get_waiting_time())
print("-"*45)

visitors.enqueue(4)
visitors.enqueue(12)
visitors.enqueue(18)
print("-"*45)

print(visitors.get_waiting_time())

print(visitors.dequeue())
print(visitors.get_waiting_time())
print("-"*45)
