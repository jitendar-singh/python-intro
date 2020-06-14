# # list / tuples : allow us to work with sequential data
# list uses []
# set uses () -- immutable cannot insert or delete
# # set : Values that are un-ordered & non-duplicate 

courese = ["History","Math","Physics","Comp Sc"]

print(len(courese))
print(courese)
print(courese[2])
print(courese[-1::-2])
# print((courese[2:-3:]))

courese.append("Art")

print(courese)

courese.insert(0,"Art")
print(courese)
courese.remove("Math")
print(courese)
pitem = courese.pop()
print(pitem)
print(courese)

courese.reverse()
print(courese)


