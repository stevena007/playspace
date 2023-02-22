zip customer-split.zip ../Lambda-Functions/customer-splitter/lambda_function.py
awslocal lambda create-function --function-name customer-splitter --zip-file fileb://customer-split.zip --handler lambda_function.lambda_handler --runtime python3.8 --timeout 300 --role arn:aws:iam::000000000000:role/lambda-role
rm customer-split.zip
