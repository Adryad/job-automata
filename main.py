# main.py
from config import CONFIG
from utils.storage import Storage
from modules.linkedin import LinkedInPlatform
from utils.utils import random_sleep
from modules.indeed import IndeedAutomata

def main():
    email = "your_email@example.com"
    password = "your_password"
    storage = Storage(CONFIG["db_path"])
    linkedin = LinkedInPlatform(storage, CONFIG, headless=False)
    linkedin.search_and_apply(keywords="Software Engineer", location="Abu Dhabi, United Arab Emirates", max_jobs=3)
    indeed = IndeedAutomata(email, password, headless=False)
    indeed.search_and_apply(
        keywords="Software Engineer",
        location="Abu Dhabi",
        max_jobs=3
    )
    # مثال: تأخير قصير قبل تشغيل منصة أخرى (إذا أضفت منصات لاحقًا)
    random_sleep(2, 6)

if __name__ == "__main__":
    main()
