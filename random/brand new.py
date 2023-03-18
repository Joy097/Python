rows = int(input())
cols = int(input())

mat = []
for _ in range(rows):
    mat.append([int(x == '1') for x in input().strip().split(' ')])

ones = set()

for row in range(rows):
    for col in range(cols):
        if mat[row][col]:
            ones.add((row, col))

regions = []
while ones:
    n = ones.pop()
    region = [n]
    regions.append(region)
    unchecked = [n]
    while unchecked:
        xr, xc = unchecked.pop()
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                p = (xr + r, xc + c)
                if p in ones:
                    ones.remove(p)
                    region.append(p)
                    unchecked.append(p)
print(max((len(region) for region in regions), default=0))