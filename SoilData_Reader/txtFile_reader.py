# author : Thalakotunage A.H.
# author_email : thalakotunage@gmail.com

import glob
import os
os.chdir(r'C:\Users\athalako\PycharmProjects\Data')
dataFiles = glob.glob('*.txt')
outputFiles = [name[:-4] + '_edited.txt' for name in dataFiles]

for infile, outfile in zip(dataFiles, outputFiles):
    with open(infile, 'r', encoding='utf-8') as dataFile, open(os.path.join(
            r'C:\Users\athalako\PycharmProjects\Outfile',outfile), 'w', encoding='utf-8') as output:
        input = dataFile.readlines()
        for i in range(4):
            output.write(input[i])
        output.write(input[len(input) - 1])
