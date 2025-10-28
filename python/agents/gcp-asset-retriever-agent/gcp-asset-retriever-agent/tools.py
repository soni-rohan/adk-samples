# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from dotenv import load_dotenv
import google.auth 
from google.adk.tools.apihub_tool.apihub_toolset import APIHubToolset
from google.adk.auth import AuthCredential, AuthCredentialTypes, OAuth2Auth
from fastapi.openapi.models import OAuth2
from fastapi.openapi.models import OAuthFlowAuthorizationCode
from fastapi.openapi.models import OAuthFlows


from google.adk.auth.auth_credential import HttpCredentials, HttpAuth

load_dotenv()

# --- ENVIRONMENT VARIABLES ---
PROJECT_ID=os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION=os.getenv("GOOGLE_CLOUD_LOCATION")
API_HUB_LOCATION=f"projects/{PROJECT_ID}/locations/{LOCATION}/apis"

oauth2_scheme = OAuth2(
   flows=OAuthFlows(
      authorizationCode=OAuthFlowAuthorizationCode(
            authorizationUrl=f"https://accounts.google.com/o/oauth2/v2/auth",
            tokenUrl=f"https://oauth2.googleapis.com/token",
            scopes={
                f"https://www.googleapis.com/auth/cloud-platform" : "default",
            }
      )
   )
)
auth_credential = AuthCredential(
  auth_type=AuthCredentialTypes.OAUTH2,
  oauth2=OAuth2Auth(
      client_id="7447300960-oo4u3r3b4c6cb06uu79r4b6j8fhsf23k.apps.googleusercontent.com", #TODO: replace with client_id
      client_secret="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", #TODO: replace with client_secret
      redirect_uri="https://8000-cs-344775984868-default.cs-us-east1-rtep.cloudshell.dev/dev-ui/" #TODO: replace with redirect_uri
  )
)

# --- 3. CONFIGURE THE APIHubToolset ---
# Pass the constructed HttpAuth object to both scheme and credential parameters.
asset = APIHubToolset(
    name="asset_retriever_api", #can be any name
    description="Retrieves Assets based on IAM",
    apihub_resource_name=f"{API_HUB_LOCATION}/2bbd39dd-e1e2-4df2-92d7-84e2abc0cc95",
    auth_scheme=oauth2_scheme,
    auth_credential=auth_credential
)

