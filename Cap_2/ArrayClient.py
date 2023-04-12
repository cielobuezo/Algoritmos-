import Array
maxSize = 10 # Max size of the array
arr = Array.Array(maxSize) # Create an array object

arr.insert(77) # Insert 10 items
arr.insert(99)
arr.insert(89)
arr.insert("none")
arr.insert(44)
arr.insert(44)
arr.insert(12.34)
arr.insert(44)
arr.insert(67)
arr.insert(-17)



print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()

#2.1
print("Maximum array value", arr.getMaxNum())
arr.traverse()

print("Array before deleting maximun value")
arr.traverse()
#2.2
deleted = arr.deleteMaxNum()

if deleted:
    print("Maximun value deleted")
else:
    print("No maximun value found")
    
print("Array after deleting maximum value")
arr.traverse()

#Excercise 2.3
#bubble sort
for passnum in range (len(arr)-1,0,-1):
    for i in range(passnum):
        if arr.get(i) > arr.get(i + 1):
            temp = arr.get(i)
            arr.set(i, arr.get(i+1))
            arr.set(i+1, temp)
            
#print sorted 
print("Sorted Array:")
arr.traverse()
#2.4
print("removeDupes",arr.removeDupes())
arr.traverse()



