s = input().split()
for word in s:
    rev = ""
    for ch in word:
        rev = ch + rev
    print(rev, end=" ")    
    

    