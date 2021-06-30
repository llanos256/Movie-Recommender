import pandas as pd

datos = pd.read_csv('movies_metadata.csv')
print(datos.head)
media = datos['vote_average'].mean()
print ("media: ", media)

minimo = datos['vote_count'].quantile(0.90)
print(minimo)

pelicula_p= datos.copy().loc[datos['vote_count'] >= minimo]
print(pelicula_p.shape)

def rating_ponderado(x, minimo=minimo, media=media):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+minimo) * R) + (minimo/(minimo+v) * media)

pelicula_p['score'] = pelicula_p.apply(rating_ponderado, axis=1)
pelicula_p = pelicula_p.sort_values('score', ascending=False)

print(pelicula_p[['title', 'vote_count', 'vote_average', 'score']].head(10))