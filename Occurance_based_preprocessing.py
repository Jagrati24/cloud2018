
# coding: utf-8

# In[16]:





# In[11]:


stopList = {'hE','meM','kI','ke','ko','se','Ora','kA','ki','hEM','eka','jo','para','kriyA','lie','kiyA','karawA','usake','karane'}

import subprocess,os, nltk, string, sys
# enginput = sys.argv[1]
enginput = "state"
e_sent_file = '/home/nupur/13Task/Merged_eng.txt'
h_sent_file = '/home/nupur/13Task/Merged_hin_wx.txt'
# print(e_sent_path)
def data_cleaning(data) :
    cleaned_data = []
    for sent in data :
        sent=sent.strip("\n")
        sent=sent.translate(sent.maketrans('', '', string.punctuation)).split()
        cleaned_data.append(sent)
    return cleaned_data
def count_occurence(word):
    e_data=open(e_sent_file,"r").read().split("\n")
#     print(cmd)
    sent_no = []
    e_data=data_cleaning(e_data)
    for sent in e_data :
        if word in sent :
            sent_no.append(e_data.index(sent))
    print("Occurence of "+word+" is "+str(len(sent_no)))
    return sent_no
sentences=count_occurence(enginput)
# print(sentences)
hindi_data=[]
def common_hindi_words():
    from collections import Counter
    hindi_data = []
    h_data = open(h_sent_file,"r").read().split("\n")
    h_data = data_cleaning(h_data)
    for i in sentences :
        hindi_data.append(h_data[i])
#         print(i+1)
    hindi_data_flat = [item for sublist in hindi_data for item in sublist]
    print(hindi_data_flat)
    hindi_data_flat=[word for word in hindi_data_flat if word not in stopList]
    Counter = Counter(hindi_data_flat)
    most_hin_occured = Counter.most_common(2)
    print(most_hin_occured)
    #print("###############")
    #print(hindi_data)

common_hindi_words()  

