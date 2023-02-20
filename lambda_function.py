import os
import json
import urllib.parse
import boto3
 
#only works in Pro localstack :-(
#s3 = boto3.client('s3')
 
#Non Pro Workaround
endpoint_url = "http://" + os.getenv("LOCALSTACK_HOSTNAME") + ":" + os.getenv("EDGE_PORT")
s3 = boto3.client("s3", endpoint_url=endpoint_url)
 
 
def lambda_handler(event, context):
 
    # print("Received event: " + json.dumps(event, indent=2))
    lines_per_file = 1000
    output_folder = 'customer-split'
 
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    orginal_key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'], encoding='utf-8')
 
    print(bucket)
    print(orginal_key)
 
    try:
        tsv_file = s3.get_object(Bucket=bucket, Key=orginal_key)
        tsv_content = tsv_file['Body'].read().decode('utf-8')
        line_count = 0
        file_count = 1
        body = ''
 
        lines = tsv_content.splitlines()
 
        for line in lines:
            line_count += 1
            body += line + '\n'
            if line_count == lines_per_file:
                line_count = 0
                key = orginal_key.split('/')[1].split('.')[0] + \
                    "-" + str(file_count) + ".tsv"
                print("New FileName : " + key)
                file_count += 1
                new_file = output_folder + "/" + key
                s3.put_object(Bucket=bucket, Key=new_file, Body=body)
                body = ''
 
            # print(lineCount)
            # print(line)
 
        if line_count > 0:
            key = orginal_key.split('/')[1].split('.')[0] + \
                "-" + str(file_count) + ".tsv"
            print("New FileName : " + key)
            new_file = output_folder + "/" + key
            s3.put_object(Bucket=bucket, Key=new_file, Body=body)
 
        print("CONTENT TYPE: " + tsv_file['ContentType'])
        return tsv_file['ContentType']
    except Exception as e:
        print(e)
        print("Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.".format(key, bucket))
        raise e
