n = int(input("Enter the Number of Elements: "))

print("Enter Elements of the list")

list1 = []

for i in range(n):
  a = int(input())
  list1.append(a)

list2 = []
for num in list1:
  if num>0:
    list2.append(num)
  else:
    pass
print(f"Output: {list2}")
