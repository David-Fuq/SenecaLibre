* Source:     Pyomo MPS Writer
* Format:     Free MPS
*
NAME unknown
OBJSENSE
 MIN
ROWS
 N  x3
 G  c_l_x4_
 G  c_l_x5_
COLUMNS
     x1 x3 1
     x1 c_l_x4_ 1
     x1 c_l_x5_ 3
     x2 x3 1
     x2 c_l_x4_ 2
     x2 c_l_x5_ 1
RHS
     RHS c_l_x4_ 8
     RHS c_l_x5_ 6
BOUNDS
 LO BOUND x1 0
 LO BOUND x2 0
ENDATA
