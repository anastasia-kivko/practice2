a, b = map(int, input().split('x')) #отверстие
c, d, e = map(int, input().split('x')) #кирпич

if (c <= a and d <= b) or (c <= b and d <= a): #грань c*d
    print('да')
elif (c <= a and e <= b) or (c <= b and e <= a): #грань c*e
    print('да')
elif (d <= a and e <= b) or (d <= b and e <= a): ##грань d*e
    print('да')
else:
    print('нет')