import spacy

nlp = spacy.load('en_use_md')

def similar(s1,s2):
    
    return(nlp(s1).similarity(nlp(s2)))