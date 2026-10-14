
from workers import WorkerEntrypoint
from urllib.parse import urlparse


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        # Get the requested URL path
        path = urlparse(request.url).path.rstrip("/")

        # Choose which HTML file to serve
        if path == "/about":
            file_path = "/about.html"

        elif path == "/joanna":
            file_path = "/joanna.html"

        elif path == "/01":
            file_path = "/01.html"
            
        elif path == "/02":
            file_path = "/02.html"

        else:
            file_path = "/index.html"

        # Ask Cloudflare to serve the selected HTML file
        asset_url = f"https://assets.local{file_path}"

        return await self.env.ASSETS.fetch(asset_url)
