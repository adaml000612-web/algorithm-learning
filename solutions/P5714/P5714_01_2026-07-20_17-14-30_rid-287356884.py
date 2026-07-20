m,h =input().split()
m = float(m)
h = float(h)
x = m/h**2
if x<18.5:
    print( "Underweight")
elif 18.5<=x<24:
    print( "Normal")
else:
    print(f"{x:.6g}")
    print("Overweight")
