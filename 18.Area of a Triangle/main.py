# Calculate Area of a Triangle with 3 sides length
# Formula: square root of s·(s-a)·(s-b)·(s-c), where s = semi-perimeter


# USE:
# 1. User_input
# 2. Functions
# 3. f-string

import math
def calc_area(sidea, sideb, sidec):
    if ((sidea + sideb) <= sidec) or ((sideb + sidec) <= sidea) or ((sidea + sidec) <= sideb):
     print(f"{sidea} {sideb} {sidec} can't make a triangle")
    else:
     semi_perimeter = (sidea + sideb + sidec)/2
     area_sq = math.sqrt(semi_perimeter*(semi_perimeter-sidea)*(semi_perimeter-sideb)*(semi_perimeter-sidec))
     print(f"The area is {area_sq}")

sidea = input("Enter length of side1: ")
sideb = input("Enter length of side2: ")
sidec = input("Enter length of side3: ")

int_sidea = int(sidea)
int_sideb = int(sideb)
int_sidec = int(sidec)

calc_area(int_sidea, int_sideb, int_sidec)


