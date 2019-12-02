<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Weather and traffic conditions in Barcelona
*Jordi Jordana*

*Data 2019, Barcelona & 29-11-19]*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project is meant to analyse whether there is or there is not a relationship between traffic crashes in Barcelona and weather conditions, particularly rain and wind.

I have always heard that rain is particularly dangerous for two wheel vehicles and Barcelona is a city packed with bikes and motorbikes. 

Though it is true it doesn’t rain much nor is a windy city, I thought there occur enough diverse climate conditions throughout the span of two years in Barcelona to test some hypothesis on the matter. So I gathered the data from years 2017 and 2018.

## Questions & Hypotheses
I had two main questions, and I eventually split one of them into two as I worked with the data. 

The first question was whether rainy days have a higher accidental rate or not. As I worked on it, it also occurred to me to analyse the wind effect on traffic collisions.

The other question I posed to myself it relates to motorbikes. If it is true that two wheel vehicles are particularly dangerous on rainy days, then the ratio of motorbike crashes should increase on these days. I wanted to give an answer to that apparently commonsensical idea.

## Dataset
I used two main dataset sources to answer these questions. In the first place, I used a dataset from the individuals involved in crashes on the road in Barcelona, available on Open Data BCN. This data includes information from all the traffic collisions in the city registered by the Guàrdia Urbana police. 

In the second place, I used the API from AEMET, which is a public Spanish weather agency. This API allows the user to request historical data from recent years through a key and choosing the information from tabs. This generates a url that can be called to obtain the data.

Open Data BCN: shorturl.at/bhsDH

AEMET API: shorturl.at/vHR67

## Workflow
With the purpose of answering the questions that guide this research I started looking for the appropriate datasets. During the search, I knew Open Data BCN would have datasets of traffic collisions and I found several of them that could be used.

In order to compare this data with the weather conditions, I searched for several different APIs. I had to make sure they contained information about Barcelona and check there was no missing information for the period 2017-2018. Finally, the AEMET API complied with everything needed when it comes to precipitations, and also triggered in me the idea of studying the influence of wind on traffic.

Once this was done, I proceeded to clean the data. The dataset containing the traffic crashes is accessible year by year, so in the first place I had to append one year to another. Then I dropped the unnecessary columns. 

The weather dataset didn’t need any special cleaning other than the drop of some columns, but since I wanted to merge both datasets the date column had to be prepared. In one of the datasets there was a column date ordered as yyyy-mm-dd. In the other one, this data was splitted into columns, so it had to be joined and properly converted.

Once the dataframes had the same column, they could be merged and explored in smaller dataframes when needed. When the dataframes were ready, I plotted the results with the matplotlib library.


## Organization
I used a Trello board. It can be found here: https://trello.com/b/j53TbAVY/project4


When it comes to the repository, the main folder there are csv to read from and three folders. The folders are: CRASHES_DC, METEO_DC and PLOTINGS. The two folders containing the suffix 'DC' are devoted to the cleaning and preparation of the data from the two datasets. The preparation of the Date column is done in parallel in two different ipynb ('Rain' & 'Accidents') in the CRASHES_DC folder. 

The folder called PLOTINGS contains the data cleaning needed to do the merge of the dataframes. It also contains the remainings of the preparation of the data in order to create the graphs. This folder also contains the graphs.

## Links

[Repository] https://github.com/JordiJordana/Project-Week-5-Your-Own-Project
[Trello] https://trello.com/b/j53TbAVY/project4