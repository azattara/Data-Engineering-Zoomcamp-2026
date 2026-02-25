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

## Question 3. Pipeline VariablesYou have a variable defined in pipeline.yml:variables: taxi_types: type: array items: type: string default: ["yellow", "green"]How do you override this when running the pipeline to only process yellow taxis? 

The specific command `bruin run --var 'taxi_types=["yellow"]'` performs the following actions:

`bruin run`: Starts the execution of an individual asset (such as an SQL or Python script) or an entire pipeline in the current directory.

`--var`: Defines a dynamic variable (or parameter) that will be injected into the pipeline or asset code during execution.

`'taxi_types=["yellow"]`: Defines the variable name as `taxi_types` and assigns it a list containing the string "yellow".

Therefore the answer is - **`bruin run --var 'taxi_types=["yellow"]'`**


## Question 4. Running with DependenciesYou've modified the ingestion/trips.py asset and want to run it plus all downstream assets. Which command should you use?

Use the --downstream flag with bruin run, targeting the asset you changed:

- **`bruin run ingestion/trips.py --downstream`**

--downstream tells Bruin to execute the specified asset and all assets that depend on it (its downstream graph)

Then the answer is - **`bruin run ingestion/trips.py --downstream`**

## Question 5. Quality Checks. You want to ensure the pickup_datetime column in your trips table never has NULL values. Which quality check should you add to your asset definition? 

To check ythe quality it necessary add a column‑level quality check with the built‑in not_null check on pickup_datetime in the asset’s definition.

Answer: - **`name: not_null`**


