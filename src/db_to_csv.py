import conect_db

db = conect_db.Noticias_DB()
lista_de_tabelas = [
    'noticia_vacina', 
    'comentario_vacina', 
    'vacina_paginas_noticia', 
    'vacina_search_tweets', 
    'vacina_tweets_aleatorios',
    'vacina_tweets_rt', 
    'vacina_user_rt'
]

for tabela in lista_de_tabelas:
    df = db.get_df(tabela)
    print(f'Tabela {tabela} ** ', end='')
    df.to_csv(f'./data/{tabela}.csv', index=False)
    print(f' Salvo!')

