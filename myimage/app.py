from flask import Flask

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return "<h1>Welcome to the Home Page!</h1>"

# About page
@app.route('/about')
def about():
    return "<h1>About Us</h1><p>We are a small company dedicated to providing great services.</p>"

# Contact page
@app.route('/contact')
def contact():
    return "<h1>Contact Us</h1><p>Feel free to reach out to us at contact@example.com.</p>"

# Services page
@app.route('/services')
def services():
    return """
        <h1>Our Services</h1>
        <ul>
            <li>Web Development</li>
            <li>App Development</li>
            <li>Data Analysis</li>
        </ul>
    """

# FAQ page
@app.route('/faq')
def faq():
    return """
        <h1>Frequently Asked Questions</h1>
        <ul>
            <li><strong>What is Flask?</strong><br>Flask is a micro web framework written in Python.</li>
            <li><strong>How do I install Flask?</strong><br>You can install Flask with pip: <code>pip install Flask</code></li>
        </ul>
    """

# Dynamic URL with a parameter
@app.route('/user/<username>')
def user_profile(username):
    return f"<h1>Welcome, {username}!</h1><p>This is your user profile page.</p>"

# Error page for non-existent routes
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1><p>Sorry, the page you're looking for doesn't exist.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)



