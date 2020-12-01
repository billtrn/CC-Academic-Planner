import pandas as pd
import os
import numpy as np

catalog = pd.read_csv('spring21.csv')
catalog = catalog.replace(np.nan, '', regex=True)
attributes = pd.read_csv('spring21attr.csv')

def getCourseList():
    cl = []
    for i in range(catalog['TITLE'].size):
        cl.append(catalog['TITLE'][i] + ", " + str(catalog['Sec'][i]))
    return cl

def getAttr(crn):
    return attributes.loc[attributes['SSRATTR_CRN'] == crn]['SSRATTR_ATTR_CODE'].tolist()

def getCRN(title):
    return catalog.loc[catalog['TITLE'] == title]['CRN'].tolist()[0]

def getNumber(crn):
    return catalog.loc[catalog['CRN'] == crn]['#'].tolist()[0]

def getDepartment(crn):
    return catalog.loc[catalog['CRN'] == crn]['Dept'].tolist()[0]

def getDays(crn):
    days = [catalog.loc[catalog['CRN'] == crn]['Days1'].tolist()[0]]

    if catalog.loc[catalog['CRN'] == crn]['Days2'].tolist()[0] != "":
        days.append(catalog.loc[catalog['CRN'] == crn]['Days2'].tolist()[0])

    if catalog.loc[catalog['CRN'] == crn]['Days3'].tolist()[0] != "":
        days.append(catalog.loc[catalog['CRN'] == crn]['Days3'].tolist()[0])

    return days

def getTimes(crn):
    times = [catalog.loc[catalog['CRN'] == crn]['Time1'].tolist()[0]]

    if catalog.loc[catalog['CRN'] == crn]['Time2'].tolist()[0] != "-":
        times.append(catalog.loc[catalog['CRN'] == crn]['Time2'].tolist()[0])

    if catalog.loc[catalog['CRN'] == crn]['Time3'].tolist()[0] != "-":
        times.append(catalog.loc[catalog['CRN'] == crn]['Time3'].tolist()[0])

    return times