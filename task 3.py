from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer

ps = PorterStemmer()
sb = SnowballStemmer('english')

Text = '''NLTK is a leading platform for building Python programs to work with human language data.
            NLTK is available for Windows, Mac OS X, and Linux.
            Best of all, NLTK is a free, open source, community-driven project.'''

Choice_Number_1 = word_tokenize(Text)
Choice_Number_2 = sent_tokenize(Text)
Choice_Number_3 = Text

user_choice = int(input('Please, Enter Your Choice: '))
if user_choice == 1:
    print("Choice Number one is : ", word_tokenize(Text))
elif user_choice == 2:
    print("Choice Number two is : ", sent_tokenize(Text))
elif user_choice == 3:
    print("Choice Number one is : ", Text)
elif user_choice == 4:
    var = str(input("Which stemmer do you want Snowball or Porter? : "))
if var == 'Porter':
    print( ps.stem('Programming'))
elif var == 'Snowball':
    print( sb.stem('programming'))




dataFrame= pd.read_csv("E:\FCAI DU\Third Year\Second Term\IR\IR Task\Robo.csv")
print("\nNumber of rows and column in our DataFrame = ",dataFrame.shape)
dataFrame = dataFrame.dropna()
print("\nDataFrame after removing null values...\n",dataFrame)
print("\n Number of rows and column after moving  null values = ",dataFrame.shape)
