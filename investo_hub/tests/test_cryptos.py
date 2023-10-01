from django.db.models import QuerySet
from django.test import TestCase
from investo_hub.models import Cryptos
from user_management.models import Crypto
from django.contrib.auth.models import User
from unittest.mock import patch
from django.core.cache import cache
from investo_hub.cryptos import (
    request_coin_api,
    request_coin_api_chart,
    request_coin_chart_cache,
    request_coin_cache,
    get_coin_info,
    get_user_cryptos,
    clear_cache,
)


class TestRequestCoinAPI(TestCase):

    @patch('investo_hub.cryptos.requests.get')
    @patch('investo_hub.cryptos.cache.set')
    def test_request_coin_api_success(self, mock_cache_set, mock_requests_get):
        # Mock the requests.get() method to return a successful response
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = [{'crypto_data': 'example'}]

        # Call your function
        result = request_coin_api()

        # Check if cache.set is called with the expected arguments
        mock_cache_set.assert_called_once_with('cached_cryptos', [{'crypto_data': 'example'}], 1 * 60 * 60)

        # Check if the result is as expected
        self.assertEqual(result, [{'crypto_data': 'example'}])

    @patch('investo_hub.cryptos.requests.get')
    def test_request_coin_api_failure(self, mock_requests_get):
        # Mock the requests.get() method to return an error response
        mock_requests_get.return_value.status_code = 404

        # Call your function
        result = request_coin_api()

        # Check if the result is None when the request fails
        self.assertIsNone(result)


class TestRequestCoinAPIChart(TestCase):

    @patch('investo_hub.cryptos.request_coin_cache')
    @patch('investo_hub.cryptos.requests.get')
    @patch('investo_hub.cryptos.cache.set')
    def test_request_coin_api_chart(self, mock_cache_set, mock_requests_get, mock_request_coin_cache):
        # Mock the request_coin_cache function to return a sample cache data
        mock_request_coin_cache.return_value = [{'id': 'crypto1'}, {'id': 'crypto2'}]

        # Mock the requests.get() method to return a successful response
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {'prices': [100, 200, 300]}

        # Call your function
        result = request_coin_api_chart()

        # Check if cache.set is called with the expected arguments
        mock_cache_set.assert_called_once()

        # Check if the result is as expected
        expected_result = {'crypto1': [100, 200, 300], 'crypto2': [100, 200, 300]}
        self.assertEqual(result, expected_result)


class TestRequestCoinChartCache(TestCase):

    @patch('investo_hub.cryptos.cache.get')
    @patch('investo_hub.cryptos.request_coin_api_chart')
    def test_request_coin_chart_cache_with_cached_data(self, mock_request_coin_api_chart, mock_cache_get):
        # Mock cache.get() to return some cached data
        mock_cache_get.return_value = {'cached_data': [100, 200, 300]}

        # Call your function
        result = request_coin_chart_cache()

        # Ensure request_coin_api_chart is not called
        mock_request_coin_api_chart.assert_not_called()

        # Check if the result is as expected (cached data)
        self.assertEqual(result, {'cached_data': [100, 200, 300]})

    @patch('investo_hub.cryptos.cache.get')
    @patch('investo_hub.cryptos.request_coin_api_chart')
    def test_request_coin_chart_cache_without_cached_data(self, mock_request_coin_api_chart, mock_cache_get):
        # Mock cache.get() to return None (no cached data)
        mock_cache_get.return_value = None

        # Mock request_coin_api_chart to return some data
        mock_request_coin_api_chart.return_value = {'crypto_data': [100, 200, 300]}

        # Call your function
        result = request_coin_chart_cache()

        # Ensure request_coin_api_chart is called
        mock_request_coin_api_chart.assert_called_once()

        # Check if the result is as expected (data from the API)
        self.assertEqual(result, {'crypto_data': [100, 200, 300]})


class TestRequestCoinCache(TestCase):

    @patch('investo_hub.cryptos.cache.get')
    @patch('investo_hub.cryptos.request_coin_api')
    def test_request_coin_cache_with_cached_data(self, mock_request_coin_api, mock_cache_get):
        # Mock cache.get() to return some cached data
        mock_cache_get.return_value = {'cached_data': [100, 200, 300]}

        # Call your function
        result = request_coin_cache()

        # Ensure request_coin_api is not called
        mock_request_coin_api.assert_not_called()

        # Check if the result is as expected (cached data)
        self.assertEqual(result, {'cached_data': [100, 200, 300]})

    @patch('investo_hub.cryptos.cache.get')
    @patch('investo_hub.cryptos.request_coin_api')
    def test_request_coin_cache_without_cached_data(self, mock_request_coin_api, mock_cache_get):
        # Mock cache.get() to return None (no cached data)
        mock_cache_get.return_value = None

        # Mock request_coin_api to return some data
        mock_request_coin_api.return_value = {'crypto_data': [100, 200, 300]}

        # Call your function
        result = request_coin_cache()

        # Ensure request_coin_api is called
        mock_request_coin_api.assert_called_once()

        # Check if the result is as expected (data from the API)
        self.assertEqual(result, {'crypto_data': [100, 200, 300]})


class TestGetCoinInfo(TestCase):

    @patch('investo_hub.cryptos.request_coin_cache')
    def test_get_coin_info_found(self, mock_request_coin_cache):
        # Mock the request_coin_cache function to return some sample data
        mock_request_coin_cache.return_value = [{'id': 'btc', 'name': 'Bitcoin'}, {'id': 'eth', 'name': 'Ethereum'}]

        # Call your function with a coin that exists in the cache
        result = get_coin_info('btc')

        # Check if the result is as expected
        expected_result = {'id': 'btc', 'name': 'Bitcoin'}
        self.assertEqual(result, expected_result)

    @patch('investo_hub.cryptos.request_coin_cache')
    def test_get_coin_info_not_found(self, mock_request_coin_cache):
        # Mock the request_coin_cache function to return some sample data
        mock_request_coin_cache.return_value = [{'id': 'btc', 'name': 'Bitcoin'}, {'id': 'eth', 'name': 'Ethereum'}]

        # Call your function with a coin that doesn't exist in the cache
        with self.assertRaises(Exception) as context:
            get_coin_info('doge')

        # Check if the exception message is as expected
        self.assertEqual(str(context.exception), 'Cryptocurrency "doge" not found in the cache.')


class TestGetUserCryptos(TestCase):

    def test_get_user_cryptos(self):
        # Create a user and some crypto records in the database for testing
        user = User.objects.create(username='testuser')
        btc = Crypto.objects.create(name='bitcoin')
        eth = Crypto.objects.create(name='ethereum')
        Cryptos.objects.create(user=user, crypto=btc, amount=1)
        Cryptos.objects.create(user=user, crypto=eth, amount=2)

        # Call your function
        self.result = get_user_cryptos(user)

        # Check if the result is a queryset
        self.assertIsInstance(self.result, QuerySet)

        # Check if the queryset contains two objects
        self.assertEqual(self.result.count(), 2)

        # Check if the objects contain specific fields
        for crypto_obj in self.result:
            self.assertTrue(hasattr(crypto_obj, 'usd'))
            self.assertTrue(hasattr(crypto_obj, 'image'))


class TestClearCache(TestCase):

    def test_clear_cache(self):
        # Set some data in the cache for testing
        cache.set('cached_cryptos', {'data': 'crypto_data'}, 60 * 60)
        cache.set('cached_cryptos_chart', {'data': 'chart_data'}, 60 * 60)

        # Call the clear_cache function
        clear_cache()

        # Check if the cache keys have been deleted
        self.assertIsNone(cache.get('cached_cryptos'))
        self.assertIsNone(cache.get('cached_cryptos_chart'))
