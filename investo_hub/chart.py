from datetime import datetime


def get_timestamps_date(data):
    for crypto_data in data.values():
        return convert_timestamps_date([entry[0] for entry in crypto_data])


def convert_timestamps_date(timestamps):
    date_format = "%d/%m/%Y"
    formatted_dates = [
        datetime.utcfromtimestamp(ts / 1000).strftime(date_format) for ts in
        timestamps]
    return formatted_dates


def get_clean_values(data):
    # Initialize an empty dictionary to store the organized data
    crypto_dict = {}

    for crypto, values in data.items():
        # Extract the prices (second element) from each entry
        prices = [entry[1] for entry in values]
        crypto_dict[crypto] = prices
    return crypto_dict
