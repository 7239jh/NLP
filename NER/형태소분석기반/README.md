# 오타보정 및 형태소 분석기를 활용한 금융 도메인의 NER모델  
1. symspellpy_ko를 활용하여 오타보정
2. Komoran 형태소 분석기의 단어 사전을 도메인에 맞는 사전으로 수정
3. 지정한 엔티티명으로 NER분석

# 데이터
1. 금융 관련 질문 셋  

![text](https://user-images.githubusercontent.com/94896717/210909296-2c9f21d9-550b-4303-a8d1-77b29a40141d.png)
  
  
2. 엔티티 종류  
st: 종목명  
pr: 가격

# 실행방법
1. data폴더내에 본인이 학습시킬 질문데이터셋 저장 
2. 데이터셋 문장들을 유니그램, 바이그램으로 나눈 후 자모분해하여 각각txt로 저장
3. 저장한 txt와 symspellpy_ko를 활용하여 질문의 오타보정
4. 엔티티 설정
5. 금융도메인의 형태소사전으로 교체
6. 코모란 형태소분석기를 활용하여 NER분석

# 참고
1. symspellpy_ko: https://github.com/HeegyuKim/symspellpy-ko  
