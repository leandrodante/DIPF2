import random
from datetime import datetime
startTimeDocument = datetime.now()
c = [0]*60
i = 0
while  i < 6 :
    sort = random.randint(0,60)
    if c[sort] == 0:
        i =  i + 1
        c[sort] = 1
        print(sort)
print(str(datetime.now() - startTimeDocument))