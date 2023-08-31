from django.core.cache import cache
import requests
import os

newsapi_key = os.environ.get('newsapi_key')
newsapi_url = os.environ.get('newsapi_url')


def get_news_api():
    # Get article from cache
    articles = cache.get('cached_articles')
    # If cache doesn't exist, request the API and save it on cache.
    if not articles:
        params = {
            'apiKey': newsapi_key,
            'language': 'en',
            'q': 'cryptocurrency',
            'sortBy': 'publishedAt'
        }
        response = requests.get(newsapi_url, params=params)
        news_data = response.json()
        articles = news_data['articles'][:4]
        cache.set('cached_articles', articles, 3 * 60 * 60)
    return articles
