import pandas as pd
import datetime

fold = pd.read_excel('1295_5pr.xlsx')
#print(fold)

dateor = fold['date']
print(dateor)
print('\n')

#fecha 
fecha1 = list()
fecha2 = list()

for index, row in fold.iterrows() :
    dater = str(row['date'])
    #print(len(dater), dater) 
    if len(dater) <= 8 :
        try :
            #daterfor = datetime.strptime(dater, '%d/%m/%y')
            daterfor = datetime.datetime.strptime(dater, '%d/%m/%y').date()
            print(daterfor)
            fecha1.append(daterfor)
            fecha2.append('null')
        except :
            dater = str('nan')
            print('null')
            fecha1.append('null')
            fecha2.append('null')
    else:
        dateor = dater.split(';') # a list with the dates
        lenght = len(dateor) 
        if lenght == 2 : 
            date1 = datetime.datetime.strptime(dateor[0], '%d/%m/%y').date()
            date2 = datetime.datetime.strptime(dateor[1], ' %d/%m/%y').date()
            print(date1, date2)
            fecha1.append(date1)
            fecha2.append(date2)
        else :
            #print(dateor)
            datelist = list()
            for i in range(lenght) :
                dateor2 = dateor[i]
                try :
                    datelis = datetime.datetime.strptime(dateor2, '%d/%m/%y').date()
                    datelist.append(datelis)
                except :
                    datelis1 = datetime.datetime.strptime(dateor2, ' %d/%m/%y').date()
                    datelist.append(datelis1)
                datelist.sort()
            fecha2.append(datelist[1:])
            fecha1.append(datelist[0])
            print(datelist[0], datelist[1:])

print(datelist)
print('\n')
print(fecha1)
print('\n')
print(fecha2)
print('\n')
print(len(fold['date']))
print(len(fecha1))
print(len(fecha2))
#print(fecha2)
fold['date1'] = fecha1
fold['date2'] = fecha2

print(fold)

fold.to_excel('dates.xlsx')



#print(type(dater))

    
