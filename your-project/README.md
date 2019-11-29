<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Rental Prices in Barcelona - "Should I stay or should I go now"
*Elliott Coyne*

*Data Analytics, Barcelona, November 2019*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
According to local hearsay, long term residential apartment rental prices in Barcelona have risen in the recent past. As a new arrival in the city I wanted to confirm if this is correct and quantify the impact. If the quantitiave research confims there is an increase in long term prices then it would be beneficial to see if there is a similar impact on short term rental prices (i.e. Airbnb properties).

Gràcia 

## Questions & Hypotheses
From my knowledge of the city's rental prices (prior to my arrival in January 2019) my assumption is that there has been an increase in long term rental prices. This lead to me to formulate my initial questions:
*1. Have long term rental prices increased in the recent past?*
*2a. Have short term rental prices increased/ decreased at a similar proportion to long term rentals?*
During the course of the research the focus of the second question had to be realsigned to:
*2b. What affect does nightly price have on the length of time short term properties appear on the Airbnb platform?*

## Dataset
What dataset (or datasets) did you use? What are the different sources you used (e.g. APIs, web scrapping, etc.)? Provide links to the data if available and describe the data briefly.
The long term rental pricing information is sought from OpenData BCN who provide historic information on long term rental prices, aggregated by barrio. The available data spanned 2014 - 2018 split by quater.
Short term rental data came from Airbnb (via scraping site, http://insideairbnb.com/). This site itseld provides data scrapes from the Airbnb platform. The scapres occured sporadically but there was consistent data available form April 2014 - September 2019 (spanning 54 months).

For both datasets, the W Get module was installed and used to download multiple files from the respective websites (using a for loop). In total 44 files were downloaded, concatenated, cleaned and analysed.

## Workflow
Outline the workflow you used in your project. What are the steps you went through?
Following the selection of the topic probelm and questions, suitable data was sourced. This data was then downloaded (programatically), extracted (where required), loaded into dataframes, cleaned and analysed. The cleaning process was carried out simultaneously to Exploratory Data Analysis (EDA); cleaning and removing outliers whilst reviewing the data appeared to be the most efficient use of time.

## Organization
In order to organise the project, a kanban board from Trello was used. The link to the Trello board can be found below.

The respository root folder has one main working directory, 'your-project' which is divded into XXX sub-folders. This Readme file resides in the root directory. Below is an explanation of each sub folder and their respective contents:
* Data - Raw CSV and zip files used for this project.
* Code - The Jupyter Notebook files used to obtain, clean and analyse the data.

## Links
Please find all relevant links for this project below:
[Repository](https://github.com/tristar82/Project-Week-5-Your-Own-Project)
[Slides](https://slides.com/)
[Trello](https://trello.com/b/5O45JOM2/project-4-bcn-rental-data)
[Medium Article](xxxxx)
**Data Sources**
[OpenData BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/est-mercat-immobiliari-lloguer-mitja-mensual)
[Insideairbnb](http://insideairbnb.com/get-the-data.html)
**Libraries Required to Run Code**
[W Get](https://pypi.org/project/wget/)
[GZip](https://docs.python.org/3.0/library/gzip.html)
[Plotly](https://plot.ly/python/v3/ipython-notebooks/cufflinks/)
[Lifelines](https://github.com/CamDavidsonPilon/lifelines)

