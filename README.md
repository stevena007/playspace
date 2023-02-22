# playspace

1 - Install localstack -> pip3 install localstack

2 - Install AWS CLI

    mkdir tmp
    cd tmp
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install

3 - Install AWSLOCAL

    pip install awscli-local

4 - Configure Dummy Local Stack Profile

    aws configure --profile default

        AWS Access Key ID [None]: test
        AWS Secret Access Key [None]: test
        Default region name [None]: ap-southeast-2
        Default output format [None]: 




