import math
from collections import Counter
from pathlib import Path

file_path = Path("inputs/input1.txt")

# Initialize two empty lists to store the columns
column1 = []
column2 = []

if file_path.exists():
    # open the file in read mode
    with open(file_path, 'r') as file:
        for line in file:
            # split line into two numbers
            num1, num2 = map(int, line.split())
            # populate the columns
            column1.append(num1)
            column2.append(num2)
else:
    print(f"File not found: {file_path.resolve()}")

# print("Column 1: ", column1)
# print("Column 2: ", column2)

# # day1 part1
# column1.sort()
# column2.sort()

# total = 0
# for i in range(len(column1)):
#     diff = abs(column1[i]-column2[i])
#     total += diff
# print(total)

# day1 part2
count_dict = Counter(column2)

# calculate similarity score
similarity_score = 0
for num1 in column1:
    if num1 in count_dict:
        similarity_score += num1 * count_dict[num1]

print(similarity_score)
