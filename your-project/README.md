<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Do we know the energy we consume? How is it produced? 

# Spanish Electricity Market Analysis 
*Íngrid Munné Collado*

*Data Analytics June 2019*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-/-questions)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

<a name="project-description"></a>

## Project Description
Our world is consuming more and more energy everyday, and we are running out of resources. On July 30th we have already consumed all the resources the world can produce for the entire year.
This project wants to analyse the way electricity is produced and hence consumed in Spain. Moreover, we also want to see if Spain is on the path towards the European Comission's goals for 2020, also called 20-20-20. This roadmap states that by 2020 we should: 

- Increase our energy efficiency by 20%
- Cut our $CO_2$ emissions by 20%
- Reduce our energy 

The Spanish TSO (Transmission System Operator) is called REE is the entity that regulates the balance between generation and demand. By means of data analytics, an exploratory data analysis is developed, to better understand the behaviour of the Spanish electricity market. 

<a name="hypotheses-/-questions"></a>

## Hypotheses / Questions

The main questions to be answered in this project are the following ones:  

- Has the electricity consumption increased since 2014? 
- Is seasonality electricity consumption significant in the Spanish electricity curve? 
- Is there an increase on renewable energy sources (RES) in the electricity share? 
- Are we on the path towards 20-20-20 goals? 

<a name="dataset"></a>

## Dataset
The data has been collected from the Spanish TSO website, on the transparency platform. The file type is a csv file, containing the data between 2015 and 2018. Data from 2014 has been obtained from Kaggle.

[Dataset REE](https://www.esios.ree.es/en/analysis/1293?vis=2&start_date=25-07-2019T00%3A00&end_date=25-07-2019T23%3A50&compare_start_date=24-07-2019T00%3A00&groupby=minutes10&compare_indicators=545,544) 

[Dataset Kaggle](https://www.kaggle.com/manualrg/spanish-electricity-market-demand-gen-price) 


<a name="workflow"></a>

## Workflow
The defined workflow follows different steps:
1. Topic choice and definition of tasks and questions. 
2. Data acquisition (REE TSO).
3. Data cleaning and export to SQL Workbench
4. Exploratory Data Analysis (EDA)
5. Hypotheses Testing
6. Data Visualization
7. Answering questions 

<a name="organization"></a>

## Organization
In order to develop this project some organization has been defined:
- All the tasks have been defined and planified using Trello. 
- A mentor has been assigned to follow the development of the project, to provide suggestions and feedback throughout the entire project.
- Good practises has been defined and followed to perform the data analysis:
    - PEP 8 
    - snake_case variables definition
    - All the coding scripts will be done on Jupyter Notebook
    - Visualization done by means of Matplotlib and Seaborn. 

### Repository Organization

This repository is structured in different folders and scripts: 

- Your project folder: 
    - README.md 
        The file you are currently reading, with an overview of the entire project. 
    - Datasets:
        Here you can find the original datasets, with raw data from REE. 
    - cleaned_data:
        Here you can find the final datasets with the cleaned data ready for visualization and Exploratory Data Analysis. 
    - Figures: 
        All the figures that have been used for the presentation and the figures that has been done under the analysis part of the project
    - Project_W5_Data_Wrangling.ipynb
        Jupyter notebook with all the data collection and data cleaning. 
    - Project_W5_Data_Visualization_Paper.ipynb
        Jupyter notebook with all the Exploratory Data Analysis and Data Visualization. 
        It is structured as a paper, with all the explanations about the data analysis. 

<a name="links"></a>

## Links

[Repository](https://github.com/wobniarin/Project-Week-5-Your-Own-Project)  
[Slides](https://slides.com/ingridmunnecollado/project-4-electricity-market-analysis)  
[Trello](https://trello.com/invite/b/eMtJ3FEv/971369a4011b84485d871090f1806929/project-4-electricity-market-data)  
[Medium](https://medium.com/@ingridmunne/is-your-electricity-consumption-20-20-20-efd7078b81ec?sk=e632d1fc56f32aaff28b75185427ed8f)