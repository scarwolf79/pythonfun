#!/usr/bin/python

import math

for a in range(10, 100):
    print('{0}'.format(a), end="")
    for bigb in range(0, 10):
        try:
            intermcalcval=a+(bigb/10)
            calcval=intermcalcval/10
            loga=math.log10(calcval)
            print('{0:16.6f}'.format(loga), end="" )
        except:
            print('{0:16}'.format("   ---"), end="" )
    print("")
        


