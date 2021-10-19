import pandas as pd
from data_preprocessing import clean_text
import os
import pickle

with open('../data/TweetsMG_LogisticRegression_AS.pkl', 'rb') as f:
    model = pickle.load(f)

with open('../data/TweetsMG_text_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)


files = os.listdir('../data/dfs/')
dic_classificacao = {
    0 : 'Neutro',
    2 : 'Negativo',
    1: 'Positivo',
}
for file in files:
    file = file.replace('.csv', '')
    df =  pd.read_csv(f'../data/dfs/{file}.csv')
    
    # preprocessamento
    df['preprocessed_text'] = df['text'].apply(lambda x: clean_text(x))

    try:
        # vetorização
        df_vectorize = vectorizer.transform(df['preprocessed_text'].values.tolist())

        # classificação
        df['sentimento'] = model.predict(df_vectorize)
        
        df['sentimento'] = df['sentimento'].replace(dic_classificacao)

        # salvando os dados em csv
        df.to_csv(f'../data/previsoes/{file}_predict.csv', index=False)

        print(f'{file} ** OK')
        
    except BaseException as e:
        print(f'{file} ** FALHOU!')

print('fim!')
