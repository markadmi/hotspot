from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_204')
@app.route('/ncsi.txt')
def captive_portal_check():
    return redirect(url_for('index'), code=302)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    code = request.form.get('code')
    if code == '12345':
        return "تم الاتصال بنجاح! يمكنك تصفح الإنترنت الآن."
    return "الكود غير صحيح، يجدر المحاولة مجدداً."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
