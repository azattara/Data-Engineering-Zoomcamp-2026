
import pandas as pd

# 1. Load the data
trips = pd.read_parquet('green_tripdata_2025-11.parquet')
zones = pd.read_csv('taxi_zone_lookup.csv')

# 2. Convert the date column to Pandas datetime format
trips['lpep_pickup_datetime'] = pd.to_datetime(trips['lpep_pickup_datetime'])

# 3. Filter only the trips from November 18, 2025
# We use .dt.date to compare only the date, ignoring the time
target_date = pd.to_datetime('2025-11-18').date()
trips_filtered = trips[trips['lpep_pickup_datetime'].dt.date == target_date]

# 4. Merge (join) with the zones dataframe to get the zone names
# PULocationID is the ID of the zone where the trip started
merged_data = pd.merge(trips_filtered, zones, left_on='PULocationID', right_on='LocationID')

# 5. Group by zone name ("Zone") and sum the "total_amount"
# We sort from highest to lowest (ascending=False)
result = merged_data.groupby('Zone')['total_amount'].sum().sort_values(ascending=False)

# 6. Display the final result
print(f"--- Zone with the highest total_amount on 11/18/2025: {result.index[0]}")
