# Homework

## Question 1. Redpanda version

After running `docker exec -it workshop-redpanda-1 rpk version` , the version of Redpanda is v25.3.9.

## Question 2. Sending data to Redpanda

We create a topic called green-trips using the follwing comand `docker exec -it workshop-redpanda-1 rpk topic create green-trips`, the we crete a producer to send the green taxi data to this topic usinng the file [`homework_producer.py`](https://github.com/azattara/streaming-workshop/blob/main/src/producers/homework_producer.py). The process was executed and the closest answer from the set of suggested answers is 10 seconds.


## Question 3. Consumer - trip distance

To answer how many trips have a trip_distance greater than 5.0 kilometers we create execute the script  [`homework_consumer.py`](https://github.com/azattara/streaming-workshop/blob/main/src/consumers/homework_consumer.py). The answer is 8506.
