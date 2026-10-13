from workers import WorkerEntrypoint, Response

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        url = request.url

        if url.endswith("/about"):
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>About - CSC131 Project</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-image:
                            url("https://images.unsplash.com/photo-1519608487953-e999c86e7455");
                        background-size: cover;
                        background-position: center;
                        background-repeat: no-repeat;
                        color: #222;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        min-height: 100vh;
                        margin: 0;
                        text-align: center;
                    }
                    .content {
                        background: white;
                        padding: 40px;
                        border-radius: 15px;
                        box-shadow: 0 4px 15px #0002;
                    }
                    a { color: #1769aa; }
                </style>
            </head>
            <body>
                <div class="content">
                    <h1>About This Project</h1>
                    <p>This is the About HTML page!</p>
                    <p>If you can see this, the URL routing is working.</p>
                    <a href="/">Return to Home</a>
                </div>
            </body>
            </html>
            """
            
        elif url.endswith("/joanna"):
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>About - CSC131 Project</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-image:
                            url("/ju01.jpg");
                        background-size: contain;
                        background-position: center;
                        background-repeat: no-repeat;
                        color: #222;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        min-height: 100vh;
                        margin: 0;
                        text-align: center;
                    }
                    .content {
                        background: rgba(0, 0, 0, 0.65);
                        color: white;
                        padding: 40px;
                        border-radius: 15px;
                        text-align: center;
                    }
                    a { color: #1769aa; }
                </style>
            </head>
            <body>
                <div class="content">
                    <h1>Cupcake Dude</h1>
                    <p>Doesn't he look like he's pooping?</p>
                    <a href="/">Return to Home</a>
                </div>
            </body>
            </html>
            """
        
        
        elif url.endswith("/01"):
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>CSC131 Project</title>
                <style>
                    * {box-sizing: border-box;}
                    html, body {
                        margin: 0;
                        width: 100%;
                        height: 100%;
                    }
                    body {
                        font-family: Arial, sans-serif;
                        background-image:
                            url("https://images.unsplash.com/photo-1519608487953-e999c86e7455");
                        background-size: cover;
                        background-position: center;
                        background-repeat: no-repeat;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }
                    .content {
                        background: rgba(0, 0, 0, 0.65);
                        color: white;
                        padding: 40px;
                        border-radius: 15px;
                        text-align: center;
                    }
                    h1 {margin-top: 0;}
                </style>
            </head>
            <body>
                <div class="content">
                    <h1>Test Page 01</h1>
                    <p>If you can read this, it means you can read!</p>
                    <p><a href="/about">Visit the About page</a></p>
                    <a href="/">Return to Home</a>
                </div>
                </body> 
                </html>
                """
        
        
        else:
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>CSC131 Project</title>
                <style>
                    * {box-sizing: border-box;}
                    html, body {
                        margin: 0;
                        width: 100%;
                        height: 100%;
                    }
                    body {
                        font-family: Arial, sans-serif;
                        background-image:
                            url("https://images.unsplash.com/photo-1519608487953-e999c86e7455");
                        background-size: cover;
                        background-position: center;
                        background-repeat: no-repeat;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }
                    .content {
                        background: rgba(0, 0, 0, 0.65);
                        color: white;
                        padding: 40px;
                        border-radius: 15px;
                        text-align: center;
                    }
                    h1 {margin-top: 0;}
                </style>
            </head>
            <body>
                <div class="content">
                    <h1>CSC131 Project</h1>
                    <p>Hello Chris & Donny, our website is working!</p>
                    <p><a href="/about">Visit the About page</a></p>
                    <p><a href="/joanna">If you're name is Joanna, go here!</a></p>
                    <p><a href="/01">Go to test page 01</a></p>
                </div>
                </body> 
                </html>
                """

        return Response(
            html,
            headers={"Content-Type": "text/html"}
    )

