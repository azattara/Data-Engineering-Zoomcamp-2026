## Question 1.  In a Bruin project, what are the required files/directories?

According to official examples and documentation, a minimal Bruin project must include:

.bruin.yml at the root directory — this defines environments, connections, and secrets. A pipeline/ directory containing:
pipeline.yml — the pipeline's metadata and configuration.
An assets/ folder — containing all asset files (Python, SQL, YAML, etc.).

Therefore the answer is .bruin.yml and pipeline/ with pipeline.yml and assets/

## Question 2. You're building a pipeline that processes NYC taxi data organized by month based on `pickup_datetime`. Which incremental strategy is best for processing a specific interval period by deleting and inserting data for that time period?

time_interval is designed for time-based processing windows—e.g., “reprocess January by deleting and reinserting rows where pickup_datetime falls in that month.” The reason for is:

   - Deletes & reinserts for a specific window: Exactly matches the need to refresh a monthly slice without touching other months.
   - Time-key driven: You specify a time column (here, pickup_datetime) to bound the interval.

Therefore the answer is `time_interval` - incremental based on a time column

## Question 3.
