nums = []
n = 0

for row in open("input1.txt"):
    r = (row.split("\n"))[0]
    if r.isdigit():
        n += int(r)
    else:
        nums.append(n)
        n = 0

print(max(nums))
nums.sort(reverse = True)
print(sum(nums[0:3]))
