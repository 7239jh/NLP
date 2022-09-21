# kr-wordrank를 활용한 키워드 추출
kr-wordrank를 활용하여 기본적인 불용어 제거 후 명사 키워드 만 추출  
kr-wordrank는 김현중님의 https://github.com/lovit/KR-WordRank에서 설치

# 실행방법
위에서 받은 KR-WordRank-master폴더 내에서 ipynb파일 실행  
추가 불용어제거 원할 경우 regex함수에 추가
명사말고 다른 형태소 출력 원할 경우 아래 코드에 다른 형태소명 입력
'''python
if len([w[0] for w in o if w[1] !='Noun'])==0:
'''
