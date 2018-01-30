'''
Created on Jan 29, 2018

@author: tchan
'''
import os 
# Import libraries necessary for this project
import numpy as np
import pandas as pd



class TitanicSurvival(object):
    
    def find(self,name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    
    def calculateSurvialPossibility(self):
        importDataFile = self.find('titanic_data.csv',os.getcwd())

        full_data = pd.read_csv(importDataFile)
        
        # Print the first few entries of the RMS Titanic data
        print(full_data.head())
        
        


        
        
        

titanic = TitanicSurvival()
titanic.calculateSurvialPossibility()
print("Here")

        