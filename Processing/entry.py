#   The Python API
#   This is the code responsible for the backend page redirecting and database update and retrieval.
   
#   It is divided into:

#   1. ===account creteion===
#           users create a new account with a unique ID and password 

#   2. ===login validation===
#           users enter their login and password and the API matches the inputs with stored data in the DB   

#   3. ===logout===
#           the login cookie is set to a blank value and the user is redirected to the login screen 

#   4.===get data===
#           gets the data from the database

#   5.===set steps===
#           record the steps data to the SQL database

#   6.===set calories===
#           record the calories data to the SQL database

#   7.===HTML routing===
#           redirects the user based on the url



from workers import WorkerEntrypoint, Response
from urllib.parse import urlparse
from http.cookies import SimpleCookie

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        # Get the requested URL path
        path = urlparse(request.url).path.rstrip("/")

        
# 1. ================================================ API create a new account ================================================

        if path == "/api/register" and request.method == "POST":
            body = await request.json()
            #gets username and passwords from the input boxes
            username = body.get("username", "").strip()
            password = body.get("password", "").strip()
            #if no username or password was entered, display error message
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
                
# 2. ================================================ API login validation ================================================
        
        #API login username/password
        if path == "/api/login" and request.method == "POST":
            body = await request.json()
            
            #gets username and passwords from input boxes
            username = body.get("username", "").strip()
            password = body.get("password", "")
            
            #SQL code to select the data from the users table that match the inputs
            user_id = await self.env.DB.prepare(
                """
                SELECT user_id FROM users WHERE username = ? AND password = ? """          
            
            ).bind(username,password).first("user_id")
            
            #if user id is not in database or was entered incorrectly, display error
            if user_id is None:
                return Response.json({"success": False, "message": "Invalid username or password"}, status=401)
            
            #store the user id in a cookie for the duration of the login session
            headers = {
                "Set-Cookie": (
                    f"user_id={user_id}; "
                    "Path=/; "
                    "HttpOnly; "
                    "SameSite=Lax"
                )
            }
            
            #if username and password are correct, display success
            return Response.json({
                "success": True,
                "message": "Login successful"
            }, headers=headers)
        
# 3. ================================================ API log out ================================================
        
        # API log out by setting cookie to nothing
        if path == "/api/logout" and request.method == "POST":
            headers = {
                "Set-Cookie": (
                    "user_id=; "
                    "Path=/; "
                    "HttpOnly; "
                    "SameSite=Lax; "
                    "Max-Age=0"
                )
            }

            return Response.json({"success": True}, headers=headers)
            
# 4. ================================================ API get data from DB ================================================
        
        #use the user_id stored in the cookie to get data crom the DB
        if path == "/api/today" and request.method == "GET":
            cookie_header = request.headers.get("Cookie") or ""
            cookies = SimpleCookie(cookie_header)
            
            #if the user isnt logged in, display error message
            if "user_id" not in cookies:
                return Response.json({
                    "success": False,
                    "message": "Not logged in"
                }, status=401)

            try:
                user_id = int(cookies["user_id"].value)
            except ValueError:
                return Response.json({
                    "success": False,
                    "message": "Invalid user session"
                }, status=401)

            #get steps and calorie data from the SQL database by user_id and todays date
            row = await self.env.DB.prepare(
                """
                SELECT steps, calories
                FROM daily_health
                WHERE user_id = ?
                  AND entry_date = date('now')
                """
            ).bind(user_id).first()

            #if a row has no data, substitute it with a 0
            if row is None:
                return Response.json({
                    "success": True,
                    "steps": 0,
                    "calories": 0
                })

            #returns the calories and steps as variables
            return Response.json({
                "success": True,
                "steps": row["steps"],
                "calories": row["calories"]
            })

#5. =========================================== API record user steps to DB =================================
        
        #on the steps page, the login cookie is used to post data into the correct user_id
        if path == "/api/steps" and request.method == "POST":
            cookie_header = request.headers.get("Cookie") or ""
            cookies = SimpleCookie(cookie_header)
            
            #if the cookie is not available, display error message
            if "user_id" not in cookies:
                return Response.json({
                    "success": False,
                    "message": "Not logged in"
                }, status=401)

            user_id = int(cookies["user_id"].value)

            #store the enetered number into a variable
            body = await request.json()
            steps = int(body.get("steps", 0))
            
            #if the variable is negative, display an error message
            if steps < 0:
                return Response.json({
                    "success": False,
                    "message": "Steps cannot be negative"
                }, status=400)
            
            #the SQL insert statement using the user_id and steps as values
            await self.env.DB.prepare(
                """
                INSERT INTO daily_health (user_id, entry_date, steps)
                VALUES (?, date('now', '-8 hours'), ?)
                ON CONFLICT (user_id, entry_date)
                DO UPDATE SET steps = daily_health.steps + excluded.steps
                """
            ).bind(user_id, steps).run()

            #displays the steps after the update
            return Response.json({
                "success": True,
                "steps": steps
            })

#6. =========================================== API record user calories to DB =================================
        
        #on the calories page, the login cookie is used to post data into the correct user_id
        if path == "/api/calories" and request.method == "POST":
            cookie_header = request.headers.get("Cookie") or ""
            cookies = SimpleCookie(cookie_header)
            
            #if the cookie is not available, display error message
            if "user_id" not in cookies:
                return Response.json({
                    "success": False,
                    "message": "Not logged in"
                }, status=401)

            user_id = int(cookies["user_id"].value)
            
            #store the enetered number into a variable
            body = await request.json()
            calories = int(body.get("calories", 0))

            #if the variable is negative, display an error message
            if calories < 0:
                return Response.json({
                    "success": False,
                    "message": "Calories cannot be negative"
                }, status=400)

            #the SQL insert statement using the user_id and calorie as values
            await self.env.DB.prepare(
                """
                INSERT INTO daily_health (user_id, entry_date, calories)
                VALUES (?, date('now', '-8 hours'), ?)
                ON CONFLICT (user_id, entry_date)
                DO UPDATE SET calories = daily_health.calories + excluded.calories
                """
            ).bind(user_id, calories).run()

            #displays the calories after the update
            return Response.json({
                "success": True,
                "calories": calories
            })
            
#7. =========================================== HTML Files ===================================================
        
        #redirecting based on url ending
        if path == "/about":
            file_path = "/about.html"
           
        elif path == "/login":
            file_path = "/login.html"
            
        elif path == "/register":
            file_path = "/register.html"
            
        elif path == "/home":
            file_path = "/home.html"
          
        else:
            file_path = "/index.html"

        #asks cloudflare to serve the selected file
        asset_url = f"https://assets.local{file_path}"

        return await self.env.ASSETS.fetch(asset_url)