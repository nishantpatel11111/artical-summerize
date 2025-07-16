# Article Summarizer Web App

This is a Flask-based web application that allows users to summarize news articles using Google's Gemini generative AI model. The app provides a simple login system, article summarization, and the ability to download the generated summary.

## Features
- **User Authentication:** Simple login page with hardcoded credentials.
- **Article Summarization:** Enter a news article URL and select a language to generate a summary with sections: Headline, Summary, Key Events, and Conclusion.
- **Download Summary:** Download the generated summary as a text file.
- **Logout:** Securely log out of the session.

## Technologies Used
- Python 3
- Flask
- Newspaper3k
- BeautifulSoup
- Markdown
- Google Generative AI (Gemini)
- dotenv

## Setup Instructions

1. **Clone the repository:**
   ```powershell
   git clone <repo-url>
   cd artical-summerize
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. **Run the application:**
   ```powershell
   python app.py
   ```
   The app will be available at `http://localhost:5000`.

## Usage
1. Go to the login page and enter the credentials:
   - Username: `admin`
   - Password: `1234`
2. Enter the URL of a news article and select the desired language.
3. View the summary and download it as a text file if needed.
4. Use the logout button to end your session.

## File Structure
```
app.py
requirements.txt
templates/
    login.html
    summarize.html
```

## License
This project is for educational purposes only.
