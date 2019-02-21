# Change path to your data dir
data_dir = './'

import json
import re
import locale
import os
import sys

import spacy

# OLDP deps
from utils import preprocessing
from refex.extractor import RefExtractor

# local deps
import wordSim

law_extractor = RefExtractor()
law_extractor.do_law_refs = True
law_extractor.do_case_refs = False


case_extractor = RefExtractor()
case_extractor.do_law_refs = False
case_extractor.do_case_refs = True

lit_pattern = re.compile('(NJW|MDR)\s?([0-9]{2,4})')

# Load model
model_path = os.path.join(data_dir, 'autocom_model')
nlp = spacy.load(model_path)
predict_label = 'POSITIVE'


# Load cases from dump file (alternatively we could get cases from API: search for "Streitwert")
file_path = os.path.join(data_dir, 'courtDecisionsPreprocessed.json')
n = 10000

book = 'BGB'
number = '439'

sents = []
sents_dict = {}
out = []

count = 0
with open(file_path, 'r') as f:
    for case_json in [next(f) for x in range(n)]:  # Read line-by-line the first n lines (one case per line)
        case = json.loads(case_json)  # Parse JSON
        has_score = False
        
        for fs_i, fs in enumerate(case['fundstellen']):  # Iterate over citations
        #for fs in case['fundstellen']:  # Iterate over citations
            count += 1
            if 'gesetze' in fs:
                for g in fs['gesetze']:
                    # Test if it refers to the requested law
                    if 'book' in g and 'number' in g and g['book'] == book and g['number'] == number:
                        sent = fs['sentencesRechtssatz']
                        
                        if sent in sents_dict:
                            continue
                        else:
                            sents_dict[sent] = 1
                        
                        _, case_markers = case_extractor.extract(sent)
                        _, law_markers = law_extractor.extract(sent)
                        
                        law_cits = [[r for r in m.references] for m in law_markers]
                        lit_cits = lit_pattern.findall(sent)
                        print(wordSim.staticmethod(count))
                        pos = case['text'].find(sent)
                        case_length = len(case['text'])
                        rel_pos = pos / case_length
                        law_cit_count =  min(len(law_cits) - 1, 0)  # Do not count itself
                        
                        sent_data = {
                            'case_cit_count': len(case_markers), 
                            'law_cit_count': law_cit_count,
                            'lit_cit_count': len(lit_cits),
                            'pos': pos, 
                            'rel_pos': rel_pos,
                            'case_length': case_length,
                            'score': law_cit_count,
                            'text': sent,
                            'cat': nlp(sent).cats[predict_label]
                        }
                        
                        sents.append(sent_data)
                        
                        case['fundstellen'][fs_i]['rank_score'] = sent_data['score']
                        
                        has_score = True
        if has_score:
            out.append(json.dumps(case))
            
        #print('###########')
    
 
        
print('processing done')

with open(os.path.join(data_dir, 'cases_with_scores.jsonl'), 'w') as f:
    f.write('\n'.join(out))
    
print('writing done')
