def main():
    i=0
    while i<99:
       
        if i<=9:
           print(f'[{i}]',end=(' '))
        elif i>9:
            i=str(i)
            sum1=int(int(i[0])+int(i[1]))
            print(f'[{i} {sum1}]',end=(' '))
            if sum1>9:
                sum2=str(sum1)
                sum2=int(int(sum1[0])+int(sum1[1]))
                print(f'[{i}{sum1}{sum2}],',end=(' '))
        i=i+1

main()

              
