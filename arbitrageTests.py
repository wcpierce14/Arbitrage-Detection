"""
Math 260
Project
Spring 2022

arbitrageTests.py
"""

# Import the Currencies class.
from currencies import *

"""
testRates function will test all of the exchange rate examples.
"""
def testRates():
    passed = 0
    print('Testing Exchange Rates 0')
    print()
    c = Currencies(0)
    if not c.arbitrage():
        print('Incorrect result for Exchange Rates 0')
        print()
    else:
        passed += 1
        print('Correct result for Exchange Rates 0')
        print()
    print('------------------------')
    print()
    print('Testing Exchange Rates 1')
    print()
    c = Currencies(1)
    if c.arbitrage():
        print('Incorrect result for Exchange Rates 1')
        print()
    else:
        passed += 1
        print('Correct result for Exchange Rates 1')
        print()
    print('------------------------')
    print()
    print('Testing Exchange Rates 2')
    print()
    c = Currencies(2)
    if not c.arbitrage():
        print('Incorrect result for Exchange Rates 2')
        print()
    else:
        passed += 1
        print('Correct result for Exchange Rates 2')
        print()
    print('------------------------')
    print()
    print('Testing Exchange Rates 3')
    print()
    c = Currencies(3)
    if not c.arbitrage():
        print('Incorrect result for Exchange Rates 3')
        print()
    else:
        passed += 1
        print('Correct result for Exchange Rates 3')
        print()
    print('------------------------')
    print()
    print('Passed %d/4 Tests' % passed)
    return

################################################################################