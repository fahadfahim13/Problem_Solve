import heapq as hq
def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    sol_map = []
    for i in range(len(mat)):
        c = 0
        for num in mat[i]:
            c += num
        sol_map.append((c, i))
    hq.heapify(sol_map)
    ans = []
    for i in range(k):
        temp = hq.heappop(sol_map)
        ans.append(temp[1])
    return ans


def main():
    mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
    k = 3
    print(kWeakestRows(mat,k))


if __name__ == '__main__':
    main()

