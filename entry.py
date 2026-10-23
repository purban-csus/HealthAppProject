#The Python API

from workers import WorkerEntrypoint, Response
from urllib.parse import urlparse


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        # Get the requested URL path
        path = urlparse(request.url).path.rstrip("/")

        #============================================= API Code ================================================
        
        # API route: create a new account
        if path == "/api/register" and request.method == "POST":
            body = await request.json()
            #gets username and passwords
            username = body.get("username", "").strip()
            password = body.get("password", "").strip()
            #in no username or password was entered, display error message
            if not username or not password:
                return Response.json({
                    "success": False,
                    "message": "Username and password are required"
                }, status=400)
            #try to insert data into the users SQL table
            try:
                await self.env.DB.prepare(
                    "INSERT INTO users (username, password) VALUES (?, ?)"
                ).bind(username, password).run()
                
                return Response.json({
                    "success": True,
                    "message": "Account created"
                })
            #if failed, display message
            except Exception:
                return Response.json({
                    "success": False,
                    "message": "That username may already exist"
                }, status=400)

        #=============================================== HTML Files ===============================================
        if path == "/about":
            file_path = "/about.html"
           
        elif path == "/login":
            file_path = "/login.html"
            
        elif path == "/register":
            file_path = "/register.html"

        else:
            file_path = "/index.html"

        # Ask Cloudflare to serve the selected HTML file
        asset_url = f"https://assets.local{file_path}"

        return await self.env.ASSETS.fetch(asset_url)