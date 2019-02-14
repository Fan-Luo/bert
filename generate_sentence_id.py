import numpy as np
import string, random
from collections import Counter
import getopt, sys
import pickle 
import datetime
import math


def sentence_id_pid(input_file, output_file):

# with open('sentence-id_pid.txt', 'w') as output1:
#     with open('../UDS_IH2_unified/train.conll', 'r') as f:
    with open(output_file, 'w') as output:
        with open(input_file, 'r') as f:

            data = f.read()
            sentences = data.split('\n\n')

            example_words = []
            example_predicates = []

            #enumerate every sentence
            for l, sentence in enumerate(sentences):    
                lines = sentence.split('\n')
                
                sent_words = []
                pred_ids = []

                #enumerate every word in a sentence
                for line in lines:
                    line = line.strip('\n') 

                    if(len(line.split('\t')) >= 3):   # avoid empty line
                        word = line.split('\t')[1].lower()
                        sent_words.append(word)
                   
                        if(line.split('\t')[2] != '_'): # a socred predicate
                            pred_id = int(line.split('\t')[0])
                            pred_ids.append(pred_id)
 
                # for every socred predicate, store the sentence
                for pred_id in pred_ids:
                    output.write("%s\t%s\n" % (str(l),str(pred_id + 1)))

sentence_id_pid('../UDS_IH2_unified/train.conll', 'train_sentence-id_pid.txt')
sentence_id_pid('../UDS_IH2_unified/dev.conll', 'dev_sentence-id_pid.txt')
sentence_id_pid('../UDS_IH2_unified/train.conll', 'test_sentence-id_pid.txt')

 