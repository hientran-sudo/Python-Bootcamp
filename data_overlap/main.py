# data overlap
# hard level
with open("file1.txt") as file1:
    list1 = file1.readlines()

list_comprehensive_1 = []
for line in list1:
    list_comprehensive_1.append(int(line.strip()))

with open("file2.txt") as file2:
    list2 = file2.readlines()

list_comprehensive_2 = []
for line in list2:
    list_comprehensive_2.append(int(line.strip()))

result = [n for n in list_comprehensive_1 if n in list_comprehensive_2]
print(result)
