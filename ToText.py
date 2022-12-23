import pandas as pd

data = pd.read_csv(r"C:\Users\28634\Desktop\工作簿5.csv")
with open(r"C:\Users\28634\Downloads\600505.txt", 'a+', encoding='utf8') as f:
    for line in data.values:
        f.write((str(line[0]))+'\t'+(str(line[1]))+'\t'+(str(line[2]))+'\t'+(str(line[3]))+'\t'+
                (str(line[4]))+'\t'+(str(line[5]))+'\t'+(str(line[6]))+'\t'+(str(line[7]))+'\t'+
                (str(line[8]))+'\t'+'\n')