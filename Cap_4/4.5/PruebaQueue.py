import PriorityQueue 

q = PriorityQueue()

q.insert("a", 3)
q.insert("b", 2)
q.insert("c", 1)

print("PriorityQueue",q)
print("peek",q.peek())
print("Remove",q.remove())
print("PriorityQueue", q)
print("it is empty",q.isEmpty())
print("len",len(q))

q.insert("d",2)
q.insert("e",1)
q.insert("f",3)

print("PriorityQueue:", q)
print("Remove",q.remove())
print("PriorityQueue:", q)


