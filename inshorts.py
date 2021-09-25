import requests
from bs4 import BeautifulSoup
import pandas as pd
dummy_url="https://inshorts.com/en/read/badminton"
data_dummy=requests.get(dummy_url)
soup=BeautifulSoup(data_dummy.content,'html.parser')

# news1=soup.find_all('div', class_=["news-card-title news-right-box"])[0]
# title=news1.find('span',attrs={'itemprop':"headline"}).string
# print(title)


# news1=soup.find_all('div', class_=["news-card-content news-right-box"])[0]
# content=news1.find('div',attrs={'itemprop':"articleBody"}).string
# print(content)

# news1=soup.find_all('div', class_ = ["news-card-author-time news-card-author-time-in-title"])[0]
# time = news1.find('span', clas=["date"]).string
# print(time)





urls=["https://inshorts.com/en/read/cricket","https://inshorts.com/en/read/tennis",
      "https://inshorts.com/en/read/badminton"]
news_data_content,news_data_title,news_data_category,news_data_time=[],[],[],[]
for url in urls:
  category=url.split('/')[-1]
  data=requests.get(url)
  soup=BeautifulSoup(data.content,'html.parser')
  news_title=[]
  news_content=[]
  news_category=[]
  news_time = []
  for headline,article,time in zip(soup.find_all('div', class_=["news-card-title news-right-box"]),
                            soup.find_all('div',class_=["news-card-content news-right-box"]),
                            soup.find_all('div', class_ = ["news-card-author-time news-card-author-time-in-title"])):
    
    news_title.append(headline.find('span',attrs={'itemprop':"headline"}).string)
    news_content.append(article.find('div',attrs={'itemprop':"articleBody"}).string)
    news_time.append(time.find('span', clas=["date"]))

    news_category.append(category)
  news_data_title.extend(news_title)
  news_data_content.extend(news_content)
  news_data_category.extend(news_category)  
  news_data_time.extend(news_time)

df1=pd.DataFrame(news_data_title,columns=["Title"])
df2=pd.DataFrame(news_data_content,columns=["Content"])
df3=pd.DataFrame(news_data_category,columns=["Category"])
df4=pd.DataFrame(news_data_time, columns=["time"])
df=pd.concat([df1,df2,df3,df4],axis=1)

df.to_csv("news_inshorts")

