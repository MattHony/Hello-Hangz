def ShowMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d的最大公约数为%d'%(num,count))


            count -= 1
            break

        else:
            print('%d是一个素数'%num)
            #break

num = int(input('请输入一个正整数：'))
# if :
#     input('please再次输入：')
ShowMaxFactor(num)


