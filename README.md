# BeckToTheFuture: Auto-generated Legal Commentary from Court Decisions

This repository demonstrate how to extract sentences from cour decisions, train a classifier of language style of sentences, compute similiarity within the corpus, compute a final ranking score.

- Traning data: `*.txt`
- Train sentence classifier: `spacy-textcat.ipynb`
- Compute similarity: `wordSim.py`
- Compute ranking: `rank_sentences.ipynb`

## #blt19

- Team: Malte, Till, Fritz, Matthias, Jan
- Which problems does your idea tackle?
  In Germany, laws are often written in an ambiguous way and it is left to courts to define a more precise meaning. These comments to laws by judges are particularly important but difficult to find. We automatically detect these sentences and provide a ranked list of comments for a specific law paragraph.

- Estimated Deliverable: Proof of concept demo for a subset of laws.

- Type of product: Web Interface

- Value Proposition:  Commentary for laws is valuable but subject to copyright. Auto-generated, high-quality commentary is an asset for each lawyer and judge in Germany. 
  
## Other notes

- Urteilsdatenbank im JSON Format http://prinz.law/decisions.zip
