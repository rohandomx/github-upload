print('Initializing...')

import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook, load_workbook
import sqlite3


conn = sqlite3.connect('JEP_many-to-many.sqlite3')
cur = conn.cursor()

list_of_boxes = list(['box_1292.xlsx', 'box_1293.xlsx']) #edit with range of spreadsheets
print('Processed sheets:')

for file_name in list_of_boxes : 
    wb = load_workbook(file_name)
    for sheet in wb.worksheets :
        df = pd.read_excel(file_name, sheet_name=sheet.title)
        print(sheet.title)
        #print(df)
        #print(type(df['Autor']))
        for index, row in df.iterrows():
            author = row['Autor']
            folder = row['Folder']
            count =  row['Cantidad']
            #print(folder)
            #print(author, folder, count)  
            #wb.save('Reporte.xlsx')

            cur.execute('''INSERT OR IGNORE INTO Author (name) 
                VALUES ( ? )''', (author, ))
            cur.execute('SELECT id FROM Author WHERE name = ?', (author, ))
            author_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Folder (name)
                VALUES ( ? )''', (folder, ))
            cur.execute('SELECT id FROM Folder WHERE name = ?', (folder, ))   
            folder_id = cur.fetchone()[0]

            cur.execute('''INSERT INTO Distribution (author_id, folder_id, count) 
                VALUES ( ?, ?, ? )''',
                ( author_id, folder_id, count ))

    conn.commit()

print('Complete!')
