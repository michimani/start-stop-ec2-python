# About
This is a simple python script to start or stop EC2 instances that have specific tag name and value.

# Usage
1. Create Lambda function using this script.
2. Add tag name `AutoStartStop` with value `TRUE` to the target EC2 instances.
3. Call the Lambda function from one of AWS services with user parameters like bellow. (e.g. CloudWatch Events)

    ```json
    {
      "Region": "ap-northeast-1",
      "Action": "start"
    }
    ```

    - `Region`: region name that has the target EC2 instances
    - `Action` : "start" or "stop"
    