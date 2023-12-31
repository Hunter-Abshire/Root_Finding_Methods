from root_bisect import bisection_method_1, bisection_method_2, bisection_method_3
from root_newton import newtons_method_1, newtons_method_2, newtons_method_3
from root_secant import secant_method_1, secant_method_2, secant_method_3

print("True roots for reference:\nEquation 1: -3.183\nEquation 2: 1\nEquation 3: 1\n")
print("-----------------------------------\n")
print("First equation Bisection method:\nX Bounds\n",end = "")
bisection_method_1(-4,-2,0)
print("\nFirst equation Newton's method:\nX-Values              Y-Values\n",end = "")
newtons_method_1(-4,0)
print("\nFirst equation Secant method:\nX-Values              Y-Values\n",end = "")
secant_method_1(-4,-2,0)
print("-----------------------------------\n")
print("Second equation Bisection method:\nX Bounds\n",end = "")
bisection_method_2(-1,2,0)
print("\nSecond equation Newton's method:\nX-Values              Y-Values\n",end = "")
newtons_method_2(2,0)
print("\nSecond equation Secant method:\nX-Values              Y-Values\n",end = "")
secant_method_2(-1,2,0)
print("-----------------------------------\n")
print("Third equation Bisection method:\nX Bounds\n",end = "")
bisection_method_2(-1,2,0)
print("\nThird equation Newton's method:\nX-Values              Y-Values\n",end = "")
newtons_method_2(2,0)
print("\nThird equation Secant method:\nX-Values              Y-Values\n",end = "")
secant_method_2(-1,2,0)
