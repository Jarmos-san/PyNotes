'''
Run demorandom.py. Run the demorandom.py script several times and save the results. 
Then add the following statement to the script and run it again several times. 
What happens when we add an explicit seed?

#!/usr/bin/env python
import random
random.seed(1)
# Simple Range 0 <= r < 6
print(random.randrange(6), random.randrange(6))
# More complex range 1 <= r < 7
print(random.randrange(1,7), random.randrange(1,7))
# Really complex range of even numbers between 2 and 36
print(random.randrange(2,37,2))
# Odd numbers from 1 to 35
print(random.randrange(1,36,2))

Try the following variation and see what happens.

#!/usr/bin/env python
import random
random.seed(time.clock())
# Simple Range 0 <= r < 6
print(random.randrange(6), random.randrange(6))
# More complex range 1 <= r < 7
print(random.randrange(1,7), random.randrange(1,7))
# Really complex range of even numbers between 2 and 36
print(random.randrange(2,37,2))
# Odd numbers from 1 to 35
print(random.randrange(1,36,2))
'''

#First variation
import random
import time

random.seed(1)
# Simple Range 0 <= r < 6
print(random.randrange(6), random.randrange(6))
# More complex range 1 <= r < 7
print(random.randrange(1,7), random.randrange(1,7))
# Really complex range of even numbers between 2 and 36
print(random.randrange(2,37,2))
# Odd numbers from 1 to 35
print(random.randrange(1,36,2))

print()#Blank line

#Second variation
random.seed(time.clock())
# Simple Range 0 <= r < 6
print(random.randrange(6), random.randrange(6))
# More complex range 1 <= r < 7
print(random.randrange(1,7), random.randrange(1,7))
# Really complex range of even numbers between 2 and 36
print(random.randrange(2,37,2))
# Odd numbers from 1 to 35
print(random.randrange(1,36,2))