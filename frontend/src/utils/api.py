import httpx
import os
from dotenv import load_dotenv
from typing import Optional, Dict, Any

# Load environment variables
load_dotenv()

class APIClient:
    def __init__(self):
        self.base_url = os.getenv("API_URL", "http://localhost:8000")
        self.headers = {
            "Content-Type": "application/json",
        }
        self.client = httpx.AsyncClient(base_url=self.base_url, headers=self.headers)

    async def set_auth_token(self, token: str):
        """Set authentication token for requests"""
        self.headers["Authorization"] = f"Bearer {token}"
        self.client = httpx.AsyncClient(base_url=self.base_url, headers=self.headers)

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None):
        """Make GET request to API endpoint"""
        async with self.client as client:
            response = await client.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()

    async def post(self, endpoint: str, data: Dict[str, Any]):
        """Make POST request to API endpoint"""
        async with self.client as client:
            response = await client.post(endpoint, json=data)
            response.raise_for_status()
            return response.json()

    async def put(self, endpoint: str, data: Dict[str, Any]):
        """Make PUT request to API endpoint"""
        async with self.client as client:
            response = await client.put(endpoint, json=data)
            response.raise_for_status()
            return response.json()

    async def delete(self, endpoint: str):
        """Make DELETE request to API endpoint"""
        async with self.client as client:
            response = await client.delete(endpoint)
            response.raise_for_status()
            return response.json()

# Singleton instance
_api_client: Optional[APIClient] = None

def get_api_client() -> APIClient:
    """Get or create API client instance"""
    global _api_client
    if _api_client is None:
        _api_client = APIClient()
    return _api_client