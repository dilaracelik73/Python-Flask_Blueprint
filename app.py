from flask import Flask, render_template
from blueprints.user_blueprint import user_bp
from blueprints.product_blueprint import product_bp
#yukarıdaki blueprint'ler blueprint dosyasındaki .py dosyalarına ve onların
#bluepprint yapılarına ulaşabilmek adına import edildi.

app = Flask(__name__)
#aşağıda / işsretinin başındaki yapılar belirtilerek sürekli yazılması önlendi ve yönlendirilmeler yapıldı.
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(product_bp,url_prefix="/product")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
