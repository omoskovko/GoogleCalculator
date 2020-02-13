'''
https://www.python.org/dev/peps/pep-0202/
PEP 202 -- List Comprehensions
PEP:	202
Title:	List Comprehensions
Author:	barry at python.org (Barry Warsaw)
Status:	Final
Type:	Standards Track
Created:	13-Jul-2000
Python-Version:	2.0
Post-History:	
'''

'''
The Proposed Solution

It is proposed to allow conditional construction of list literals using for and if clauses. 
They would nest in the same way for loops and if statements nest now.

Rationale

List comprehensions provide a more concise way to create lists in situations 
where map() and filter() and/or nested loops would currently be used.
'''

#Examples

print([i for i in range(10)])
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([i for i in range(20) if i%2 == 0])
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

nums = [1, 2, 3, 4]
fruit = ["Apples", "Peaches", "Pears", "Bananas"]
print([(i, f) for i in nums for f in fruit])
'''
[(1, 'Apples'), (1, 'Peaches'), (1, 'Pears'), (1, 'Bananas'),
 (2, 'Apples'), (2, 'Peaches'), (2, 'Pears'), (2, 'Bananas'),
 (3, 'Apples'), (3, 'Peaches'), (3, 'Pears'), (3, 'Bananas'),
 (4, 'Apples'), (4, 'Peaches'), (4, 'Pears'), (4, 'Bananas')]
'''
print([(i, f) for i in nums for f in fruit if f[0] == "P"])
'''
[(1, 'Peaches'), (1, 'Pears'),
 (2, 'Peaches'), (2, 'Pears'),
 (3, 'Peaches'), (3, 'Pears'),
 (4, 'Peaches'), (4, 'Pears')]
'''
print([(i, f) for i in nums for f in fruit if f[0] == "P" if i%2 == 1])
#[(1, 'Peaches'), (1, 'Pears'), (3, 'Peaches'), (3, 'Pears')]
print([i for i in zip(nums, fruit) if i[0]%2==0])
#[(2, 'Peaches'), (4, 'Bananas')]

