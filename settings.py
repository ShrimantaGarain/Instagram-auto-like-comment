from random import randint

# Local path to chrome driver
chromedriver_path = "cdrive/chromedriver.exe"

# List of hashtags to go through
hashtag_list = ['#solotravel','camping','indiaplaces']

# List of comments to be randomly chosen from
comments_list = ['Love this!', 'Nice shot :)', 'Amazing~', 'Looks great! :)', 'Beautiful']
# Number of posts to go through per hashtag
number_of_posts = 100

# Chance of commenting on photo
chance_to_comment = 2

# Time to wait in between processing instagram posts in seconds
wait_between_posts = randint(7, 16)

# Time to wait in between liking a post and commenting on it in seconds
wait_to_comment = randint(10, 20)
