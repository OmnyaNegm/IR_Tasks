from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import pandas as pd

Text = 'NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.'

Choice_Number_1 = word_tokenize(Text)
print('\n','Choice Number 1','\n',Choice_Number_1)

Choice_Number_2 = sent_tokenize(Text)
print('\n','Choice Number 2','\n',Choice_Number_2)

Choice_Number_3 = Text
print('\n','Choice Number 3:','\n',Choice_Number_3)

Show = pd.read_csv("E:\FCAI DU\Third Year\Second Term\IR\IR Task\Robo.csv", nrows=5)
print('\n', 'The first 5 Rows','\n',Show)

Show = pd.read_csv("E:\FCAI DU\Third Year\Second Term\IR\IR Task\Covid.csv", nrows=5)
print('\n', 'The first 5 Rows of covide dataset','\n',Show)



