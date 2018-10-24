import ctypes as C
mylib = C.CDLL('./libmylib.so')

mylib.add_float.restype = C.c_float
mylib.add_float.argtypes = [C.c_float, C.c_float]

float1 = float(input("Enter a number:"))
float2 = float(input("Enter another number:"))

print(mylib.add_float(float1, float2))

mylib.add_int.restype = C.c_int
mylib.add_int.argtypes = [C.c_int, C.c_int]

int1 = int(input("Enter a number:"))
int2 = int(input("Enter another number:"))

print(mylib.add_int(int1, int2))

cinco_float = C.c_float(5)
seis_float = C.c_float(6)
res_float = C.c_float()
cinco_int = C.c_int(5)
seis_int = C.c_int(6)
res_int = C.c_int()

mylib.add_float_ref(C.byref(cinco_float),
                    C.byref(seis_float),
                    C.byref(res_float))
print(res_float.value)

mylib.add_int_ref(C.byref(cinco_int),
                  C.byref(seis_int),
                  C.byref(res_int))
print(res_int.value)

in1 = (C.c_int * 3) (2, 4, -2)
in2 = (C.c_int * 3) (3, -1, -2)
out = (C.c_int * 3) ()
mylib.add_int_array(C.byref(in1),
                    C.byref(in2),
                    C.byref(out),
                    3)
print(out[0], out[1], out[2])

flin1 = (C.c_float * 3) (2.0, 1.5, 3.2)
flin2 = (C.c_float * 3) (1.5, -3.0, 0.5)
flout = C.c_float()

print(mylib.dot_product(C.byref(flin1), C.byref(flin2), 3))