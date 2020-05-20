<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Internet Movie Databases Exploratory Analysis
*Beto Sibileau*

*DATA Barcelona Bootcamp (March 2020)*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The original motivation for my project was to discover the Netflix prize dataset, released by the company in 2006 before launching their disruptive bussiness model based on streaming and recommendation systems.

## Questions & Hypotheses
I want to analyze the bussiness evolution of Netflix in the media entertainment industry in the first place. I got the Google trend measurements about Netflix in USA and Spain and data revealed much more than I know about Netflix bussiness model shifts starting from their foundation in 1997.

Initially, I wanted to compute myself a recommendation predictive algorithm but decided afterward that would be a better idea to tackle with the machine learning algorithms that we would learn for the next Bootcamp project. However, I had a very large dataset of +14k titles from movies and came with the idea of addressing the question about a possible correlation that suggest producers at a given country about a movie duration that would maximize their user ratings. The data revealed that this correlation is not feasible. However, I ended up with two different user rating systems (one from Netflix and other from OMDb) for the same movie titles, that eventually showed a strong positive correlation. This results an interesting insight meaning that eventually, two different ranking systems from different users could be statistically interchangable up to some extend.

Finally, the distribution of movie durations from an IMDB database of more than 80k movies is analyzed accross a timeline beginning at the earlies 1900's up to today for titles produced in the USA. The data reveals an interesting insight about how the mode of a movie distribution has been shifting along time and its current trend from 2000 up to today.

## Dataset
Many different datasets are compiled in the present analysis, starting from Netflix prize dataset which comes with more than 20 million recommendations in a quite heavy series of data text files. A particular reading system has been program in order to retrieve the necessary information from the text files. Another sources have been the OMDb API and IMDB dataset from kaggle website in a standard `csv` format. The following links are provided for the interested reader:

[Netflix Data Prize](https://www.kaggle.com/netflix-inc/netflix-prize-data/)  
[OMDb API](https://slides.com/)  
[IMDB dataset](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset)  

## Workflow
Once my interest was caught about Netflix evolution of their bussiness model, I began the research of databases and found the Netflix Data Prize. I wanted to correlate ratins against movie durations, which were not present in that dataset. Thus, I jumped into API calls to OMDb and eventually retrieved the runtime and also the OMDb rating. Given that this correlation analysis failed, I proceed to a succesfully correlation analysis of the different user rating systems from Netflix and OMDb. Finally, the exploratory data analysis of the evolution of movie runtimes along time is conducted and properly evaluated.

## Organization
The organization of the different project steps is provided below in a link to a kanban board.

With respect to this repository, the reader would find in this folder two Jupyter notebooks with the Python code of my project. In addition, there is a folder with a presentation of the project, images and datasets. Unfortunately, some datasets are heavy and are not uploaded to the repo but the interested reader could find them in the provided links above.

## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository](https://github.com/beto-Sibileau/Project-Week-5-Your-Own-Project/tree/master/your-project)  
[Slides](https://github.com/beto-Sibileau/Project-Week-5-Your-Own-Project/tree/master/your-project)  
[Trello Board](https://trello.com/b/kc0c28Ou/my-own-project-netflix-eda)  
