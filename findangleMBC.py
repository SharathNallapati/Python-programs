import math
from math import degrees
from math import atan

AB=int(input())
BC=int(input())

print(str(round(degrees(atan((AB / 2) / (BC / 2))))) + "°")
