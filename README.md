# SmartFilter


```
╔═╗┌┬┐┌─┐┬─┐┌┬┐  ╔═╗┬┬ ┌┬┐┌─┐┬─┐
╚═╗│││├─┤├┬┘ │───╠╣ ││  │ ├┤ ├┬┘
╚═╝┴ ┴┴ ┴┴└─ ┴   ╚  ┴┴─┘┴ └─┘┴└─                                                                    
```                                                                                       
**SmartFilter** A tool for efficiently filtering and classifying text data from datasets. It uses advanced language models to identify and categorize text based on specified criteria .

## Installation

1 - Clone the repository and run the following command:

```bash
git clone https://github.com/ayoubkirouane/SmartFilter.git
cd SmartFilter
```

2 - Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

- `--ds_name`: The name of the dataset to filter (e.g., `ayoubkirouane/Small-Instruct-Alpaca_Format`).
- `--split`: The dataset split to use (e.g., `train`).
- `--target_column`: The column containing the text data (e.g., `text`).


**Example** : 

```bash
python src/main.py --ds_name ayoubkirouane/Small-Instruct-Alpaca_Format --split train --target_column text
```

**NOTE** 

In this project, I'm using the `microsoft/Phi-3-mini-128k-instruct` model from Microsoft. You can customize the model, as well as parameters like `MAX_NEW_TOKENS` and `TEMPERATURE`, by modifying the `src/settings.py` file. Occasionally, you might need to log in to Hugging Face to download models like `Phi-3`. 

To do so, use the following command:

```sh
huggingface-cli login --token hf_xxxxxxxxxxxxxxxxxxxx
```