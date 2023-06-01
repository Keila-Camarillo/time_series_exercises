import pandas as pd

def process_dataframe(df):
    """
    Process the given DataFrame by performing the following operations:
    1. Remove GMT from the 'sale_date' column.
    2. Strip whitespace from the 'sale_date' column.
    3. Change the datatype of the 'sale_date' column to datetime.
    4. Set the 'sale_date' column as the index.
    5. Sort the DataFrame by the index.
    6. Create a 'month' column based on the 'sale_date' index.
    7. Create a 'day_of_week' column based on the 'sale_date' index.
    8. Create a 'sales_total' column by multiplying 'sale_amount' and 'item_price' columns.

    Parameters:
        df (pandas.DataFrame): The DataFrame to be processed.

    Returns:
        pandas.DataFrame: The processed DataFrame.
    """
    # Remove GMT
    df.sale_date = df.sale_date.str.replace('00:00:00 GMT', '')
    
    # Strip whitespace
    df.sale_date = df.sale_date.str.strip()
    
    # Change datatype
    df.sale_date = pd.to_datetime(df.sale_date, format="%a, %d %b %Y")
    
    # Set index
    df = df.set_index('sale_date')
    
    # Sort index
    df = df.sort_index()
    
    # Create month column
    df['month'] = df.index.strftime('%B')
    
    # Create day of week column
    df['day_of_week'] = df.index.strftime('%a')
    
    # Create sales total from sale amount and item price
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

def drop_rows_by_index_range(df, start_date, end_date):
    """
    Drop rows from a DataFrame based on a specified index range.

    Parameters:
        df (pandas.DataFrame): The DataFrame from which to drop rows.
        start_date (str or pandas.Timestamp): The start date of the index range (inclusive).
        end_date (str or pandas.Timestamp): The end date of the index range (inclusive).

    Returns:
        pandas.DataFrame: The DataFrame with rows dropped based on the specified index range.
    """
    # Create a mask to identify rows within the specified index range
    mask = (df.index >= start_date) & (df.index <= end_date)
    
    # Drop rows using the mask
    df = df.drop(df[mask].index)
    
    return df

def fill_nulls_using_resample(df, frequency):
    """
    Resamples the DataFrame to a specified frequency and fills null values using the forward fill method.

    Args:
        df (DataFrame): The input DataFrame.
        frequency (str): The desired frequency for resampling, such as 'D' for daily, 'W' for weekly, or 'M' for monthly.

    Returns:
        DataFrame: The resampled DataFrame with null values filled using the forward fill method.
    """
    # Resample the DataFrame
    df_resampled = df.resample(frequency).asfreq()
    
    # Apply fill method to handle null values
    df_filled = df_resampled.fillna(method='ffill')  # Forward fill
    
    return df_filled