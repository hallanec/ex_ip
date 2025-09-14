A = int(input())
L = int(input())
P = int(input())
H = int(input())

hora_a= A*H
hora_l= L*H
hora_p= P*H

media_al = (hora_a + hora_l + abs(( hora_a - hora_l))) / 2
maior= (media_al+ hora_p + abs((media_al - hora_p))) / 2
print(maior)