import pandas as pd
import requests
from io import StringIO


def source_data_from_web_page(web_page_url, matching_keyword):
    """
    Fetches a table from a webpage and returns it as a pandas DataFrame.
    """
    try:
        # Define headers to mimic a browser request and avoid 403 Forbidden errors
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(web_page_url, headers=headers)
        response.raise_for_status()

        # Wrap the response text in StringIO to comply with Pandas 2.0+ requirements
        # match specifies a unique string that must be present in the target table
        tables = pd.read_html(StringIO(response.text), match=matching_keyword)

        if not tables:
            print("No tables found matching the keyword.")
            return pd.DataFrame()

        df = tables[0]

        # Clean up headers:
        # Wikipedia tables often use MultiIndex (nested headers).
        # This collapses them into a single string (e.g., 'IMF_Estimate')
        df.columns = [
            '_'.join(col).strip() if isinstance(col, tuple) else col
            for col in df.columns.values
        ]

        # Rename the first column to a standard 'Country' name
        df.rename(columns={df.columns[0]: 'Country'}, inplace=True)

        return df

    except Exception as e:
        print(f"Error during data extraction: {e}")
        return pd.DataFrame()


def extract_data():
    """
    Main function to define the source URL and trigger the extraction.
    """
    web_page_url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    # 'Country/Territory' is a reliable unique string for the GDP table
    matching_keyword = "Country/Territory"

    df_html = source_data_from_web_page(web_page_url, matching_keyword)
    return df_html


# Execute the script
if __name__ == "__main__":
    df = extract_data()

    if not df.empty:
        # Display the first 10 rows and the first few columns to verify the result
        print("Data successfully extracted:")
        print(df.iloc[:, [0, 1, 2]].head(10))
    else:
        print("DataFrame is empty. Check the URL or matching keyword.")