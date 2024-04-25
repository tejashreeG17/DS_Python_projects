from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Correct import
import time
import random as rand

class GetLinkedInProfileLink():
    def __init__(self):
        self.SEARCH_QUERY = "{} {} {} site:linkedin.com"
        self.GOOGLE_SEARCH = "https://www.google.com/search?q={}"

    def random_sleep(self):
        time.sleep(rand.randint(1, 5))

    def get_linkedin_profile(self, first_name, last_name, company):
        chrome_options = Options()  # Correct instantiation
        chrome_options.headless = True

        driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
        self.random_sleep()

        search_query = self.SEARCH_QUERY.format(first_name, last_name, company)
        driver.get(self.GOOGLE_SEARCH.format(search_query))

        self.random_sleep()
        search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        linkedin_url = None
        self.random_sleep()

        for result in search_results:
            url = result.find_element(By.TAG_NAME, "a").get_attribute("href")
            if "linkedin.com/in/" in url:
                linkedin_url = url
                break
        driver.close()
        return linkedin_url

# Create an instance of the GetLinkedInProfileLink class
linkedin_scraper = GetLinkedInProfileLink()

# Define the details for the LinkedIn profile search
first_name = "John"
last_name = "Doe"
company = "Acme Corp"

# Get the LinkedIn profile URL
profile_url = linkedin_scraper.get_linkedin_profile(first_name, last_name, company)

# Write the profile URL to a text file
if profile_url:
    with open("linkedin_profile.txt", "w") as file:
        file.write(profile_url)
    print("LinkedIn Profile URL written to 'linkedin_profile.txt'")
else:
    print("LinkedIn profile not found.")
