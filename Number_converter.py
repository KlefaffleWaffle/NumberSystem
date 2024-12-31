
number_2_convert = int(input('Please input a number \n'))


def decimal_to_binary(number_2_convert):

    x = 0
    while number_2_convert > pow(2,x) :
        x+=1
        

    print (x)
    x-=1;
    for i in range(x, -1, -1):
        if number_2_convert >= pow(2,i):
            print ('1', end= " ")
            number_2_convert -= pow(2,i)  
        else:
            print ('0', end= " ")
          
        print('\t' + str(pow(2,i)) + '\t' + str(number_2_convert))

def d2b(number_2_convert):

    x = 0
    while number_2_convert > pow(2,x) :
        x+=1
        

    #print (x)
    x-=1;
    for i in range(x, -1, -1):
        if number_2_convert >= pow(2,i):
            rInt = int(number_2_convert/(pow(2,i)))
            rStr = str(rInt)
      


            print (rStr + ',', end= " ")
            number_2_convert -= rInt*(pow(2,i))  
        else:
            
            print ('0,', end= " ")
          
        #print('\t' + str(pow(2,i)) + '\t' + str(number_2_convert))
    print('')


def d2h(number_2_convert):

    x = 0
    while number_2_convert > pow(16,x) :
        x+=1
        

    #print (x)
    x-=1;
    for i in range(x, -1, -1):
        if number_2_convert >= pow(16,i):
            rInt = int(number_2_convert/(pow(16,i)))
            rStr = str(rInt)
            if rInt == 10:
                rStr = 'A'
            elif rInt == 11:
                rStr = 'B'
            elif rInt == 12:
                rStr = 'C'
            elif rInt == 13:
                rStr = 'D'
            elif rInt == 14:
                rStr = 'E'
            elif rInt == 15:
                rStr = 'F'


            print (rStr + ',', end= " ")
            number_2_convert -= rInt*(pow(16,i))  
        else:
            
            print ('0,', end= " ")
          
        #print('\t' + str(pow(2,i)) + '\t' + str(number_2_convert))
    print('')

print('')

print ('Your number in binary is:');
d2b(number_2_convert)

print('')

print ('Your number in hexadecimal is:');
d2h(number_2_convert)

print ('')


"""
for i in range(0, 16, +1):
    d2h(i);
    print('');

"""