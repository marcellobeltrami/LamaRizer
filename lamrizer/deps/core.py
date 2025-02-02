from duckduckgo_search import DDGS
import ollama


# Gets carrys general search on the web
def general_search(query):
    print("Searching the web...", end="")
    results = DDGS().text(query, max_results=20)
    
    text =  "\\n".join([r["title"] + ": " + r["body"] for r in results])
    print("Done")
    return text

# Carrys out news search on the web Return links from DDGS search
def newssearch(query):
    print("Searching the web for news...", end="")
    results = DDGS().news(query,max_results=20)
    
    text =  "\\n".join([r["title"] + ": " + r["body"] for r in results])
    print("Done")
    return text

# Gets a query list
def chatrequest(usr_input, model, input_modifiers=""):
    print(model, "is thinking...")
    # add a way to list all models installed.
    response = ollama.chat(model=model, 
                           messages=[{"role": "user", 
                                      "content": f"{input_modifiers} : {usr_input}"}])
    
    return response["message"]["content"]

# List models installed on the machine
def list_models():
    ollama_list = ollama.list()  

    if ollama_list['models'] == []:
        return "No models installed"
    else:
        for model in ollama_list['models']:
            print(model['model'])