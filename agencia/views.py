from django.shortcuts import render

# Create your views here.

def home (requesst):
    """
    Render a simple html document as home page
    """
    template_name = '''
    <html>
        <head>
            <title>Simple DeMoTo</title>
        <head>
        <body>
            <header>
                <h2>DeMoTO - simple last mile delivery</h2>
            </header>
            <p> This is a sample app</>
        </body>
    </html>
    '''
    return render(request, template_name)
