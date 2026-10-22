
from workers import WorkerEntrypoint, Response
from urllib.parse import urlparse


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        # Get the requested URL path
        path = urlparse(request.url).path.rstrip("/")

        #============================================= API Code ================================================
        


        #=============================================== HTML Files ===============================================
        if path == "/about":
            file_path = "/about.html"
           
        elif path == "/login":
            file_path = "/login.html"

        else:
            file_path = "/index.html"

        # Ask Cloudflare to serve the selected HTML file
        asset_url = f"https://assets.local{file_path}"

        return await self.env.ASSETS.fetch(asset_url)
