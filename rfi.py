import numpy as np
import os

class RFI:
    def __init__(self, spectrum_model, masktype = None):
        self.spectrum_model = spectrum_model
        self.masktype = masktype

    #get dimension of spectrum_model

    #initialize an array of value 1

    #class should include methods to generate and return different rfi masks

    def generate_mask(self, masktype):

        mask = np.zeros(np.shape(self.spectrum_model))
        
        if self.masktype == None:
            
            mask[:,:] = 1.

        if os.path.exists(self.masktype):
            
            mask[:,:] = 1. #open profile and load in as mask
            assert(np.shape(self.spectrum_model) == np.shape(mask))

        return mask
    
