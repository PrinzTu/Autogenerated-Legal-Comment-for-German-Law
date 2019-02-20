import nltk
import re

import json

from nltk.corpus import stopwords
nltk.download('stopwords')


sample_text = "Das Vorabentscheidungsersuchen betrifft die Auslegung von Art. 15 Abs. 1 Buchst. c der Verordnung (EG) Nr. 44/2001 des Rates vom 22. Dezember 2000 über die gerichtliche Zuständigkeit und die Anerkennung und Vollstreckung von Entscheidungen in Zivil‑ und Handelssachen (ABl. 2001, L 12, S. 1) in Verbindung mit Art. 16 Abs. 1 der Verordnung."


de_stops = set(stopwords.words('german'))
punction_stops = ['.', ',','(',')','-','_',' ', ':', ').','),']


dic = {}
wordsfound = {}

with open("decisions/courtDecisionsPreprocessed.json") as f:
    for line in f:
        j = json.loads(line)
        if 'sentencesSplitted' in j:
            sentences = j['sentencesSplitted'].split('\n')
            for sentence in sentences:
                all_words = nltk.tokenize.WordPunctTokenizer().tokenize(sentence)
                keywords = []
                for word in all_words:
                    if word not in de_stops and word not in punction_stops:
                        if not re.search('[0-9]*', word):
                            keywords.append(word.lower())
                            wordsfound[word.lower()] = wordsfound.get(word.lower(),[])
                            wordsfound[word.lower()] += 1
#                key = ''.join(sorted(keywords))
#                if key in dic.keys():
#                    dic[key]= dic[key] + 1
#                else:
#                    dic[key]=1

for val in dic.values():
    if val > 1:
        print(val)

