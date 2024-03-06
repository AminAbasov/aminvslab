s=0
z1=1
z=1
i=1
eps=0.01
while z>eps:
    z1=z1*i  
    z=1/z1
    s=s+z
    i=i+1
    print(s)
