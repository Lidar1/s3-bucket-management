import boto3
import uuid

# הגדרות וחיבור ל-S3
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': current_region}
    )
    return bucket_name, bucket_response

def delete_all_objects(bucket_name):
    bucket = s3_resource.Bucket(bucket_name)
    bucket.objects.delete()
    print(f"Deleted all objects in bucket {bucket_name}")

if __name__ == "__main__":
    # דוגמת שימוש בפונקציות
    bucket_name, _ = create_bucket('myappbucket-', s3_resource)
    print(f"Created bucket {bucket_name}")
    delete_all_objects(bucket_name)
    s3_resource.Bucket(bucket_name).delete()
    print(f"Deleted bucket {bucket_name}")
