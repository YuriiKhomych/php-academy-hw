from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

import csv

import os
from datetime import datetime

chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "chromedriver")
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://stackoverflow.com/")

topics = driver.find_elements_by_class_name("question_short")

search_input = driver.find_element_by_name("q")
search_input.send_keys("python 3 selenium new" + Keys.RETURN)

# driver.set_window_size(414, 736)


topics = driver.find_elements_by_class_name("question-summary")

for topic in topics:
    title_element = topic.find_element_by_css_selector(".result-link")
    title = title_element.text
    url = topic.find_element_by_css_selector("div.result-link span a")
    url.click()
    content = driver.find_element_by_id("content")
    viewed = content.find_element_by_css_selector("p.label-key b")
    driver.back()
    print(viewed)
    # I can`t go back in my browser history


    #     voted = \
    #     topic.find_element_by_class_name("vote-count-post").text
    #
    #     published_string = topic.find_element_by_class_name("relativetime").get_attribute("title")[:-1]
    #     published_datetime = datetime.strptime(published_string, "%Y-%m-%d %H:%M:%S")
    #     published_date = published_datetime.strftime("%d-%m-%Y")
    #
    #     answers = topic.find_element_by_class_name("excerpt").text
    #
    #     tags = topic.find_element_by_css_selector(".summary .tags").text
    #     #answers_count = topic.find_element_by_css_selector("div.status strong").text
    #
    #     data = {
    #         "title": title,
    #         "url": url,
    #         "voted": voted,
    #         "published date": published_date,
    #         "answers": answers,
    #         "tags": tags
    #         #"answers_count": answers_count
    #     }
    #     with open('stackoverflow.csv', 'a') as csvfile:
    #         fieldnames = ['title', 'url','voted','published date','answers','tags']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writerow(data)
    # try:
    #     next_button = driver.find_element_by_css_selector("a span.page-numbers.next")
    #     next_button.click()
    # except:
    #     print("Last page")
    #     break


#driver.quit()