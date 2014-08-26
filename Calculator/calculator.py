while True:
    print('\n\n\n\n1:Add\n2:Subtract\n3:Multiply\n4:Divide\n5:Exponent\nQuit:9')
    answer = input('What is your choice: ')
    if answer=='9':
        break
    elif answer=='1':
        a = int(input('First value: '))
        b = int(input('Second value: '))
        print ('*****************\nAnswer: ', int(a+b))
        
    elif answer=='2':
        a = int(input('First value: '))
        b = int(input('Second value: '))
        print ('*****************\nAnswer: ', int(a-b))
        
    elif answer=='3':
        a = int(input('First value: '))
        b = int(input('Second value: '))
        print ('*****************\nAnswer: ', int(a*b))
        
    elif answer=='4':
        a = int(input('First value: '))
        b = int(input('Second value: '))
        print ('*****************\nAnswer: ', int(a/b))

    elif answer=='5':
        a = int(input('Base: '))
        b = int(input('Power: '))
        print ('*****************\nAnswer: ', int(a**b))   
        
    
