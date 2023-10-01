from django.test import TestCase
from investo_hub.chart import get_timestamps_date, convert_timestamps_date, get_clean_values


class TestCryptoDataFunctions(TestCase):
    def test_get_timestamps_date(self):
        # Create sample data
        data = {
            'crypto1': [(1632847200000, 100), (1632847300000, 110)],
            'crypto2': [(1632847200000, 200), (1632847300000, 220)],
        }

        # Test the function
        result = get_timestamps_date(data)

        # Perform assertions
        expected_result = ['28/09/2021', '28/09/2021']
        self.assertEqual(result, expected_result)

    def test_convert_timestamps_date(self):
        # Create sample timestamps
        timestamps = [1632847200000, 1632847300000]

        # Test the function
        result = convert_timestamps_date(timestamps)

        # Perform assertions
        expected_result = ['28/09/2021', '28/09/2021']
        self.assertEqual(result, expected_result)

    def test_get_clean_values(self):
        # Create sample data
        data = {
            'crypto1': [(1632847200000, 100), (1632847300000, 110)],
            'crypto2': [(1632847200000, 200), (1632847300000, 220)],
        }

        # Test the function
        result = get_clean_values(data)

        # Perform assertions
        expected_result = {
            'crypto1': [100, 110],
            'crypto2': [200, 220],
        }
        self.assertEqual(result, expected_result)
