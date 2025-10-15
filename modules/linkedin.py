# modules/linkedin.py
from modules.base_platform import BasePlatform
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from utils.utils import random_sleep
import time

class LinkedInPlatform(BasePlatform):
    def __init__(self, storage, config, headless=False):
        super().__init__(storage, config)
        self.email = config.get("linkedin_email")
        self.password = config.get("linkedin_password")
        self.headless = headless

    def login(self, page):
        page.goto("https://www.linkedin.com/login", timeout=0)
        page.fill("input#username", self.email)
        page.fill("input#password", self.password)
        page.click("button[type='submit']")
        # انتظار بسيط عشوائي بدل ثابت
        try:
            page.wait_for_selector("div[role='main']", timeout=0)
        except PlaywrightTimeout:
            print("Login may have failed or two-step is enabled.")
        # بعد التسجيل، انتظر فترة عشوائية
        delay = random_sleep(2, 6)
        print(f"[debug] post-login delay: {delay:.2f}s")

    def apply_to_job(self, page):
        """
        مثال: محاولة الضغط على Easy Apply وSubmit — يمكن فشلها حسب نوع النموذج.
        تُرجع True لو نجحت، False إن لم تنجح أو لا وجود Easy Apply.
        """
        try:
            if page.is_visible("button:has-text('Easy Apply')"):
                page.click("button:has-text('Easy Apply')")
                random_sleep(2, 6)

                # مثال: محاولة إيجاد زر Submit أو Next
                if page.is_visible("button:has-text('Submit application')"):
                    page.click("button:has-text('Submit application')")
                    random_sleep(2, 6)
                    return True

                # بعض التطبيقات تطلب مراحل: اضغط Next حتى تظهر Submit
                for _ in range(5):
                    if page.is_visible("button:has-text('Next')"):
                        page.click("button:has-text('Next')")
                        random_sleep(2, 6)
                    if page.is_visible("button:has-text('Submit application')"):
                        page.click("button:has-text('Submit application')")
                        random_sleep(2, 6)
                        return True
            return False
        except Exception as e:
            print("apply_to_job error:", e)
            return False

    def search_and_apply(self, keywords="Software Engineer", location="United Arab Emirates", max_jobs=5):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--disable-infobars",
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ]
    )
            context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ""(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",ignore_https_errors=True)
            page = context.new_page()
            self.login(page)
            # توجه لصفحة البحث
            search_url = f"https://www.linkedin.com/jobs/search/?keywords={keywords.replace(' ','%20')}&location={location.replace(' ','%20')}"
            page.goto(search_url)
            random_sleep(2, 6)

            # احصل قائمة الوظائف الظاهرة
            jobs = page.query_selector_all("ul.jobs-search__results-list li")
            count = 0
            for job in jobs:
                if count >= max_jobs:
                    break
                try:
                    job.click()
                    random_sleep(2, 6)
                    # link:
                    job_link = page.url
                    # get title & company (محاولة بسيطة)
                    title = ""
                    company = ""
                    try:
                        title_el = page.query_selector("h2.topcard__title")
                        if title_el:
                            title = title_el.inner_text().strip()
                        comp_el = page.query_selector("a.topcard__org-name-link") or page.query_selector("span.topcard__flavor")
                        if comp_el:
                            company = comp_el.inner_text().strip()
                    except Exception:
                        pass

                    applied = self.apply_to_job(page)
                    status = "applied" if applied else "skipped"
                    self.storage.add_application("linkedin", title, company, job_link, status=status)
                    print(f"[LinkedIn] {title} at {company} -> {status}")
                    count += 1
                    random_sleep(2, 6)
                except Exception as e:
                    print("Error iterating job:", e)
            browser.close()
