A = int(input())
B = int(input())

if A < B:
    for i in range(A,B):
        print(i,end=" ")
else:
    for i in reversed(range(B,A)):
        print(i,end=" ")