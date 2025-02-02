#!/bin/bash

curl -fsSL https://ollama.com/install.sh | sh # Install Ollama

ollama pull mistral #Installs default model for ease of use

ollama serve # Command To be run in tmux for this to work locally

 