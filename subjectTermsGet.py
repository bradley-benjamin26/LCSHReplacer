#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import xml.etree.ElementTree as ET

outputFile = input("Please provide the name for the output file.")
searchTerm = input("Please provide LCSH term to query: ")
preferredTerm = input("Please provide the preferred term you would like to use: ")
url = "https://id.loc.gov/search/?q=cs:http://id.loc.gov/authorities/subjects&q="+searchTerm

data = requests.get(url).text
root = ET.fromstring(data)
results = root.findall(".//{http://www.w3.org/1999/xhtml}a[@title='Click to view record']")
with open(outputFile, 'w') as file:
    file.write("Old Term"+"\t"+"new term"+'\n')
    for term in results:
        term = term.text
        newTerm = term.replace(searchTerm, preferredTerm)
        print(term+' is being replace by '+newTerm)
        file.write(term+'\t'+newTerm+'\n')
