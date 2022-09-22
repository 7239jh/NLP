# textrank를 활용한 키워드 추출
textrank를 활용하여 기본적인 불용어 제거 후 명사 키워드 만 추출  
textrank는 김현중님의 https://github.com/lovit/textrank 에서 설치  
# 실행방법
위에서 받은 패키지 폴더 내에서 ipynb파일 실행  
추가 불용어제거 원할 경우 regex함수에 추가 
```python
def regex(x):
    
    x=re.sub("\[.*\]|\s-\s.*",'',x)
    x=re.sub("\(.*\)|\s-\s.*",'',x)
    x=re.sub("\<.*\>|\s-\s.*",'',x)
    x=re.sub("\【.*\】|\s-\s.*",'',x)
    x= re.sub('[-=+#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》,▷▶ⓒ]', '', x)
    
    return x
 ```
komoran, okt 형태소 분석기 중에 선택  
```python
keyword_extractor_komoran = KeywordSummarizer(
    tokenize = komoran_tokenizer,min_count=2, min_cooccurrence=1,
    window=-1,                
    verbose = False)

keyword_extractor_okt = KeywordSummarizer(
    tokenize = okt_tokenizer,min_count=2, min_cooccurrence=1,
    window=-1,                
    verbose = False)
```

명사말고 다른 형태소 출력 원할 경우 아래 코드에 다른 형태소명 입력  
```python
def komoran_tokenizer(sent):
    words = komoran.pos(sent, join=True)
    words = [remove(w) for w in words if ('/NNG' in w or '/NNP' in w)]
    return words

def okt_tokenizer(sent):
    words = okt.pos(sent, join=True)
    words = [remove(w) for w in words if ('/Noun' in w) ]
    return words
```
