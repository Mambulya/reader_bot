import pandas as pd
# import openpyxl  - - - for FutureWarning
""" 
--------------------------------
    CREATING A DATA FRAME
--------------------------------

words = {
    'words': ['derive', 'data frame'],
    'PHRASAL VERBS': ['be frown up', '-']
}
dataFrame = pd.DataFrame(words, columns = ['words', 'PHRASAL VERBS'])

print(dataFrame)


---------------------------------------------
    CREATING A DATA FRAME FROM EXCEL FILE
---------------------------------------------


words = pd.read_excel(r'benefitsEng.xlsx')
df = pd.DataFrame(words, columns = ['word', 'phrasal verb'])

print (df)
"""