from distutils.command.config import config
from inspect import signature
from unittest import result
import boto3
from botocore.client import Config

from constants import BUCKET_DELIVERY


def upload(permission=None):
    s3 = boto3.resource("s3", config=Config(signature_version="s3v4"))

    data = open("PuestosPrueba.csv", "rb")

    res = s3.Bucket(BUCKET_DELIVERY).put_object(
        Key="Puestos.csv", Body=data, ACL=permission
    )

    print("done", res)
    return res


if __name__ == "__main__":
    upload(permission="public-read")
