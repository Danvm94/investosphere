from datetime import datetime


def get_timestamps_date(data):
    for crypto_data in data.values():
        return convert_timestamps_date([entry[0] for entry in crypto_data])


def convert_timestamps_date(timestamps):
    date_format = "%d/%m/%Y"
    formatted_dates = [datetime.utcfromtimestamp(ts / 1000).strftime(date_format) for ts in timestamps]
    return formatted_dates


def get_clean_values(data):
    crypto_dict = {}  # Initialize an empty dictionary to store the organized data

    for crypto, values in data.items():
        prices = [entry[1] for entry in values]  # Extract the prices (second element) from each entry
        crypto_dict[crypto] = prices
    return crypto_dict
