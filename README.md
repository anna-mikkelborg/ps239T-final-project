## About the project

This project collects data from Google Trends on Google search rates for "White History Month" by Nielson Designated Market Area (DMA) and evaluates the relationship between these search rates and several indicators of racial conservatism from the 2016 Cooperative Congressional Election Study. Data collection is tricky for a couple of reasons: first, Google Trends only provides search rates calculated from a sample of all searches during the period queried; second, there is no official Google Trends API for collecting multiple samples; and third, few DMAs have high enough search rates for "white history month" relative to other terms for this term to show up in a given sample. To get around these issues, I use pyTrends, an unofficial Google Trends API for Python, to collect 100 samples for "white history month", "weather" (a universally common search term), and "weather + 'white history month'" and use regression coefficients to impute search rates for "white history month" using search rates for "weather" and the two terms combined. The data collection from Google Trends is done in Python and the regression and subsequent data analysis and visualization are completed in R.

In order to explore the relationship between interest in a "White History Month" and racial conservatism, I must aggregate county-level CCES measures to the DMA level. I calculate county-level means for the variables of interest, then merge this dataset with a dataset that includes both counties and DMAs on county FIPS. Finally, I merge this dataset with my Google Trends data on DMA name. Using this complete dataset of DMA-level measures, I use regression analysis to examine correlations between search rates and both individual and indexed measures of racial conservatism.

## Dependencies

1. Python, 3.7.3
2. R, 3.6.1

## Files

#### /

1. slides.Rmd: code for slides.
2. slides_files: material for using reveal.js to create slides.
3. slide.html: slides for in-class presentation.
4. README.md: this document.

#### Code/
1. 01_gtrends_data_collection.py: Runs 100 queries of Google Trends for relevant search terms. Saves datasets with averages for each search term by DMA.
2. 02_data-merging.Rmd: Loads, cleans, and merges the Google Trends and CCES data.
3. 03_analysis_and_visualization.R: Conducts descriptive analysis of the data, producing the visualizations found in the Results directory.

#### Data/

1. weather.csv: average of 100 sampled Google Trends search rates for "weather" by DMA
2. whm.csv: average of 100 sampled Google Trends search rates for "white history month" by DMA
3. whmweather.csv: average of 100 sampled Google Trends search rates for "weather + 'White History Month'" by DMA
4. region_averages.csv: the above three datasets combined into one
5. county_dma.csv: one county per row, with a column for corresponding DMA, used to aggregate county-level CCES data to DMA-level, available here: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IVXEHT
6. CCES16.RDATA: relevant variables from the 2016 CCES, available here: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910/DVN/GDF6Z0
7. cces_dmas_whm.csv: The final analysis dataset derived from the raw data above. It includes observations for the following variables:
    - *alphabetical*: The alphabetical order in which DMAs occur
    - *DMA*: the DMA name
    -*dmamean_anger*: average disagreement with the CCES survey item "I am angry that racism exists" from 0 (strongly agree) to 1 (strongly disagree)
    -*dmamean_advantage*: average disagreement with the CCES survey item "White people in the U.S. have certain advantages because of the color of their skin" from 0 (strongly agree) to 1 (strongly disagree)
    -*dmamean_fear*: average agreement with the CCES survey item "I often find myself fearful of people of other races" from 0 (strongly disagree) to 1 (strongly agree)
    -*dmamean_isolated*: average agreement with the CCES survey item "Racial problems in the U.S. are rare, isolated situations" from 0 (strongly disagree) to 1 (strongly agree)
    -*dmamean_rc*: average across above 4 CCES items, ranging from 0 (least conservative) to 1 (most conservative)
    -*dmamean_ord*: Reordered CCES DMA names, used for merging
    -*region*: Google Trends DMA variable
    -*weather*: Google Trends search rates for "weather"
    -*weather....white.history.month.*: Google Trends search rates for "weather + 'White History Month'"
    -*whm_estimate*: Imputed value for white history month search rate
    -*region_first3*: First three characters of DMA, used for merging
8. check.csv: A dataset including DMAs with complete Google Trends data that also includes their imputed search volumes, used in the presentation to display the discrepancy between real and imputed volumes.
9. whm.png: A screen shot of a Google Trends map showing search volumes for "White History Month"
10. whm_weather.png: A screen shot of a Google Trends map showing search volumes for "'White History Month' + weather"
11. weather.png: A screen shot of a Google Trends map showing search volumes for "weather"

#### Results/

1. advantage.png: a histogram showing the distribution of belief in racial advantage among white CCES respondents by DMA
2. anger.png: a histogram showing the distribution of anger that racism exists among white CCES respondents by DMA
3. fear.png: a histogram showing the distribution of fear towards other races among white CCES respondents by DMA
4. isolated.png: a histogram showing the distribution of belief that racial incidents are isolated among white CCES respondents by DMA
5. rc.png: a histogram showing the distribution of mean scores on the above four variables
6. whm.png: a histogram showing the distribution of estimated searches for "white history month" by DMA
7. whm_advantage.png: a regression plot showing the relationship between search rates and belief in racial advantage
8. whm_anger.png: a regression plot showing the relationship between search rates and anger at other races
9. whm_fear.png: a regression plot showing the relationship between search rates and fear of other races
10. whm_isolated.png: a regression plot showing the relationship between search rates and belief in isolation of racism
11. whm_rc.png: a regression plot showing the relationship between search rates and racial conservatism
12. models.html: Summarizes the results of OLS regression, modelling *whm_estimate* on various measures of racial conservatism.
13. models.png: a screen shot of the above .html document to include in my presentation.

## More Information

Anna Mikkelborg is a PhD student of political Science at the University of California-Berkeley.
anna.mikkelborg@berkeley.edu
