from gensim. parsing.preprocessing import remove_stopwords

text = "new home sales top forecasts .....home sales rise in july .....increase in home sales in july....july new home sales rise"
filtered_sentence = remove_stopwords (text)
print (filtered_sentence)

Doc_1= "new home sales top forecasts"
Doc_2= "home sales rise in july"
Doc_3 = "increase in home sales in july"
Doc_4 = "july new home sales rise"
Docs =[Doc_1, Doc_2, Doc_3, Doc_4]

#creating inverted index in the form of a dictionary
inverted_index = {}
for i, doc in enumerate (Docs):
    for term in doc.split():
        if term in inverted_index:
            inverted_index [term].add(i+1)
        else: inverted_index[term] = {i+1}



