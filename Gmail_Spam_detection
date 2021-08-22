
import pandas as pd
data = pd.read_csv('SPAM.csv' , encoding='windows-1252')
#print(data.head(10))---will show 10 rows of data from start(head)
data['spam'] = data['type'].map({'spam': 1, 'ham': 0}).astype(int)
#print(data.head(5))---will show 5 rows of data from start (head)after spam is added as a column
print("Columns in the given data :")
for col in data.columns:
    print(col)


#Tokenization
def tokenizer(textdata):
    return textdata.split()
data['text']=data['text'].apply(tokenizer)
print(data.head(5))


#Stemmimg
from nltk.stem import SnowballStemmer
snowball= SnowballStemmer(language='english',ignore_stopwords=False)
def stem_it(datatext):
    return (snowball.stem(x) for x in datatext)
data['text']=data['text'].apply(stem_it)
print(data.head(5))

#Lemmitization
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
lemmatizer= WordNetLemmatizer()
def lemmit_it(text):
    return[lemmatizer.lemmatize(word,pos="a") for word in text]
data['text'] = data['text'].apply(lemmit_it)


#Stopword removal

from nltk.corpus import stopwords
nltk.download('stopwords')
Stop_Words= stopwords.words('english')
def Stop_it(text):
    review=[word for word in text if not word in Stop_Words]
    return review
data['text']= data['text'].apply(Stop_it)
data['text']=data['text'].apply(''.join)


#Transform text data into TDF/TF_IDF vectors
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer()
y=data.spam.values
x=tfidf.fit_transform(data['text'])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1,test_size=0.2,shuffle=False)


#classification using logistic regression
from sklearn.linear_model import LogisticRegression
clf= LogisticRegression()
clf.fit(x_train,y_train)
y_pred= clf.predict(x_test)
from sklearn.metrics import accuracy_score
acc_log= accuracy_score(y_pred,y_test)*100
print("Accuracy: ",acc_log)

#classificatio using linear SVC accuracy
from sklearn.svm import LinearSVC
Linear_svc=LinearSVC(random_state=0)
Linear_svc.fit(x_train,y_train)
y_pred=Linear_svc.predict(x_test)
acc_linear_svc=accuracy_score(y_pred,y_test)*100
print("Accuracy_svc: ",acc_linear_svc)
