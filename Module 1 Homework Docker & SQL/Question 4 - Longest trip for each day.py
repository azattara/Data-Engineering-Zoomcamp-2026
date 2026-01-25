
import pandas as pd

# Load the data
df = pd.read_parquet('green_tripdata_2025-11.parquet')

# Filter trips with less than 100 miles
df_filtered = df[df['trip_distance'] < 100]

# Find the row (trip) with the greatest distance
longest_trip = df_filtered.loc[df_filtered['trip_distance'].idxmax()]

# Extract the date and time and format only the day
pickup_datetime = pd.to_datetime(longest_trip['lpep_pickup_datetime'])
pickup_day = pickup_datetime.strftime('%Y-%m-%d, %A')  # Format: YYYY-MM-DD, Day of the Week

print(f"The day with the longest trip (less than 100 miles) was: {pickup_day}")
print(f"The trip distance was: {longest_trip['trip_distance']} miles")

