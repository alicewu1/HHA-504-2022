#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:48:50 2021

@author: hantswilliams



CREATE USER 'hantsTest'@'%' IDENTIFIED BY 'hants';
GRANT ALL PRIVILEGES ON * . * TO 'hantsTest'@'%';
FLUSH PRIVILEGES;


"""

import pandas as pd



loadUsers = pd.read_csv('./Part5_DBs/rbac/ahi_cohort_2022.csv')

loadUsers['un'] = loadUsers['userEmail'].str.split('@').str[0]
loadUsers['un'] = loadUsers['un'].str.lower()
loadUsers['un'] = loadUsers['un'].str.replace(r'\.', '')
loadUsers['un'] = loadUsers['un'].str.replace(r'\-', '')
loadUsers['pwd'] = loadUsers['un'] + '2021'


userlist = list(loadUsers['un'])





rule = """
GRANT ALL ON ahi.* TO 'USERNAME'@'%';
FLUSH PRIVILEGES;"""




modedAdd = [] 

for i in range(len(loadUsers)) :
    
  #Create the variables  
  username =  loadUsers.loc[i, "un"] 
 
  #Make a copy of the rule template 
  ruleCopy = rule
    
  #Replace the variables of the rule template with each of the row/from the transformed dataframe
  ruleCopy = ruleCopy.replace("USERNAME", username)
 
  modedAdd.append(ruleCopy)
  
  print('finishedWith: ', username)
  
  del(ruleCopy)
  
    
modedAddString = "\n".join(modedAdd)





#open and delete existing file
open("./Part5_DBs/rbac/userModificationP2.sql", 'w').close()
#write the new rules to it
f= open("./Part5_DBs/rbac/userModificationP2.sql","w+")
f.write(modedAddString)
f.close() 





