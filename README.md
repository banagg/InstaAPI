# InstaAPI

## About
1. An API endpoint which extracts and displays metadata of public posts posted on Instagram when being input a Brand Name and a Product Name.
2. Was made in March 2019 as a code assignment for the internship interview process of a Hong Kong based startup named [EZENCIEL](https://ezenciel.com/).

## Working
1. A custom made Instagram scraping process was used to extract data from Instagram, the link for which can be found [here](https://github.com/rarcega/instagram-scraper).
2. The above mentioned project is *required* to be installed on the system to successfully run the project.
3. The scrapper would retrieve public data from Instagram and InstaAPI would insert all that data into its own SQLite database.
4. Now if a person opens the file **hello.html** then he/she would be able to view the data that was extracted from Instagram by retrieving the same data from our local database (after providing the relevant Brand Name and the Product Name).
