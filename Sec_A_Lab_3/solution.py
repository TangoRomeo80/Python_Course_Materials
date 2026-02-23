def solve():
    n = int(input())
    tokens = input().strip().split()
    # tokens = [int(x) for x in tokens]

    total = 0
    multi = 0
    mx = 0

    for i in range(n):
        p = int(tokens[i])
        # t = (p + 9) // 10
        t = p // 10 + (1 if p % 10 > 0 else 0)
        total += t
        if t > 1:
            multi += 1
        if t > mx:
            mx = t
    
    print(total, multi, mx)

if __name__ == "__main__":
    solve()
