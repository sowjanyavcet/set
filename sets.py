normal_set = set(["a", "b","c"]) 


#add
people={"y", "z", "x"}
people.add("u") 
print(people)


#union
people1={"y", "z", "x"}
people2={"a","b","c"}
c=people1|people2
print(c)


people1={"y", "z", "x"}
people2={"a","b","c"}
c=people1.union(people2)
print(c)


#intersection
people1={"y", "z", "x"}
people2={"a","y","c"}
c=people1&people2
print(c)


people1={"y", "z", "x"}
people2={"a","b","y"}
c=people1.intersection(people2)
print(c)



#difference
people1={"y", "z", "x"}
people2={"a","b","y"}
c=people1.difference(people2)
print(c)


people1={"y", "z", "x"}
people2={"a","b","y"}
c=people1-people2
print(c)




set1 = set() 
set2 = set() 
for i in range(1,6): 
    set1.add(i) 
  
for i in range(3,8): 
    set2.add(i) 
  
print("Set1=",set1) 
print("Set2=",set2) 
print("\n") 
set3 = set1 | set2
print("Union of Set1 & Set2: Set3 = ", set3) 
set4 = set1 & set2 
print("Intersection of Set1 & Set2: Set4 = ", set4) 
print("\n") 
if set3 > set4:  
    print("Set3 is superset of Set4") 
elif set3 < set4:  
    print("Set3 is subset of Set4") 
else : 
    print("Set3 is same as Set4") 
  

if set4 < set3: 
    print("Set4 is subset of Set3") 
    print("\n") 
  

set5 = set3 - set4 
print("Elements in Set3 and not in Set4: Set5 = ", set5) 
print("\n") 
  

if set4.isdisjoint(set5): 
    print("Set4 and Set5 have nothing in common\n") 
  

set5.clear() 
  
print("After applying clear on sets Set5: ") 
print("Set5 = ", set5) 
