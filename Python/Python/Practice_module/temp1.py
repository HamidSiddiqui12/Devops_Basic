s = "abc;def;ghi"

for i in range(len(s)):
    if s[i] == ";":
        print(s[i+1])
        print(s[i], s[i+1], "\n")
        continue
    elif s[i] != ";":
        continue
    else:
        print("No semicolon found")


result1 = s.find(";")
result2 = s.rfind(";")

print(s[result1+1:result2])  #slicingg 

#for i in range(result1+1, result2):
#    print(s[i], end =" ")  # This keeps them on one line

#print() # Optional: Adds a newline at the very end so the next prompt isn't on the same line


#~Practice Question
#~ Input --> [1,2,3,4,5,6,7,8,9,10]
#~ Output --> [[1,2],[3,4],[5,6],[7,8],[9,10]]