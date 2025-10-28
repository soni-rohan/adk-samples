# Environment Variables Config Instructions 

These instructions where to find the values for your environment variables. 

1. Apigee Credentials 

* `PROJECT_ID` the project where your Apigee organization is located, e.g.: apigee-demo-123456
* `APIGEE_ENV` the Apigee environment where the demo resources should be created. You can find this in your Google Cloud Console by going to Apigee -> Environments
* `APIGEE_HOST` the externally reachable hostname of the Apigee environment group that contains APIGEE_ENV. You can find this in your Google Cloud Console by going to Apigee -> Environments -> Environment Groups -> Host Names

2. API Hub Credentials
   
* `APIGEE_APIHUB_PROJECT_ID` the project where your Apigee organization is located (same as project ID) 
* `APIGEE_APIHUB_REGION` the region where your API Hub is located. You can find this in your Google Cloud Console by going to Apigee -> API hub -> Settings -> Plugins -> 3 vertical dots -> See details -> Instance reosurce name 

3. OAuth Client Credentials

a. In your Cloud Shell, first run the following command:
```bash
adk web
```

Click on the hyperlink, e.g,: http://127.0.0.1:8000 in your terminal that opens a local host. Copy the URI in the web server that opens - this is your `REDIRECT_URI`. It typically looks like https://8080-dot-1234567-tp.cloudshell.dev. You need to update the URI in the env.sh file. 

b. Create the OAuth Client in Google Cloud Console:Navigate to the APIs & Services -> Credentials page in the Google Cloud console. Click + Create Credentials -> OAuth client ID. For Application Type, select Web application. Under Authorized redirect URIs, click + Add URI and paste the URL you copied from the step above. Click Create. Copy the generated `CLIENT_ID` and `CLIENT_SECRET` and update the env.sh file. 

