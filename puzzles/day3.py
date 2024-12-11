import math
from pathlib import Path
import re

file_path = Path("inputs/input3.txt")

# day3 part1

# if file_path.exists():
#     with open(file_path, 'r') as file:
#         content = file.read()
#         # Remove newlines
#         content = content.replace("\n", " ")
#         # Regular expression to match mul(x,y)
#         pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
#         matches = re.findall(pattern, content)
#         # Convert to tuples of integers
#         mul_pairs = [(int(x), int(y)) for x, y in matches]
#         # Calculate the sum of products
#         result = sum(x * y for x, y in mul_pairs)  
#         print(result)

# else:
#     print(f"File not found: {file_path.resolve()}")

# day3 part2
if file_path.exists():
    with open(file_path, 'r') as file:
        content = file.read()
        # Remove newlines
        content = content.replace("\n", " ")
        # Regular expression to match mul(x,y)
        pattern = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
        matches = re.findall(pattern, content)

else:
    print(f"File not found: {file_path.resolve()}")

ans = 0
is_enabled = True
for match in matches:
    if match == "do()":
        is_enabled = True
    elif match == "don't()":
        is_enabled = False
    else:
        if is_enabled:
            pair = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", match)
            x, y = pair[0]
            ans += int(x)*int(y)

print(ans)