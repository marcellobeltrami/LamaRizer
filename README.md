# LamaRizer 🦙

A CLI application to run local AI ChatBots. 

Integrates seamessly with ollama, allowing to run all models.

## Install 

**Ollama setup**

Installs ollama and mistral latest model (default model used in the app). Other models can be installed using `ollama pull <model_name>`

```bash
chmod +x ./setup.sh

sudo ./setup.sh
```

⚠️To use the app, ensure you have tmux open and are running `ollama serve` (the selfhosted ollama server) after installation. If this returns an error such as `tcp already in use` then you already have the server up and don't need to wrry about this. 

**Poetry, mamba and project setup**

Mamba setup to use correct python version.

```bash
curl -Ls https://micro.mamba.pm/install.sh | bash 

micromamba create -n LamaRizer python=3.12 

micromamba activate LamaRizer
```

Install all python dependencies using poetry.  To install poetry run the following command.

```bash 
curl -sSL https://install.python-poetry.org | python3 - # poetry installation

```
Inside the project directory run `poetry install` to install all the projects dependencies.


```bash

cd ./path/to/LamaRizer

poetry install

```


## Quick Use

#### CLI

Command line arguments for this app. The CLI is split into `search` and `docsearch`. See below for appropriate flags.

- `-lm`, `--list_models`: Lists models installed on the system. Run `ollama pull <model_name>` to install more from [https://ollama.com](https://ollama.com/search).

`search`
- `-c`, `--chatrequest`: Directly use chatbot.
- `-w`, `--websearch`: Search the web and summarize the results.
- `-n`, `--newsearch`: Search for news specifically and summarize the results.
- `-m`, `--model`: Specify the model to use (default is "mistral").
- `-o`, `--output`: Specify output file.


`docsearch`
- `-t`, `--textsummary`: Summarize a text file.
- `-p`, `--pdfsummary`: Summarize a PDF file.
- `-m`, `--model`: Specify the model to use (default is "mistral").
- `-o`, `--output`: Specify output file.



```bash
python lamrizer/main.py search -c "What is a Deep Learning model" -o AI_model.md

python lamrizer/main.py search -n "Current news in AI" -o AI_news.md

# To be tested.
#python lamrizer/main.py docsearch -t "path/to/textfile.txt" -o summary.txt
#python lamrizer/main.py docsearch -t "path/to/textfile.txt" -o summary.txt

#python lamrizer/main.py docsearch -p "path/to/pdffile.pdf" -o summary.pdf
```

#### GUI

(Currently being developed)
