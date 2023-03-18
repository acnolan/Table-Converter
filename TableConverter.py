import pandas as pd
import sys
from os import path

fileToConvert = input('Please provide the file you would like to convert!\n')

filename, extension = path.splitext(fileToConvert)

if not extension in ['.csv', '.md', '.html']:
    print('Table must be a csv, md, or html file!')
    sys.exit()

df = pd.DataFrame()

if extension == '.csv':
    df = pd.read_csv(fileToConvert)
if extension == '.html':
    df = pd.read_html(fileToConvert)[0]
if extension == '.md':
    df = pd.read_table(fileToConvert, sep='|', header=0)
    df = df.dropna(axis=1, how='all')
    df = df.drop(axis=0, labels=0)

try:
    if extension != '.md':
        with open(filename + 'convertedToMarkdown.md', 'w') as md:
            df.to_markdown(buf=md, index=False)
    if extension != '.csv':
        df.to_csv(filename + 'convertedToCSV.csv', index=False)
    if extension != '.html':
        with open(filename + 'convertedToHTML.html', 'w') as html:
            df.to_html(buf=html, index=False)
except Exception as e:
    print('Something went horribly, terribly wrong! :\'^(\nPlease check your input file is a valid table.')
    print(e)


