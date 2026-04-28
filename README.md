**Title:** Title of your project

**Contributors:** Bulleted list of contributors (with optional ORCIDs).

-Pranathi:  I worked on the Summary and the Data profile sections. I also worked on answering the second research question by creating the SQL table to connect the media, media relations, and objects datasets together. Once I did this, I made a data visualization bar chart to compare the amount of traditional versus digital objects that were represented in the National Gallery of Art dataset. Once I did this, I was able to answer my research questions. This helped me add more to the Summary and Data profile sections. I also did the Metadata documentation section by importing the Data Dictionary information from the original National Gallery  of Art. I finished this part off by including the machine-readable descriptive metadata that described my project in conformance with the Schema.org standard. 

**Summary:** [500-600 words] Description of your project, motivation, research question(s), and any findings.

In the digital age, there is an increase in digital media, and art is easier to create and distribute. This poses an opportunity for museums to incorporate digital media into their catalogues, which blends traditional art curation methods with contemporary data archival practices. Therefore, our goal for this project is to analyze the historical and current practices of the National Gallery of Art Museum to gain a better understanding of the trends in art curation practices in this country. We will do this by combining various datasets provided by the Museum and analyzing them using SQL. The three of us worked together to draft a project plan and work out how we would split up the work, first analyzing our data and then answering our research questions based on our interpretations. There are several research questions that we will focus on to address our overall project goal: analyzing the historical and current practices of the National Gallery of Art Museum to gain a better understanding of the trends in art curation practices in the United States. The research questions we wanted to explore are: 
**Does the National Gallery of Art Museum use data management and storage techniques that allow for the preservation and accessibility of digital objects?
What is the difference between how digital and traditional media are treated in the National Gallery of Art Museum? Are there more digital items or traditional items? **
**We want to know the relationship between older, traditional works of art and modern works at the National Gallery of Art in terms of their region of origin and the artists who made them. **
Overall, we want to know the relationship between older, traditional works of art and modern works at the National Gallery of Art in terms of their region of origin and the artists who made them. After answering our first research question, we found that the National Gallery of Art Museum provided a data dictionary in their repository as well as a relational model and extensive SQL code, which made analysis significantly easier. However, we had to perform additional data cleaning methods to merge categories that were misspelled, categorized incorrectly, and had typos. Additionally, we had to do additional searching on the National Gallery of Art Museum’s website to gain further information on what the digital objects were from the Media CSV file. We saw this as the main drawback to the ‘opendata’ repository since certain links provided in the Media CSV were only for internal use at the National Gallery of Art Museum. 
When answering our second research question, which was “What is the difference between how digital and traditional media in the National Gallery of Art Museum are treated? Are there more digital or traditional items?”, we answered these questions by first using SQL to link the objects, media_items, and media_relationships with one another. After doing this, we identified how many null items there were in media_df based on the related_id that we used to connect with the objects_id from the objects data. Based on the number of null items we found, we used this to determine how many traditional media pieces there were in the National Gallery of Art Museum database. From this, we found that there was a disproportionate amount of digital media represented in the National Gallery of Art Museum, as this was significantly underrepresented compared to the traditional media works in the Museum. 


**Data profile:** [max2000 words] For each dataset used, describe its structure, content, and characteristics. Specify the location of the dataset files in your project repository. Discuss any ethical or legal constraints associated with the data and explain how the datasets relate to your questions

**Data quality:** [500-1000 words] Summary of the quality assessment.

**Data cleaning:** [max 1000 words] Summarize the data cleaning operations you performed and explain how each operation addressed specific data quality issues in your datasets.

**Findings:** [~500 words] Description of any findings including numeric results and/or visualizations.

**Future work:** [~500-1000 words] Brief discussion of any lessons learned and potential future work.

**Challenges:** [~500 words] Discuss the main challenges you encountered while working on the project.

**Reproducing:** Sequence of steps required for someone else to reproduce your results.

**How to Install Dependencies:**

**References:** [Formatted citations for any papers, datasets, or software used in your project.]The National Gallery of Art Open Data File on GitHub: (https://github.com/NationalGalleryOfArt/opendata/tree/main/data)

Project Metadata: This repository contains machine-readable metadata. You can access the Schema.org JSON-LD file at: metadata/metadata.jsonld
