
# File: datetime-example-4.py

import datetime
import time

date1 = "31/12/2015"
date2 = "01/01/2016"

newdate1 = time.strptime(date1, "%d/%m/%Y")
newdate2 = time.strptime(date2, "%d/%m/%Y")
print(newdate1 > newdate2)
print(newdate1 < newdate2)
