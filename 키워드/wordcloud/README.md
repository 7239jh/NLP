# wordcloud
이 코드는 빈도수가 아닌 krwordrank의 rank를 int로 변형 후 워드클라우드를 산출  
# 실행방법
rank가 아닌 빈도수나 다른 수치를 입력하길 원하면 아래의 코드에서 ranks 리스트 대신 다른 리스트 입력  
```python
tag=[]
for i,j in zip(keys,ranks):
    tag.append((i,int(j)))
dic=dict(tag[:50])
dic
```

# 한글 글씨체 로드
글씨체 파일 경로를 지정  
```python
wc = WordCloud(font_path='D:/mycode/NLP/keyword/wordcloud/gulim.ttc',background_color="white", max_font_size=60)
```
