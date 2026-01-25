
import pandas as pd

# 1. Load the dataset
df = pd.read_parquet('green_tripdata_2025-11.parquet')

# 2. Convert datetime columns to proper datetime format (if necessary)
df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)

# 3. Apply the filters:
# - Trips in November (between 2025-11-01 inclusive and 2025-12-01 exclusive)
# - Trip distance (trip_distance) <= 1 mile
query = df[
    (df.lpep_pickup_datetime >= '2025-11-01') &
    (df.lpep_pickup_datetime < '2025-12-01') &
    (df.trip_distance <= 1)
]

# 4. Count the results
print(f"Total trips: {len(query)}")
