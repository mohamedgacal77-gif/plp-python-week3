count = 1
total = 0

# BUG: Added a colon after the while condition to fix the syntax error.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Changed the output to use an f-string because total is an integer.
print(f"Sum of 1 to 5 is: {total}")