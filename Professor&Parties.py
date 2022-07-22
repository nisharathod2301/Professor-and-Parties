def PartyType(self, a, n):
    hashset =set()
    for n in a:
        if n in hashset:
            return "BOYS"
        hashset.add(n)
    return "GIRLS"

arr=input("Enter input:")
num=arr.len
PartyType(arr,num)