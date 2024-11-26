from typing import List

def solve(grid: List[List[int]], rules: List[dict]) -> List[List[int]]:
    map_rule = {tuple(rule["pattern"]): rule["result"] for rule in rules}
    res = []
    n = len(grid)

    for y in range(n - 1):
        row = []
        for x in range(n - 1):
            sub_sqare = [
                grid[y][x], grid[y][x+1], grid[y+1][x], grid[y+1][x+1]
            ]
            row.append(map_rule.get(tuple(sub_sqare), 0))
        res.append(row)
    return res


if __name__ == "__main__":
    grid = [
        [1, 1, 1],
        [1, 1, 4],
        [1, 4, 6]
    ]
    rules = [
        {"pattern": [1, 1, 1, 1], "result": 5},
        {"pattern": [1, 1, 1, 4], "result": 6},
    ]

    # 输出结果应该是 [[5, 6], [6, 0]]
    print(solve(grid, rules))
