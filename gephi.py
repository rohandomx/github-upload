import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook, load_workbook

df_final = pd.read_excel('Reporte.xlsx', sheet_name='Total', usecols='A, B')
limit = 185
df_f = df_final[:limit]

#print(df_f)

d = []
e = 

for row in df_f.itertuples():
    #print(type(row))
    author = getattr(row, 'Autor').split()
    #author = row['Autor'].split()
    #print(author)
    if len(author) == 2 :
        name = author[1]
    elif len(author) == 3 :
        name = ' '.join(author[1:3])
    elif len(author) == 4 :
        name = ' '.join(author[1:4])
    elif len(author) == 5 :
        name = ' '.join(author[2:5])
    else:
        name = author[0]
    #name = author.split().get(1)
    count = getattr(row, 'Cantidad')
    #print(name, count)
    d.append((name, count))
    #d.append((name, ))
    #append.ser(name, count)
    #new = index, name, count
    #print(new)
    #print(type(new))
    #df.append(ser)



#df = pd.DataFrame(columns=[index, name, count])
#print(d)

nodes = pd.DataFrame(d, columns=('label', 'count'))
nodes.insert(0, 'id', range(100, 100 + len(nodes)))
print(nodes)

edges = pd.Dataframe(d, columns=('source', 'weight'))
edges.insert


#nodes.to_csv('nodes.csv', encoding='iso-8859-1', index=False)