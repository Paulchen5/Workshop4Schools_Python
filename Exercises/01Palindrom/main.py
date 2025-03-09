def palindrom(s1: str):
    return s1.lower().replace(" ", "") == s1.lower().replace(" ", "")[::-1]


# -------------------
#    Tests:
# -------------------
import os
import sys
import inspect

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe()))
)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import testing

print("TESTS:")
testNum = 1
testNum = testing.testFunction(palindrom, testNum, False, "")
testNum = testing.testFunction(palindrom, testNum, True, "aA")
testNum = testing.testFunction(palindrom, testNum, False, "Busfahrt")
testNum = testing.testFunction(palindrom, testNum, True, "Rentner")
testNum = testing.testFunction(palindrom, testNum, True, "Amok Oma")
testNum = testing.testFunction(palindrom, testNum, True, "Ein Esel lese nie")
