tuple=(4,7,9,2,5,10,11)
k=2
val=[]
sort_tuple=sorted(list(tuple))
for i in range(k):
  val.append(sort_tuple[i])
for i in range(len(tuple)-k,len(tuple)):
  val.append(sort_tuple[i])
print("Minimum and Maximum k elements in tuple is: ",val)