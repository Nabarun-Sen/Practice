X=[[2,5,4],[1,3,9],[7,6,2]] 
Y=[[1,8,5],[7,3,6],[4,0,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]
for r in result:
    print(r)
print()

#Additional Concept
""" Prepending or Appending Items to a List when any additional items can be
added to the start or end of a list using the + concatenation operator
or the += augmented assignment operator.
"""
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print("Before appending :",a)
a += ['grault', 'garply']
print("After Appending :",a)
print()

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print("Before prepending :",a)
a = [10, 20] + a
print("After prepending :",a)
print()

""" Technically, it isn’t quite correct to say a list must be concatenated
with another list. More precisely, a list must be concatenated with an object
that is iterable. Of course, lists are iterable,so it works to concatenate
a list with another list.

Strings are iterable also.But watch what happens when you concatenate a string
onto a list"""
a = ['foo', 'bar', 'baz', 'qux', 'quux']
print("Before appending with string:",a)
a += 'corge'
print("After Appending with string:",a)

a += ['corge']
print("After Appending with string:",a)
print()

