<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Data Analysis of Super Bowl Commercials
*Kevin Forster*

*Data Analytics, Barcelona, 19.2.2020*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
I decided to analyse a part of the super bowl specatacle as the event recently took place and I think it is a topic that most of the audience is interested in. The project is about the development of the commercials in Super Bowl breaks and how much awareness these commercials created in Twitter. 

## Questions & Hypotheses
- By how much has the price of a commercial (30 seconds) during Super Bowl increased?
- Which are the companies that show commercials during Super Bowl in 2020 and in history?
- What kind of products are in the commercials?
- How much awareness is created by the commercials, reflected in tweets on Twitter?
- Which is the company that was mentioned the most on Twitter during Super Bowl?
- Is there any impact of the event on the share value of the companies?

## Dataset
CSV:
- Kaggle: Dataset of Commercial brands and product in Super Bowl History [Link](https://www.kaggle.com/prondeau/superbowlads) 
- Shares: Shares CSV where all the companies with the Ticker were listed. Ticker is a unique 4 letter code what was used for the API to get the share values

Web Scraping
- Viewers and commercial costs in Super Bowl history [Repository]((https://superbowl-ads.com/cost-of-super-bowl-advertising-breakdown-by-year/)
- Twitterscraping via twitter scraper

API:
- alpha_vantage.timeseries to receive the share values in history

## Workflow
- Researched about an interesting topic
- Defined questions
- Researched about dataset
- Created a dataframe with the first csv, started with data wrangling
- Added more data to the dataframe via web scrapping
- Integrated an API to get the share valuefor each brand
- Integrated the twitterscraping to see the impact of the event
- Visualisation in Tableau
- Finishing the presentation and the paper

## Organization
- Jupyter Notebook file, called project4.ipynb: this is the paper where all the cleaned codes are in and also comments are inserted. This is the paper that sums up the project
- csv folder: here are all the input csv and output csv
- Tableau folder: here are all the visualisation that were used for the paper and the presentation


## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository](https://github.com/kevforster/Project-Week-5-Your-Own-Project)  
[Slides](https://slides.com/)  
