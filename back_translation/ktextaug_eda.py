import pandas as pd
import argparse
from ktextaug import TextAugmentation
from tqdm import tqdm

def define_argparser():
    p = argparse.ArgumentParser()

    p.add_argument('--data',required=True)
    p.add_argument('--eda',required=True)

    config = p.parse_args()

    return config
config = define_argparser()

agent = TextAugmentation(tokenizer="komoran",num_processes=1)

def read_text():
    data_path=config.data
    df=pd.read_csv(data_path,sep=',')
    texts=df['texts'].tolist()
    labels=df['labels'].tolist()
    idx=int(len(texts))
    texts_eda=[]
    labels_eda=[]
    for i,j in tqdm(zip(texts[:idx],labels[:idx])):
        a=agent.generate(i)
        texts_eda.append(a)
        labels_eda.append(j)           
    dfe=pd.DataFrame({'labels':labels+labels_eda,'texts':texts+texts_eda})       
        
    return dfe

dfeda=read_text()
eda_path=config.eda
dfeda.to_csv(eda_path,sep=',',index=False)

