# 사전학습모델을 활용한 음절기반 NER분석
금융챗봇을 만들기 위해 필요한 금융도메인의 NER분석기로서 데이터를 자체적으로 만들었기에 매우 적은 양으로 소수의 엔티티에 대해서만 실험  
금융관련 엔티티는 오픈소스 형태소분석기로는 분류가 잘 안되고 형태소분석기를 만들만큼 데이터가 충분하지 않기에 음절기반의 NER분석기를 만듬

# 실행방법
1. 박장원님이 개발하신 사전학습모델인 KoCharELEcTRA모델을 https://github.com/monologg/KoCharELECTRA에서 받아서 설치한다.
2. data폴더내에 본인이 학습시킬 음절레이블링이된 데이터셋을 저장한다.(train.tsv, valid.tsv, test.tsv)
3. KoCharELECTRA_master폴더가 있는 폴더내에서 ner_character.ipynb을 실행
