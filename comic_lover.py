import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.gocomics.com/pearlsbeforeswine/2019/08/21'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text)
comic_div = soup.select('picture.item-comic-image')
image_url = comic_div[0].contents[0].attrs['src']
image_res = requests.get(image_url)
image_res.raise_for_status()

image_file = open(os.path.basename(image_url), 'wb')

# for chunk in image_res.iter_content(100000):
#     image_file.write(chunk)
# image_file.close()

#print("comic div is", comic_div)
#print("comic div 0 is", comic_div[0])
# image_url = 'https:' + comic_div[0].contents[1].attrs['src']
# image_res = requests.get(image_url)
# image_res.raise_for_status()
# print(image_res)
#
# image_file = open(os.path.basename(image_url), 'wb')
#
# # so there is finite number of bytes can saved
# for chunk in image_res.iter_content(100000):
#     image_file.write(chunk)
# image_file.close()
#
# # GET PREVIOUS URL
# # a: is the tag
# # []: attributes
# prev_url = soup.select('a[rel="Read More"]')[0]
# url = 'https://www.gocomics.com/pearlsbeforeswine/' + prev_url.get('href')
# # print(prev_url)
# # this will give us the number from the hyperlink reference: 2188
# # print(prev_url.get('href'))
# # take 2188 to append the url
# # url += prev_url.get('href')
#
# print(url)
# sleep(1)

# Write a python program that will download the latest 10 comic images from https://www.gocomics.com/pearlsbeforeswine/
#
# Navigate to the latest page by clicking 'Read More'.
#
# Requirements:
#
# Use BeautifulSoup and the Requests library to download the image like we did in the example.
#
# Extract the link to the previous image with BeautifulSoup/Requests
#
# Write a for loop that will run 10 times, saving the latest comic images in the same location as your python code.
#
# Make sure your program runs before you send it!