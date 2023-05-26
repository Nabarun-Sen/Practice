"""List is a heterogenous datatype(actually datastructure) in python.
Java Collection Framework.
It is written with comma-separeted values between square bracket.
Syntax: List_variable=[val1,val2,....]
==>List is mutable which means that value of its elements can be changed.
Access values of List : seq=List[start:stop:step]
Example : seq=List[::2] #starting with index 0
          seq=List[1::2]#starting with index 1
==>An error is generated if you try to delete an element from the list that is
not present in the list.
"""
#slice operation to acces list
num_list=[1,2,3,4,5,6,7,8,9]
print("First element in the list is",num_list[0])
print("num_list[2:5]",num_list[2:5])
print("num_list[::2]",num_list[::2])
print("num_list[1:3]",num_list[1:3])
print()
#deletion of element from list
num_list2=[1,2,3,4,5,6,7,8,9]
del num_list2[2]
print(num_list2)
del num_list2
#print(num_list2)
print()
#updation of list
num_list3=[1,2,3,4,5,6,7,8,9]
print("List is:",num_list3)
num_list3[5]=100
print(num_list3)
num_list3.append(200)
print(num_list3)
print()
#insert a list in another list
num_list4=[1,8,9,7,56]
print("Original list:",num_list4)
num_list4[2]=[4,5,6]
print("Updated List :",num_list4)
print()
#nested list : a list within a list
list1=[1,'a',"abc",[2,3,4,5],8,9]
i=0
while i<(len(list1)):
    print("List1[",i,"]=",list1[i])
    i+=1
print()

"""If we want to modify a list and also keep a copy of the original list,
then you should create a separate copy of the list(not just the reference),this
is called Cloning."""
#copy and clone of list
list1=[1,2,3,4,5,6,7,8,9]
list2=list1 #copies of a list using reference aliasing
print("List1=",list1)
print("List2=",list2)#both lists point to the same list
list3=list1[2:6]
print("List3=",list3)#list3 is a clone of list1
print()
"""Operations of lists are :
len(),concatenation,in,not in,max,min,sum,all,any,list,sorted
"""
#all
l1=[0,8,3,4]
print(all(l1))
print(any(l1))
#list keyword
l2=list("Hello")
print(l2)
#sorted
l3=[3,4,1,2,7,8]
l4=sorted(l3)
print(l4)
"""List Methods:
append(),count(),index(),insert(),pop(),remove(),reverse(),sort(),extend()"""
#insert(),remove() and sort() only modify the list ,no return type
num_list=[100,200,300,400]
print(num_list.insert(2,250))
print(num_list)
print()
#sort() method
list1=['1','a',"abc",'2','B',"Def"]
list1.sort()
print(list1)
print()

#delete items using empty list
list=['p','r','o','g','r','a','m']
list[2:5]=[]
print(list)
print()
#stack opeartion in list
stack=[1,2,3,4,8]
print("Original stack:",stack)
stack.append(7)
print("Stack after push operation is:",stack)
stack.pop()
print("Stack after pop operation is:",stack)
last_element_index=len(stack)-1
print("Value obtained after pop operation is :",stack[last_element_index])
print()
#del and pop() methods does the same thing.The only difference is
#that pop()

#list as queue
queue=[1,2,3,4,5,6]
print("Original queue:",queue)
queue.append(7)
print("Queue after insertion operation is:",queue)
queue.pop(0)
print("Stack after pop opeartion is:",queue)
print("Queue after deletion is :",queue)
print("Value obtained after peek operation is :",queue[len(queue)-1])


























