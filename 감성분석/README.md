# 사전학습 모델을 활용한 감성분석
1. 터미널 환경에서 실행하여 학습(파인튜닝) 후 가장 valid_loss가 적은 모델을 저장
2. 저장한 모델을 로드하여 테스트셋 예측 및 평가

# 학습 실행방법
터미널에서 py파일들이 있는 폴더로 이동 후 아래 코드입력
```python
python finetune.py --model_fn ./models/test.pth --train_fn ./data/train_data.csv --gpu_id 0 --batch_size 32 --n_epochs 2 --pretrained_model_name "monologg/koelectra-base-v3-discriminator"
```
# 예측 실행방법
터미널에서 py파일들이 있는 폴더로 이동 후 아래 코드입력
```python
python predict.py --data ./data/test_data.csv --model_fn ./models/test.pth --gpu_id 0 --pred ./data/pred.csv
```

# 참고
데이터셋: 네이버평점리뷰  
코드: https://github.com/kh-kim 
