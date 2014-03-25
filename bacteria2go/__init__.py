#!/usr/bin/python

__version__ = '0.0.1'
__email__ = 'marco.galardini@ebi.ac.uk'

def dict2Strain(d):
    '''
    Takes a JSON-derived dict and returns a Strain object
    '''
    strain = Strain(d['id'])
    
    for k,v in d.items():
        if k == 'id':continue
        setattr(strain, k, v)

    return strain

class Strain(object):
    '''
    Strain class

    contains all relevant informations regarding a strain
    inside the NCBI database
    '''

    def __init__(self, id):
        self.id = id
        self.name = None
        self.taxid = None

        self.taxonomy = None
        self.bioproject = None

        self.creation = None
        self.updated = None

        self.ndna = None
        self.ldna = None
        self.gc = None

        self.nprot = None
        self.lprot = None

        self.complete = None

    def __len__(self):
        '''
        Length of the genome (in base pairs)
        '''
        return self.ldna

    def check(self):
        '''
        Check if some of the general statistics are None
        '''
        if None in [self.ndna, self.ldna, self.nprot, self.lprot]:
            return False
        return True

    def toDict(self):
        '''
        Returns a dictionary representation of this object
        Useful for JSON serialization
        '''
        d = {}
        
        d['id'] = self.id
        d['name'] = self.name
        d['taxid'] = self.taxid
        d['taxonomy'] = self.taxonomy
        d['bioproject'] = self.bioproject
        d['creation'] = self.creation
        d['updated'] = self.updated

        d['ndna'] = self.ndna
        d['ldna'] = self.ldna
        d['gc'] = self.gc

        d['nprot'] = self.nprot
        d['lprot'] = self.lprot

        d['complete'] = self.complete

        return d
        

