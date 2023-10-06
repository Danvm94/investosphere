from django.test import TestCase
from unittest.mock import patch
from user_management.newsapi import get_news_api


class TestGetNewsAPI(TestCase):

    @patch('user_management.newsapi.requests.get')
    def test_get_cached_articles(self, mock_requests_get):
        # Mock the cache to return cached articles
        with patch('user_management.newsapi.cache.get',
                   return_value=['cached_article1',
                                 'cached_article2']) as mock_cache_get:
            articles = get_news_api()

            # Ensure that the cached articles are returned
            self.assertEqual(articles, ['cached_article1', 'cached_article2'])

            # Ensure that the API request is not made when articles are cached
            mock_requests_get.assert_not_called()

    @patch('user_management.newsapi.requests.get')
    def test_get_articles_from_api(self, mock_requests_get):
        # Mock the cache to return None (no cached articles)
        with patch('user_management.newsapi.cache.get',
                   return_value=None) as mock_cache_get:
            # Mock the API response with sample articles
            mock_response = {
                'articles': ['api_article1', 'api_article2', 'api_article3']}
            mock_requests_get.return_value.json.return_value = mock_response

            articles = get_news_api()

            # Ensure that the function requests articles from the API
            mock_requests_get.assert_called_once()

            # Ensure that the returned articles match the ones from the API
            self.assertEqual(articles,
                             ['api_article1', 'api_article2', 'api_article3'])

            # Ensure that the articles are cached
            mock_cache_get.assert_called_once()
