# https://github.com/lex8erna/UPGMApy/blob/master/UPGMA.py
from utils import *

# lowest_cell:
def lowest_cell(table):
    min_cell = float("inf")
    x, y = -1, -1

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_cell:
                min_cell = table[i][j]
                x, y = i, j

    return x, y

# join_labels:
def join_labels(labels, a, b):
    if b < a:
        a, b = b, a

    labels[a] = "[" + labels[a] + "," + labels[b] + "]"
    del labels[b]


# join_table:
def join_table(table, a, b):
    if b < a:
        a, b = b, a

    row = []
    for i in range(0, a):
        row.append((table[a][i] + table[b][i])/2)
    table[a] = row
    
    for i in range(a+1, b):
        table[i][a] = (table[i][a]+table[b][i])/2
        
    for i in range(b+1, len(table)):
        table[i][a] = (table[i][a]+table[i][b])/2
        del table[i][b]

    del table[b]


# UPGMA full algo
def UPGMA(table, labels):
    labels = ['\'' + l + '\'' for l in labels]
    while len(labels) > 1:
        x, y = lowest_cell(table)

        join_table(table, x, y)
        join_labels(labels, x, y)

    # Return the final label
    return labels[0]


# alpha_labels:
def alpha_labels(start, end):
    labels = []
    for i in range(ord(start), ord(end)+1):
        labels.append(chr(i))
    return labels

def get_clusters_assign(str_list, num_clust, dendro=None):
    out = un_nest(UPGMA(get_diagonal_mat(str_list), str_list))
    return cut_tree_at_lv(get_linkage_mat(str_list), numclust=num_clust, upgma_out=out)

# Test table data and corresponding labels
M_labels = alpha_labels("A", "G")   #A through G
M = [
    [],                         #A
    [19],                       #B
    [27, 31],                   #C
    [8, 18, 26],                #D
    [33, 36, 41, 31],           #E
    [18, 1, 32, 17, 35],        #F
    [13, 13, 29, 14, 28, 12]    #G
    ]
print(un_nest(UPGMA(M, M_labels)))

test_list = [
 "Acquiesce.",
"Acronym.",
"Ambiguity.",
"Analogy.",
"Anachronism.",
"Andragogy.",
"Antithesis.",
"Antonym.",
]

print(un_nest(UPGMA(get_diagonal_mat(test_list), test_list)))
print(cut_tree_at_lv(get_linkage_mat(test_list), numclust=5))
# UPGMA(M, M_labels) should output: '((((A,D),((B,F),G)),C),E)'