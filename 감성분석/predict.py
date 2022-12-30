import sys
import argparse

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchtext import data

from transformers import BertTokenizerFast,BertModel
from transformers import BertForSequenceClassification, AlbertForSequenceClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification,AdamW
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.metrics import f1_score


def define_argparser():
  
    p = argparse.ArgumentParser()
    p.add_argument('--data',required=True)
    p.add_argument('--pred',required=True)
    p.add_argument('--model_fn', required=True)
    p.add_argument('--gpu_id', type=int, default=-1)
    p.add_argument('--batch_size', type=int, default=256) 
    p.add_argument('--top_k', type=int, default=1)  

    config = p.parse_args()

    return config


def read_text():
  
    data_path=config.data
    df=pd.read_csv(data_path,sep=',')
    df_drop=df.dropna(axis=0)
    df_text=df_drop['texts']
    texts=df_text.tolist()
    
    return texts
def read_label():
   
    data_path=config.data
    df=pd.read_csv(data_path,sep=',')
    df_drop=df.dropna(axis=0)
    df_text=df_drop['labels']
    texts=df_text.tolist()
    texts_int=list(map(int,texts))
    return texts_int

def main(config):
    saved_data = torch.load(
        config.model_fn,
        map_location='cpu' if config.gpu_id < 0 else 'cuda:%d' % config.gpu_id
    )   

    train_config = saved_data['config']
    bert_best = saved_data['bert']
    index_to_label = saved_data['classes']

    lines = read_text()

    with torch.no_grad():  
        tokenizer = AutoTokenizer.from_pretrained(train_config.pretrained_model_name)
        model_loader =AutoModelForSequenceClassification
        model = model_loader.from_pretrained(
            train_config.pretrained_model_name,
            num_labels=len(index_to_label)
        )
        model.load_state_dict(bert_best)  

        if config.gpu_id >= 0:
            model.cuda(config.gpu_id)
        device = next(model.parameters()).device  

        model.eval()

        y_hats = []
        for idx in range(0, len(lines), config.batch_size):
            mini_batch = tokenizer(
                lines[idx:idx + config.batch_size],
                padding=True,    
                truncation=True,  
                return_tensors="pt", 
            )

            x = mini_batch['input_ids']
            x = x.to(device)   
            mask = mini_batch['attention_mask']  
            mask = mask.to(device)

            y_hat = F.softmax(model(x, attention_mask=mask).logits, dim=-1)

            y_hats += [y_hat]

        y_hats = torch.cat(y_hats, dim=0)

        probs, indice = y_hats.cpu().topk(config.top_k)
        pred=[]
        for i in range(len(lines)):
            p=[int(index_to_label[int(indice[i][j])]) for j in range(config.top_k)]
            pred +=p
        result=pd.DataFrame({'labels':pred,'texts':read_text()})
        result.to_csv(config.pred,sep=',',index=False)
        accuracy = accuracy_score(read_label(),pred)
        f1 = f1_score(read_label(),pred,average='weighted')   
        print('acc:'' ' '%.4f' % (accuracy)) 
        print('f1:'' ' '%.4f' % (f1))  

if __name__ == '__main__':
    config = define_argparser()    
    main(config)
