import pandas as pd
import os
import numpy as np

catalog = pd.read_csv('spring21.csv')
catalog = catalog.replace(np.nan, '', regex=True)
attributes = pd.read_csv('spring21attr.csv')
#print(catalog.head())

def getCourseList():
    cl = []
    for i in range(catalog['TITLE'].size):
        cl.append(catalog['TITLE'][i] + ", " + str(catalog['Sec'][i]))
    return cl

def getAttr(crn):
    return attributes.loc[attributes['SSRATTR_CRN'] == crn]['SSRATTR_ATTR_CODE'].tolist()

def getCRN(title):
   return catalog.loc[catalog['TITLE'] == title]['CRN'].tolist()[0]

def getDays(crn):
    return catalog.loc[catalog['CRN'] == crn]['Days1'].tolist()[0]

def getTimes(crn):
    return catalog.loc[catalog['CRN'] == crn]['Time1'].tolist()[0]

# title = 'INTRO TO LANGUAGE AND MIND'
# crn = getCRN(title)
# print('The atrributes for', title, 'are:', getAttr(crn))
# print(len(max(catalog['Notes'].tolist(), key=len)))
#print(getCourseList())
#print(getDays(10471))