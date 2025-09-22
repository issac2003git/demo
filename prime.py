num=int(input('ENter a number:'))

for d in range(2,(num//2)+1):
    if num%d==0:
        print('not prime')
        break
else:
    print('prime')
