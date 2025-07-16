from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
from newspaper import Article
from bs4 import BeautifulSoup
import markdown
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Flask Setup
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

# Route: Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('summarize'))
        else:
            flash("❌ Invalid credentials")
    return render_template('login.html')

# Route: Summarizer
@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    summary = None
    file_path = None

    if request.method == 'POST':
        url = request.form['url']
        language = request.form['language']
        try:
            article = Article(url)
            article.download()
            article.parse()

            prompt = f"""Summarize the following article in {language} with sections:
            Headline, Summary, Key Events, and Conclusion.

            Article Text:
            {article.text}
            """

            response = model.generate_content(prompt)

            html = markdown.markdown(response.text)
            soup = BeautifulSoup(html, "html.parser")
            summary = soup.get_text()

            file_path = "summarized_article.txt"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(summary)

        except Exception as e:
            flash(f"❌ Error: {e}")
    
    return render_template('summarize.html', summary=summary, file_path=file_path)

# Route: Download
@app.route('/download')
def download():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return send_file("summarized_article.txt", as_attachment=True)


# Route: About Us
@app.route('/about')
def about():
    return render_template('about.html')

# Route: Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment, default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)

