
import pandas as pd

# 1. Load the data
trips = pd.read_parquet('green_tripdata_2025-11.parquet')
zones = pd.read_csv('taxi_zone_lookup.csv')

# 2. Merge with the zone table to identify the PICKUP zone
merged_data = pd.merge(trips, zones, left_on='PULocationID', right_on='LocationID')
merged_data.rename(columns={'Zone': 'pickup_zone'}, inplace=True)

# 3. Filter only trips that started in "East Harlem North"
# Note: The filter for November is already implicit in the month 11 file
ehn_trips = merged_data[merged_data['pickup_zone'] == 'East Harlem North']

# 4. Merge the result with the zone table to identify the DROP-OFF zone
df_final = pd.merge(ehn_trips, zones, left_on='DOLocationID', right_on='LocationID')
df_final.rename(columns={'Zone': 'dropoff_zone'}, inplace=True)

# 5. Find the row with the highest tip_amount
# We find the index of the largest tip and retrieve the name of the drop-off zone
largest_tip_zone = df_final.sort_values('tip_amount', ascending=False).iloc[0]['dropoff_zone']

# 6. Display the final result
print(f"--- The drop off zone that had the largest tip was: {largest_tip_zone} ---")


