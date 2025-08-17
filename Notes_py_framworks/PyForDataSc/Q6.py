# Q6. 6. Demonstrate usage of `for`, `if`, `break`, `continue`, and `else` in a loop.

for i in range(10): #0-9
    if i == 3:
        continue
    # if i == 8:
    #     break
    print(i)
else:
    print("Loop ended successfully.")


'''
In Python:

for ...:
    # loop body
else:
    # runs only if loop ends normally (no break)

Yaha else for loop ke saath bind hai (jaise if ke saath hota hai). Isliye chahe indentation se lagta ho ke loop ke baahar hai, asal me ye loop ka ek logical part hai.
'''