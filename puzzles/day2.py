import math
from pathlib import Path

file_path = Path("inputs/input2.txt")

reports = []
if file_path.exists():
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            reports.append(report)
else:
    print(f"File not found: {file_path.resolve()}")

# print("Reports: ", reports)

# day2 part1

# def is_all_increasing(report):
#     for i in range(len(report)-1):
#         if report[i] > report[i+1]:
#             return False
#     return True

# def is_all_decreasing(report):
#     for i in range(len(report)-1):
#         if report[i] < report[i+1]:
#             return False
#     return True

# def is_all_increasing_or_decreasing(report):
#     return is_all_increasing(report) or is_all_decreasing(report) 

# def is_diff_good(report):
#     for i in range(len(report)-1):
#         diff = abs(report[i]-report[i+1])
#         if diff < 1 or diff > 3:
#             return False
#     return True

# def is_safe(report):
#     return is_all_increasing_or_decreasing(report) and is_diff_good(report)


# rewrite to avoid iterating over the reports list multiple times
def is_safe(report):
    # Check if the report is either strictly increasing or decreasing
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    # Check if differences between adjacent levels are within range
    valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    # A report is safe if it meets both conditions
    return (increasing or decreasing) and valid_differences

# # count safe reports
# safe_count = 0
# for report in reports:
#     if is_safe(report):
#         safe_count += 1

# day2 part2
def is_safe_with_dampener(report):
    # check if the report is already safe
    if is_safe(report):
        return True

    # Check if removing one level makes it safe
    for i in range(len(report)):
        # create a modified report with the i-th level removed
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    # if no single-level removal makes it safe, return False
    return False

# count safe reports
safe_count = 0
for report in reports:
    if is_safe_with_dampener(report):
        safe_count += 1

print(safe_count)