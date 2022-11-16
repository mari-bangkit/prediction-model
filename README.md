# Prediction Model

Prediction model for [Mobi.lo](https://github.com/mari-bangkit/Mobi.lo) apps by Mari Bangkit. Hosted in Azure ML as a [web service](https://maribangkit.eastus.inference.ml.azure.com/score).

## About the Model

The exported model uses Lasso Regression to predict the car purchase amount a customer would buy based on their profile, such as gender, annual salary, and more. The main aim is to provide a personalized car recommendation for customers.

The dataset used is accessible [here](https://raw.githubusercontent.com/mari-bangkit/dataset/main/otomotic_id.csv). It is originally come from [Car Purchase Price (beginner dataset)](https://www.kaggle.com/datasets/yashk07/car-purchase-price-beginner-dataset), but has been modified to suit the Indonesian currency (Rp).

## Publication

Research paper: [https://ejurnal.stmik-budidarma.ac.id/index.php/jurikom/article/view/5021](https://ejurnal.stmik-budidarma.ac.id/index.php/jurikom/article/view/5021)

## Deployment

### Prerequisites

- Azure Machine Learning workspace resource.

- Azure CLI and the `ml` extension. Each on v2 or more.

- Python v3 or more.

- Bash/Fish/ZSH or any UNIX-like shell.

### Local Deployment

1. Clone the repo.

    ```
    git clone https://github.com/mari-bangkit/prediction-model.git
    cd prediction-model
    ```

1. Log in to Azure account and set up Azure CLI default setting.

    ```
    az login
    az account set --subscription <subscription ID>
    az configure --defaults group=<resource group> workspace=<Azure Machine Learning workspace name>
    ```

1. Run local deployment script.

    ```
    ./deploy_local.sh
    ```

    The endpoint URL is provided at the **FINAL STATUS** section.

1. Test the API.

    Bash/ZSH shell:

    ```
    export AZURE_ML_URL_LOCAL=<local endpoint url>
    python test_request_local.py
    ```

    Fish shell:

    ```
    set -x AZURE_ML_URL_LOCAL <local endpoint url>
    python test_request_local.py
    ```

### Azure Deployment

1. Run Azure deployment script.

    ```
    ./deploy_azure.sh
    ```

    Open your workspace in [Azure ML Studio](https://ml.azure.com) to get the API URL and key.

1. Test the API.

    Bash/ZSH shell:

    ```
    export AZURE_ML_URL=<endpoint url>
    export AZURE_ML_API_KEY=<endpoint key>
    python test_request_cloud.py
    ```

    Fish shell:

    ```
    set -x AZURE_ML_URL <endpoint url>
    set -x AZURE_ML_API_KEY <endpoint key>
    python test_request_cloud.py
    ```
