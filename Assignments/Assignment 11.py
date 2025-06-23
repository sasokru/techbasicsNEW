# Code Study: LinkedIn Job Scraper

## Repository I found interesting
[Python-Projects by ahmedmujtaba1](https://github.com/ahmedmujtaba1/Python-Projects)

## File Analysis
`linkedin_scraper/linkedin_scraper.ipynb`

## Project Purpose
The project is a LinkedIn job scraper that automatically navigates job listings, clicks through each post, extracts key job information, and saves it to a CSV file.

## Code Summary
The script:
- Uses Selenium to automate browser interactions.
- Scrapes job titles, locations, companies, employment types, and full descriptions.
- Handles pagination to scrape multiple pages.
- Saves all the scraped data into a CSV file.

## Key Python Patterns (quite a bit more than we learned )
- **Selenium Automation:** Automates browser clicks, scrolling, and input.
- **WebDriverWait:** Efficiently waits for elements to load instead of using fixed sleep timers.
- **Exception Handling:** Ensures that if elements are temporarily unavailable, the scraper retries or continues.
- **Action Chains:** Allows for advanced interactions like moving to specific elements before clicking.

## Interesting learnings i took from this / had to look up seperately
- How to use Selenium’s `WebDriverWait` to wait for dynamic web elements.
- How to navigate complex web pages using XPATH.
- How to write scraped data directly to a CSV file.
- How to handle infinite scroll or pagination using Selenium.

## New syntax I researched
- `WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH, "xpath")))`
   *Waits until a specific element is visible.*

- `ActionChains(driver).move_to_element(element).perform()`
   *Moves the mouse to an element, which is useful when elements need to be in view to be clickable.*

- `co.add_experimental_option("detach", True)`
   *Keeps the browser open after the script finishes.*

## Overall thoughts
I found this project useful to understand how web scraping works on dynamic websites like LinkedIn. The use of Selenium, XPATH navigation, and exception handling were particularly interesting and helpful for building robust scrapers.

## Link to File
[View File](https://github.com/ahmedmujtaba1/Python-Projects/blob/main/linkedin_scraper/linkedin_scraper.ipynb)