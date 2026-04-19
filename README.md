# 🤖 Job Automata

An intelligent automation tool that **searches and applies to jobs** automatically on **LinkedIn** and **Indeed**, using [Playwright](https://playwright.dev/python/) for browser control and realistic human-like actions.

---

## 🚀 Features

✅ Auto login to job platforms  
✅ Searches jobs by keyword and location  
✅ Auto-applies to **Easy Apply** jobs  
✅ Supports **LinkedIn** and **Indeed**  
✅ Uses **random 2–6 second delays** between actions to reduce ban risk  
✅ No timeouts (runs indefinitely until jobs are processed)  
✅ Headless or visible browser modes  

---

## 🏗️ Project Structure


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/job-automata.git
cd job-automata
2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate      # On Windows
source .venv/bin/activate   # On Linux/Mac
3. Install dependencies
pip install -r requirements.txt
4. Install Playwright browsers
playwright install
🧠 Configuration

Open main.py and update your credentials and job preferences:
email = "your_email@example.com"
password = "your_password"

linkedin.search_and_apply(
    keywords="Software Engineer",
    location="Abu Dhabi, United Arab Emirates",
    max_jobs=3
)

indeed.search_and_apply(
    keywords="Software Engineer",
    location="Abu Dhabi",
    max_jobs=3
)
▶️ Run the Bot
python main.py
⚡ Tips for Best Performance

Use headless=False to see what’s happening during runs.

Avoid running too frequently to prevent account restrictions.

Use real delays — the system already includes random 2–6s pauses.

Use your normal IP or trusted VPN (not datacenter proxies).

🧩 Roadmap

 Add support for Bayt.com

 Add support for Naukrigulf.com

 Add YAML configuration file for user settings

 Integrate job progress logging and reporting

🛡️ Disclaimer

This tool is for educational and personal use only.
Automating job applications may violate platform terms of service.
Use responsibly and at your own risk.
📜 License

MIT License © 2025 Adryad

---
pleas add star
## 🧰 Bonus — Requirements File

Create a `requirements.txt` with:

