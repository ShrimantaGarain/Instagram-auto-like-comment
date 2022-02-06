from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
import sys
from random import randint
from login import *
from settings import *


logging.basicConfig(
    format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# chrome driver Path
browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')
sleep(2)
# login info
username = browser.find_element_by_name('username')
username.send_keys(USERNAME)
password = browser.find_element_by_name('password')
password.send_keys(PASSWORD)

sleep(2)

# login button
browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
try:
    if browser.find_element_by_xpath("//*[@id='slfErrorAlert']"):
        browser.close()
        sys.exit('Error: Login information is incorrect')
    else:
        pass
except:
    pass

sleep(2)

logger.info(f'Logged in to {USERNAME}')
try:
    browser.find_element_by_xpath(
        "//*[@id='react-root']/div/div/section/main/div/div/div/div/button").click()
except Exception:
    pass

sleep(2)
try:
    browser.find_element_by_xpath(
        "/html/body/div[5]/div/div/div/div[3]/button[2]").click()
except Exception:
    pass

sleep(2)
likes = 0
comments = 0

# Index for tags in hashtag list
tag_index = 0

for hashtag in hashtag_list:
    browser.get(
        f'https://www.instagram.com/explore/tags/{hashtag_list[tag_index]}/')
    logger.info(f'Exploring #{hashtag}')
    sleep(5)
    first_thumbnail = browser.find_element_by_xpath(
        "//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]")
    first_thumbnail.click()

    # Go through x number of photos per hashtag
    for post in range(1, number_of_posts):

       # Check if the post is already liked
        # If not, then like, comment, and go to next post
        try:
            browser.find_element(By.XPATH, "//*[contains(@class, 'fr66n')]/button/div/*[*[local-name()='svg']/@aria-label='Unlike']/*").click()
            logger.info("Already liked this post")
        except Exception:
            # Like
            browser.find_element(By.XPATH, "//*[contains(@class, 'fr66n')]/button/div/*[*[local-name()='svg']/@aria-label='Like']/*").click()
            logger.info("Liked")
            likes += 1

            # Random chance of commenting
            do_i_comment = randint(1, chance_to_comment)
            if do_i_comment == 1:
                try:
                    # Comment
                    browser.find_element_by_xpath("//form").click()
                    comment = browser.find_element_by_xpath("//textarea")

                    sleep(wait_to_comment)

                    rand_comment_index = randint(0, len(comments_list))
                    comment.send_keys(comments_list[rand_comment_index])
                    comment.send_keys(Keys.ENTER)
                    logger.info(
                        f"Commented '{comments_list[rand_comment_index]}'")
                    comments += 1

                except Exception:
                    continue
        # Go to next post
        sleep(wait_between_posts)
        # browser.find_element_by_xpath(u'/html/body/div[6]/div[2]/div/div/button').click()
        
        nxt =browser.find_elements_by_xpath(u'/html/body/div[6]/div[2]/div/div/button')
        if len(nxt) > 1:
            nxt[1].click()

        else:
            nxt[0].click()
        logger.info('Getting next post')
        sleep(wait_between_posts)
    tag_index += 1
logger.info(f'Liked {likes} posts')
logger.info(f'Commented on {comments} posts')
