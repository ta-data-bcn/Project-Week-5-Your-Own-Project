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
The property rental market in Barcelona is well known for having undergone significant price rises in the recent past. With this in mind, I have decided to do an analysis of short and long term rentals to see what the property market is likely to be doing in February, 2020. This is incidently when my current lease is up.

## Questions & Hypotheses
What are the questions you would like to answer with your analysis? What did you feel were the answers to those questions before answering them with data?
Is there a history of price increases in Barcelona?
Is there any correlation between short tem and long term rental prices?

## Dataset
What dataset (or datasets) did you use? What are the different sources you used (e.g. APIs, web scrapping, etc.)? Provide links to the data if available and describe the data briefly.
The long term rental pricing information is sought from OpenData BCN who provide historic information on rental prices, aggregated by barrio. Short term rental data came from AirBNB (via scraping site, http://insideairbnb.com/). In order to relate these twho different dataset, the Insideairbnb data will need to be cleaned and then the price per square meter calculcated using available data.
For both datasets, the WSGet module was installed and used to download multiple files from the respective websites (using a for loop). In total, over 40 files were downloaded, concatenated, cleaned and analysed.

## Workflow
Outline the workflow you used in your project. What are the steps you went through?
Following the selection of the topic probelm and questions, suitable data was sourced. This data was then downloaded (programatically), extracted (where required), loaded into dataframes, cleaned and analysed.

## Organization
How did you organize your work? Did you use any tools like a kanban board?
In order to organise the project, a kanban board from Trello was used. This can be access at XXXXXXXXXXXXX.

What does your repository look like? Explain your folder and file structure.
The respository root folder has one main working directory, 'your-project' which is divded into XXX sub-folders. A Readme file exists in the root directory, the raw data is stores in the 'Data' folder. The working files (Jupyter Notebook) are found in 'Working'.

## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository](https://github.com/tristar82/Project-Week-5-Your-Own-Project)
[Slides](https://slides.com/)
[Trello](https://trello.com/b/5O45JOM2/project-4-bcn-rental-data)
[OpenData BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/est-mercat-immobiliari-lloguer-mitja-mensual)
[Insideairbnb](http://insideairbnb.com/get-the-data.html)

