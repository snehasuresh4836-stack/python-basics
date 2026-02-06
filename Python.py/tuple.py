
t=("apple","orange","mango","grapes")
print("tuple:", t)

print("first element:", t[0])
print("last element:", t[3])

for x in t:
    print("element:", x)

    print("length:", len(t))

    #concatination
    t2=("kiwi","watermelon")
    new_tuple=t+t2
    print("concatinatinated:", new_tuple)

    #repetation
    print("repeated tuple:",t*2)

    


f=input("enter fruit:")
print(f"Is {f} present?", f in t)




