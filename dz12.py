def writeFile(x):

    with open('calc.txt', mode='a', encoding='utf-8') as log_file1:
        log_file1.write(x+ '\n')
