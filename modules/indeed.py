from playwright.sync_api import sync_playwright
import random
import time
from utils.helpers import random_sleep

class IndeedAutomata:
    def __init__(self, email, password, headless=True):
        self.email = email
        self.password = password
        self.headless = headless

    def search_and_apply(self, keywords, location, max_jobs=3):
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=self.headless,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--disable-infobars",
                    "--no-sandbox",
                    "--disable-dev-shm-usage"
                ]
            )

            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            # Disable all timeouts
            page.set_default_timeout(0)
            page.set_default_navigation_timeout(0)

            print("[Indeed] Opening Indeed...")
            page.goto("https://www.indeed.com/", wait_until="domcontentloaded")
            random_sleep()

            # Search for jobs
            print(f"[Indeed] Searching for '{keywords}' in '{location}'")
            page.fill("input[name='q']", keywords)
            random_sleep()
            page.fill("input[name='l']", location)
            random_sleep()
            page.click("button[type='submit']")
            random_sleep(4, 8)

            # Collect job links
            job_cards = page.query_selector_all("a.tapItem")
            print(f"[Indeed] Found {len(job_cards)} jobs. Applying to first {max_jobs}...")
            
            for i, card in enumerate(job_cards[:max_jobs]):
                try:
                    card.click()
                    random_sleep(4, 8)

                    # Switch to job view
                    job_title = page.query_selector("h1.jobsearch-JobInfoHeader-title")
                    if job_title:
                        print(f"[Indeed] Applying to: {job_title.text_content().strip()}")

                    # Check for easy apply button
                    apply_btn = page.query_selector("button:has-text('Apply now'), button:has-text('Easily apply')")
                    if apply_btn:
                        apply_btn.click()
                        random_sleep(3, 6)
                        print("[Indeed] Applied (Easy Apply).")
                    else:
                        print("[Indeed] Skipped (No Easy Apply).")

                    random_sleep(2, 6)
                except Exception as e:
                    print(f"[Indeed] Skipped job {i+1}: {e}")
                    continue

            print("[Indeed] Done applying!")
            browser.close()
