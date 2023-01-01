# 실행방법
터미널에서 py파일들이 있는 폴더로 이동 후 아래 코드입력
```python
python finetune.py --model_fn ./models/test.pth --train_fn ./data/train_data.csv --gpu_id 0 --batch_size 32 --n_epochs 2 --pretrained_model_name "monologg/koelectra-base-v3-discriminator"
```
