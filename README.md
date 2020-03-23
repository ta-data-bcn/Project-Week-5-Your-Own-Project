<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of My Project
*[Your Name]*

*[Your Cohort, Campus & Date]*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The objective of this project is to find out if there is a relation between catastrophies and stock-market changes. First thing is to distinguish two types of disasters: natural and medical disasters.

## Questions & Hypotheses
Search for a pattern in stock-market as reaction to disasters.
* Is there a direct relation?
* Do all markets react the same way?
* Do markets react the same way to a natural disaster (e. tsunami) and a medical disaster (covid-19)?

## Dataset
Main origin of data (web scrapping):
[https://markets.businessinsider.com](https://markets.businessinsider.com)

## Workflow
* scrapp data from web (about 15 years of each stock-market)
* visualisation of all markets during this lapse of time
* search for patterns that make them go on the same way
* search for patterns during disasters
* try to find out if there are outliers or all markets work in somehow the same way
* find patterns during top natural and medical disasters over the last 15 years

## Organization
- all data is stored in path /data/csv
- basic used queries stored in /data/sql
- stock-market analysis is stored as follows
    - 1. scrap data from web and store it in csv files
    - 2. read csv files, make a first clean of data and store it in database
    - 3. read all stock-market data and create the prints needed

## Links
[Stock-market conspiracy](https://github.com/Cunillet/Project-Week-3-Data-Thieves)  
[Slides](https://docs.google.com/presentation/d/1d-sK06Uu22up8jAKb5cuHWEukF4NzCc0CqFcrAGK2Ow/edit)  
