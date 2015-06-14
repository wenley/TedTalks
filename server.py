
# Main imports
from flask import Flask
app = Flask(__name__)

# Rendering imports
from flask import render_template

@app.route('/')
def main():
  return render_template('main.html')

if __name__ == "__main__":
  app.run()
