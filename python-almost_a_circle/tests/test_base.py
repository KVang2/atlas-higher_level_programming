"""

import unittest
from models.base import Base

if __name__ == "__main__":

b1 = Base()
print(b1.id)

b2 = Base()
print(b2.id)

b3 = Base(32)
print(b3.id)

b4 = Base(45)
print(b4.id)
"""