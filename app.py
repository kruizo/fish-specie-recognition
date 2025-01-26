from flask import Flask, render_template

# Specify static and template folder paths relative to the project root
app = Flask(__name__, 
            static_folder='frontend/static', 
            template_folder='frontend/template', 
            static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')  # Flask will look in 'frontend/template' folder

if __name__ == "__main__":
    app.run(debug=True)
