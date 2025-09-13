x = int(input())
z = int(input())
x_2 = 34
z_2= 220 
x_3 = 0
z_3 = 0
x_4 = 140
z_4 = 456
H = float(((x-x_2)**2 + (z-z_2)**2)**(1/2))
K= float(((x-x_3)**2 + (z-z_3)**2)**(1/2))
S= float((((x-x_4)**2 + (z-z_4)**2)**(1/2)))
print("Distancia para Hogsmeade:", "{:.2f}".format(H))
print("Distancia para Kakariko:", "{:.2f}".format(K))
print("Distancia para Solitude:", "{:.2f}".format(S))