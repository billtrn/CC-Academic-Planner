import pandas as pd
import os

catalog = pd.read_csv('spring21.csv')
attributes = pd.read_csv('spring21attr.csv')
#print(catalog.head())

def getAttr(crn):
    return attributes.loc[attributes['SSRATTR_CRN'] == crn]['SSRATTR_ATTR_CODE'].tolist()

def getCRN(title):
   return catalog.loc[catalog['TITLE'] == title]['CRN'].tolist()[0]

title = 'INTRO TO LANGUAGE AND MIND'
crn = getCRN(title)
print('The atrributes for', title, 'are:', getAttr(crn))