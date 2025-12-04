
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
X = int(input())
found = False
for row in matrix:
    if X in row:
        found = True
        break
if found:
    print("will not take number")
else:
    print("will take number")