# Imports
import pandas as pd
import requests

def get_json(base_url, ext_url = ""):
    """
    Make an API request to retrieve JSON data and convert it to a DataFrame.

    Parameters:
        base_url (str): The base URL of the API.
        ext_url (str): The extended URL specific to the desired data (default: "").

    Returns:
        pandas.DataFrame: The merged DataFrame containing the retrieved data.
    """

    # Make the API request
    url = base_url + ext_url
    response = requests.get(url)
    data = response.json()
    data = data['results']

    # Create the initial DataFrame
    df = pd.DataFrame(data)

    # Concatenate the initial DataFrame with the extracted data
    df = pd.concat([df, pd.DataFrame(data)]).reset_index()

    return df

def acquire_opsd_data(url= 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'):
    """
    Acquire the Open Power Systems Data for Germany.

    Parameters:
        url (str): The URL to the OPSD data file.

    Returns:
        pandas.DataFrame: The acquired OPSD data.
    """
    # Read the data from the URL
    opsd_data = pd.read_csv(url)

    return opsd_data