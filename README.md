# LamRizer 🦙

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

Command line arguments for this app. The output is always printed to console and can be easily piped into text files using the `>` command. The CLI is split into `search` and `docsearch`. See below for appropriate flags.

- `-lm`, `--list_models`: Lists models installed on the system. Run `ollama pull <model_name>` to install.

`search`
- `-c`, `--chatrequest`: Directly use chatbot.
- `-w`, `--websearch`: Search the web and summarize the results.
- `-n`, `--newsearch`: Search for news specifically and summarize the results.
- `-m`, `--model`: Specify the model to use (default is "mistral").

`docsearch`
- `-t`, `--textsummary`: Summarize a text file.
- `-p`, `--pdfsummary`: Summarize a PDF file.
- `-m`, `--model`: Specify the model to use (default is "mistral").



```bash
python lamrizer/main.py search -c "What is a Deep Learning model" > AI_model.md

python lamrizer/main.py search -n "Current news in AI" > AI_news.md

# To be tested.
#python lamrizer/main.py docsearch -t "path/to/textfile.txt" > summary.txt

#python lamrizer/main.py docsearch -p "path/to/pdffile.pdf" > summary.pdf
```

#### GUI

(Currently being developed)
