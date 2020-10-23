def Signed16(x): return (x +2**15) % (2**16) - 2**15
def Signed16u(x): return (x) % (2**16)
def ArithmeticOperation(A, B, ShiftSize, IsAdder, DoSaturate):
    """
    Performs arithmetic operation of either adding or multiplying A and B,
    with right-shift value ShiftSize, and saturation flag DoSaturate.
    """
    A = Signed16(int(A))
    B = Signed16(int(B))
    if IsAdder:
        r = (A+B) >> ShiftSize
    else:
        r = (A*B) >> ShiftSize
    if DoSaturate:
        r = min(max(r, -2**15), 2**15-1)
    else:
        r = Signed16(r)
    return r
    
# main 
part1 = True
# input values
a0 = 1
a1 = -1
x0 = 2
x1 = 1

# multiplier parameters
multiplier_shift = 0
multiplier_isAdder = 0
multiplier_sat = 0

# standard adder parameters
adder_shift = 0
adder_isAdder = 1
adder_sat = 0

if part1:
    # part 1 of the experiment
    # intermediate calculations a0*x0 and a1*x1. FILL IN THE MISSING PARAMETERS
    int0 = ArithmeticOperation(a0, x0, __________, ___________, _________)
    int1 = ArithmeticOperation(a1, x1, __________, ___________, _________)
else:
    # part 2 of the experiment
    int0 = 0x7000
    int1 = 0x2000
# calculate y = a0*x0 + a1*x1. FILL IN THE MISSING PARAMETERS
y = ArithmeticOperation(int0, int1, __________, ___________, _________)

print("int0 = " + str(int0) + " = " + format(Signed16u(int0), "=#06X"))
print("int1 = " + str(int1) + " = " + format(Signed16u(int1), "=#06X"))
print("y = " + str(y) + " = " + format(Signed16u(y), "=#06X"))