mi_set = set([1,2,(1,2,3),3,4,5])
print(type(mi_set))
print(2 in mi_set)


otro_set = {1,2,3,4}
print(type(otro_set))
print(4 in otro_set)

s1 = {'carlos','mateo','sasha'}
s2 = {'mateo','isis','tony'}
s3 = s1.union(s2)
print(s3)

s3 = {1,2,3}
s3.add(4)
s3.remove(2)
s3.discard(5)
s3.pop()

print(s3)
