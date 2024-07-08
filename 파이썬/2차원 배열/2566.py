import sys
input = sys.stdin.readline

total_max_value = 0
row_max_value = 0

for i in range(9):
    cell = list(map(int, input().split()))
    row_max_value = max(cell)
    if total_max_value <= row_max_value:
            total_max_value = row_max_value
            row = i + 1
            column = cell.index(row_max_value) + 1

print(total_max_value)
print(row, column)