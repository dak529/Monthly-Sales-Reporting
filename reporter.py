# reporter.py
import pandas as pd
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH[] OF OCTOBER 2014...")

url = 'https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/monthly-sales/sales-201904.csv'
df = pd.read_csv(url, error_bad_lines=False)
#print(df)

revenue = df["sales price"].sum()
print(revenue)

#df["month"] = pd.datetimeindex

df['year'] = pd.DatetimeIndex(df["date"]).year
df.head()

#print(df)

#df['year'] = pd.DatetimeIndex(df[columns]).year
#df.head()

df['month'] = pd.DatetimeIndex(df["date"]).month
df.head()

df['monthname'] = pd.to_datetime(df['month'], format='%m').dt.month_name()

#print(df)

month = df.at[0,"monthname"]
#print(month)
year = df.at[0,"year"]
#print(year)

print("Sales Report",month, year)

print("Total Sales:", to_usd(float(revenue)))