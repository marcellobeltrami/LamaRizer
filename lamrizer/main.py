import deps.core as Main
import deps.docs_import as DocsImport
import argparse 

def main():
    
    # CLI args.
    parser = argparse.ArgumentParser(description="LamRizer CLI")
    parser.add_argument("-m", "--model", type=str, help="Specify the model to use", default="mistral")
    
    subparsers = parser.add_subparsers(dest="command")

    # Search command
    search = subparsers.add_parser("search", help="Search and summarize")
    search.add_argument("-c", "--chatrequest", type=str, help="Directly use chatbot")
    search.add_argument("-w", "--websearch", type=str, help="Search the web and summarize the results")
    search.add_argument("-n", "--newsearch", type=str, help="Search for news specifically and summarize the results")

    # Docsearch command
    docsearch = subparsers.add_parser("docsearch", help="Document search and summarize")
    docsearch.add_argument("-t", "--textsummary", type=str, help="Summarize a text file")
    docsearch.add_argument("-p", "--pdfsummary", type=str, help="Summarize a PDF file")
    args = parser.parse_args()

### SEARCH QUERY ###
    # chat with the model directly
    if args.command == "search":
        if args.chatrequest:
            chat_output = Main.chatrequest(args.chatrequest, model=args.model, input_modifiers="")
            print(chat_output)
        if args.websearch:
            chat_output = Main.chatrequest(Main.web_search(args.websearch), model=args.model, input_modifiers="Extract detailed summary of this internet search without any unnecessary information.")
            print(chat_output)
    #Searches and summarizes news 
        if args.newsearch:
            chat_output = Main.chatrequest(Main.newssearch(args.newsearch), model=args.model, 
                                        input_modifiers="Extract detailed summary of these news accurately.")
            print(chat_output)

### DOCUMENT SEARCH ###
    elif args.command == "docsearch":
    # summarize a pdf file
        if args.docsearch.pdfsummary:
            pdf_text = DocsImport.PdfToText(args.pdfsummary)
            summary_pdf = Main.chatrequest(pdf_text, model=args.model, 
                                        input_modifiers="Extract detailed summary of this text. Do not include any unnecessary information.")
            print(summary_pdf)
        
        # summarize a text file
        if args.docsearch.textsummary:
            txt_text = DocsImport.TxtToText(args.textsummary)
            summary_pdf = Main.chatrequest(txt_text, model=args.model, 
                                        input_modifiers="Extract detailed summary of this text. Do not include any unnecessary information.")
            print(txt_text)


        # List all models installed
        if args.list_models:
            Main.list_models()

if __name__ == "__main__":
        main()