# InstaAPIv1


InstaAPIv1 is an API endpoint which extracts info about images from Instagram when given a Brand Name & a Product Name. Implemented using the Instagram scraping API whose link can be found [here](https://github.com/rarcega/instagram-scraper) (which is necessary to install to successfully run it). The scraper scrapes 100 items for both product name and the brand name and its maximum value can be changed manually from the code by changing the value in the -m paramater (though increasing the value will increase the time taken by the API to run).

Technologies Used: Python

Libraries Used: Flask, sqlite3, subprocess, pandas

Steps to operate:

1 - Run the mainf.py file

2 - Run the hello.html file which can be found in the templates section.

3 - Enter the Brand Name and the Product Name on the hello.html page.

4 - Wait for the scraping to end and view the extracted data.
