"""Minimal working example code to load the IBM data.
"""

import pickle

def load_obj(filename ):
    with open(filename + '.pkl', 'rb') as f:
        return pickle.load(f)
    
    
directory = '12-03-19/'
filename = 'CDW_clean_poughkeepsie_6sites_symmetric_tmax1-5_trotter4'

data = load_obj(directory+filename)

print(data)