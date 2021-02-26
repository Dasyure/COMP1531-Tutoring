### Original ###
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for idx in range(len(x)):
  if x[idx] % 2 == 0:
    result.append(x[idx] * 2)
  else:
    result.append(x[idx])

print(result)

'''
Issues:
- Spacing inconsistent
- Indentation not 4 spaces (refer to style guide on webcms3)
- Could use for-range loop in this case
- range(len(x)) is redundant, could just use range normally
'''
### Improved upon code ###
result = []

for num in range(1, 11):
  if num % 2 == 0:
    result.append(num * 2)
  else:
    result.append(num)

print(result)

### List-comphrension ###
# https://www.programiz.com/python-programming/list-comprehension
my_list = [(element * 2 if element % 2 == 0 else element) for element in range(1,11)]
print(my_list)
