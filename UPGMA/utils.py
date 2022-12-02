import sys, re
import numpy as np

def load_fasta(fnam, as_list=True):
    f=open(fnam,'r')
    lines=f.readlines()

    hre=re.compile('>(\S+)')
    lre=re.compile('^(\S+)$')
    gene={}
    for line in lines:
            outh = hre.search(line)
            if outh:
                    id=outh.group(1)
            else:
                    outl=lre.search(line)
                    if(id in gene.keys()):
                            gene[id] += outl.group(1)
                    else:
                            gene[id]  =outl.group(1)
    if as_list:
        return gene.keys(), gene.values()

    return gene

def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

def get_diagonal_mat(seq_list):
    List1, List2 = seq_list, seq_list
    Matrix = np.zeros((len(List1),len(List2)),dtype=np.int)
    mat = []

    for i in range(0,len(List1)):
        temp = []
        for j in range(i,len(List2)):
            temp.append(minimumEditDistance(List1[i],List2[j]))
        mat.append(temp)

    mat.reverse()
    mat[0] = []
    return mat

def content_by_level(str1, l=0):
    level_dict = {}
    level = 0
    level_char = ''
    for s in str1:
        if s == '(':
            if level not in level_dict:
                level_dict[level] = [level_char]
            elif level_char != '':
                level_dict[level].append(level_char)
            level_char = ''
            level += 1
        elif s == ')':
            if level not in level_dict:
                level_dict[level] = [level_char]
            elif level_char != '':
                level_dict[level].append(level_char)
            level_char = ''
            level -= 1
        else:
            level_char += s
    
    print(level_dict) # {0: [''], 1: ['a', 'hi'], 2: ['b', 'd', 'e', 'g'], 3: ['c', 'f']}
    return level_dict[l]

def un_nest(s):
    s = eval(s)
    return s