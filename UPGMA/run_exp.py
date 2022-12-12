from utils import *
from upgma import *
import time

# flags
timing=True
required_similarity=[0.85, 0.9, 0.95]
fasta_path='./data/60x50.fas'
as_list=True
numclust=50


def main():
    tag, seqs = load_fasta(fasta_path)
    tag, seqs = list(tag), list(seqs)
    start = time.time()
    tree_out = un_nest(UPGMA(get_diagonal_mat(seqs), seqs))
    assn = cut_tree_at_lv(get_linkage_mat(seqs), numclust=numclust)
    end = time.time()
    elapsed_t = end-start

    get_similarity(tag, assn)
    print(elapsed_t)




if __name__ == "__main__":
    main()