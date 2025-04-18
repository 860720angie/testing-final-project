from playwright.sync_api import sync_playwright
import time

def test_hello_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://localhost:5000/hello-form")

        page.fill("input#name", "Anyelo")
        page.click("text=Say Hello")
        print("✅ System test for /hello-form passed!")
        
        time.sleep(5)  # browser stays open for 5 seconds
        
        browser.close()

if __name__ == "__main__":
    test_hello_form()


