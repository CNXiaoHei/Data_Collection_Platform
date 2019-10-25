import test_1
import time

test = test_1.Test_one(40,'data1024')
for i in range(2000):
    if i<9:
        pass
    else:
        test.wula()
    time.sleep(0.5)

