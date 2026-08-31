from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

ENDPOINT = "https://hughmann-6084-resource.openai.azure.com/"
CHAT_DEPLOYMENT = "gpt-5-mini"          # the deployment name you set
EMBED_DEPLOYMENT = "text-embedding-3-small"
API_VERSION = "2024-10-21"              # check docs for the current stable version

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    azure_ad_token_provider=token_provider,   # keyless — no api_key
    api_version=API_VERSION,
)