# LamRizer

A CLI application to run local AI ChatBots. 

Integrates seamessly with ollama, allowing to run all models.

## Install 

**Ollama setup**
Installs ollama and mistral latest model (default model used in the app). Other models can be installed using `ollama pull <model_name>`

```bash
chmod +x ./setup.sh

sudo ./setup.sh
```

**Poetry and project setup**

Install all python dependencies using poetry.  To install poetry run the following command.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Inside the project directory run `poetry install` to install all the projects dependencies.


## Quick Use

#### CLI

Command line arguments for this app. The output is alway printed to console and can be easily piped into text files using the `>` command.

- `-i`, `--chatrequest`: Send a chat request to the model directly.
- `-w`, `--websearch`: Search the web and summarize the results using AI model.
- `-n`, `--newsearch`: Search for news specifically and summarize the results using the AI model.
- `-t`, `--textsummary`: Summarize a text file with AI.
- `-p`, `--pdfsummary`: Summarize a PDF file with AI.
- `-m`, `--model`: Specify the model to use (default is "mistral").
- `-lm`, `--list-models`: List all models installed.

```bash
python main.py -i "What is a Deep Learning model" > AI_model.md

python main.py -n "Current news in AI" > AI_news.md

``` 

#### GUI

(Currently being developed)
