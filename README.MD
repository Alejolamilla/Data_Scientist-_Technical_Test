# Data Scientist - Technical Test

## Description
This project is a technical test for data scientists. We are working on a lead scoring algorithm for a client that has an Event Management SaaS application. The job is to receive the raw data from the client and prepare it to train a classification algorithm that will predict the probability of conversion of each lead.

## Project Structure
The project has the following structure:
- `Data`: This folder contains two subfolders:
  - `raw`: Contains the original datasets.
  - `processed`: Contains several datasets that were used at different stages of the project. Each dataset represents a different stage of processing.
- `Notebooks`: This folder contains four Jupyter notebooks detailing the entire process from importing and cleaning the data, through EDA and enrichment, to the different models that were tried, and finally the creation of the app. There is also a notebook called `Clean_notebook` that contains only the necessary code to process the data, with out visualizations or data analysis sections. Lastly, there is a Python file called `toolbox.py` that acts as a library for useful functions used in the notebooks.
- `environment.yml`: This file contains the necessary libraries to run the project.

## Original Datasets
There are 2 datasets that reflect the phases in the client’s sales process:
1. `leads.csv`: This dataset contains data of all potential clients.
2. `offers.csv`: This dataset contains data of clients that got at least to the demo meeting.

The target column is `Status` from the `offers` dataset, which indicates whether a client has bought the product.

## Getting Started
To get started with this project, you'll need to do the following:
1. Clone the repository to your local machine.
2. Install the necessary dependencies using the `environment.yml` file.
3. Load the datasets into your preferred data analysis tool.
4. Begin exploring the data and building your classification model.
5. Alternatively, you can simply run the `Clean_notebook.ipynb` which will process the whole data and train the model.

## License
This project is licensed under the terms of the MIT license.
