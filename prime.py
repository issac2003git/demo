num=int(input('ENter a number:'))

cnt=0
d=1
while d<=num:
    if num%d==0:
        cnt=cnt+1

    d=d+1
if cnt==2:
    print('prime')
else:
    print('not prime')
