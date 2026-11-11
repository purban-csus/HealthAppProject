BetterU - Health App Project ( CSC 131 )

This is the official repository for BetterU, a health app created for CSC 131, as part of a collaborative project. BetterU is a web-based health tracking application, allowing you to keep track of caloric and macro-nutrient intake. 

Team Members

-Pawel Urban
-Christopher Mariano
-Donny Zaragoza

Technologies & Tools  Used

-	Cloudflare : host website and provide serverless backend executables
-	Python : utilized for backend API routing and request handling logic
-	Javascript : used for asynchronous API calls
-	HTML: utilized for home pages, login and registration page.
-	CSS: used for custom layout and styling
-	SQL : used to manage login information credentials and entry records


Project structure
|-----about.html	# Project background
|-----calories.html	# Calorie intake template page
|-----entry.py		# Cloudflare Worker handling registration/routing
|-----home.html	# Home page template
|-----login.html	# User authentication interface
|-----register.html 	# Registration interface template
|-----steps.html	# Step Tracking template page
|-----style.html	# Style and background rules


Key Features

Serverless Backend
-	Utilizing python to create a Cloudflare Workers entry

SQL Database 
-	Application connects to cloudflare D1 SQL based database
-	Stores manages login credentials and entry records
