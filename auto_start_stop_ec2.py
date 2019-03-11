import json
import boto3
import traceback

def lambda_handler(event, context):
  try:
    region = event['Region']
    action = event['Action']
    client = boto3.client('ec2', region)
    responce = client.describe_instances(Filters=[{'Name': 'tag:AutoStartStop', "Values": ['TRUE']}])

    target_instans_ids = []
    for reservation in responce['Reservations']:
      for instance in reservation['Instances']:
        tag_name = ''
        for tag in instance['Tags']:
          if tag['Key'] == 'Name':
            tag_name = tag['Value']
            break

        target_instans_ids.append(instance['InstanceId'])

    print(target_instans_ids)

    if not target_instans_ids:
      print('There are no instances subject to automatic start / stop.')
    else:
      if action == 'start':
        client.start_instances(InstanceIds=target_instans_ids)
        print('started instances.')
      elif action == 'stop':
        client.stop_instances(InstanceIds=target_instans_ids)
        print('stopped instances.')
      else:
        print('Invalid action.')

    return {
      "statusCode": 200,
      "message": 'Finished automatic start / stop EC2 instances process. [Region: {}, Action: {}]'.format(event['Region'], event['Action'])
    }
  except:
    print(traceback.format_exc())
    return {
      "statusCode": 500,
      "message": 'An error occured at automatic start / stop EC2 instances process.'
    }

