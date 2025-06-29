# https://www.geeksforgeeks.org/program-to-print-multiplication-table-of-a-number/

def printTable(n):
    for i in range (1, 11): 
        print ("%d * %d = %d" % (n, i, n * i))

printTable(8)
