from imdb import IMDb
from textblob import TextBlob
import pandas as pd

ia = IMDb()
moviequotes = []

movie = ia.search_movie('godfather')
movid = movie[0].movieID
mymov = ia.get_movie(movid)
ia.update(mymov, 'quotes', 'rating')

for q in mymov['quotes']:
    blob = TextBlob(str(q))
    score = {
        'movie': str(mymov),
        'rating': mymov['rating'],
        'quote': str(q),
        'polarity': blob.sentiment.polarity,
        'subjectivity': blob.sentiment.subjectivity
    }
    moviequotes.append(score)


df = pd.DataFrame(moviequotes)
df = df[(df.polarity != 0.0)]
total = pd.pivot_table(df, index=['movie'])
print(total.head())
