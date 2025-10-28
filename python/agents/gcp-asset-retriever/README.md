# GCP Asset Retriever Agent 

This sample provides a set of APIs designed to act as tools for an [AI agent](https://cloud.google.com/discover/what-are-ai-agents) that retrieves information about your users IAM bindings.

The agent implementation that accompanies this sample was built using Google's [Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

This repo contains the following:

1. API specifications which act as the [tools](https://google.github.io/adk-docs/tools/) used by the agent.
    * These APIs are imported to [Apigee API hub](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub) and then referenced in the agent code using ADK's built-in [ApiHubToolset](https://google.github.io/adk-docs/tools/google-cloud-tools/#apigee-api-hub-tools). This lets agent developers easily turn any existing API from their organization's API catalog into a tool with just a few lines of code.
2. An Apigee [Proxy](https://cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#whatisanapiproxy) implementation that serves the API responses to the agent.
    * This sample proxy implementation returns mock data generated using Gemini.
3. An [Application Integration](https://cloud.google.com/application-integration) process that connects to Google Cloud Rest APIs and queries IAM policy information. 

To try the sample, first follow the instructions below to deploy the API specs, proxies, and integration. Then clone the [agent implementation](https://github.com/google/adk-samples/tree/main/python/agents/auto-insurance-agent) and run it by following the instructions in that repo.


## Pre-Requisites

1. [Provision Apigee X](https://cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro)
2. [Provision Apigee API hub](https://cloud.google.com/apigee/docs/apihub/provision)
3. Configure [external access](https://cloud.google.com/apigee/docs/api-platform/get-started/configure-routing#external-access) for API traffic to your Apigee X instance
4. Enable Vertex AI in your project
5. Make sure the following tools are available in your terminal's $PATH (Cloud Shell has these preconfigured)
    - [gcloud SDK](https://cloud.google.com/sdk/docs/install)
    - [apigeecli](https://github.com/apigee/apigeecli)
    - unzip
    - curl
    - jq
6. Python 3.12+
7. Google Cloud Project with the following roles assigned
  - Apigee Organization Admin
  - Service Usage Consumer
  - Logs Viewer
8. Once you have created your project, [install the Google Cloud SDK](https://cloud.google.com/sdk/docs/install). Then run the following command to authenticate:
```bash
gcloud auth login
```
9. You also need to enable certain APIs. Run the following command to enable:
```bash
gcloud services enable aiplatform.googleapis.com
```
## Agent Setup - Part 1: Deploy API Proxy 

1.  Clone the repository:

    ```bash
    git clone https://github.com/soni-rohan/adk-samples.git
    cd python/agents/gcp-asset-retriever
    ```

    For the rest of this tutorial **ensure you remain in the `python/agents/gcp-asset-retriever` directory**.

2. Edit `env.sh` and configure the following variables:

* `PROJECT_ID` the project where your Apigee organization is located
* `APIGEE_HOST` the externally reachable hostname of the Apigee environment group that contains APIGEE_ENV
* `APIGEE_ENV` the Apigee environment where the demo resources should be created
* `APIGEE_APIHUB_PROJECT_ID` the project where your Apigee organization is located (same as project ID) 
* `APIGEE_APIHUB_REGION` the region where your API Hub is located

Now source the `env.sh` file

```bash
source ./env.sh
```

3. Deploy Apigee API proxy

``` bash
./deploy-adk-asset-retriever.sh
```

## Agent Setup - Part 2: Deploy Integration Process

1) Navigate to the `gcp-asset-retriever` directory
```sh
cd src/gcp-asset-retriever
```
2) In the Google Cloud console, go to the [Application Integration](https://console.cloud.google.com/integrations?_ga=2.161317246.2144651509.1683660420-1351281240.1683660420) page
3) In the navigation menu, click Integrations. The Integrations List page appears.
4) Select an existing integration or create a new integration by clicking Create integration.
If you are creating a new integration:
    i) Enter the name `asset-retrieval-adk` and description in the Create Integration dialog.
    ii) Select a Region for the integration from the list of supported regions.
    iii) Click Create.
This opens the integration in the integration designer.
5) In the integration designer, click `Upload/download menu` and then select `Upload integration`.
7) In the file browser dialog, select `adk-asset-retriever.json`, and then click Open. A new version of the integration is created using the uploaded file.
8) In the integration designer, click Test.
9) Click Test integration. This runs the integration and displays the execution result in the Test Integration dialog.

## Running the Agent Locally

You can run the agent locally using the `adk` command in your terminal:

1.  To run the agent from the CLI:

    ```bash
    adk run gcp-asset-retriever-agent
    ```

2.  To run the agent from the ADK web UI:

    ```bash
    adk web
    ```
    Then select the `gcp-asset-retriever-agent` from the dropdown.

