import deps.core as Main
import deps.docs_import as DocsImport
import argparse 

def main():
    
    # CLI args.
    parser = argparse.ArgumentParser(description="LamRizer CLI")
    parser.add_argument("-lm", "--list_models", action='store_true', help="Lists models installed on system. Run ollama pull <model_name to install>")

    subparsers = parser.add_subparsers(dest="command")

    # Search command
    search = subparsers.add_parser("search", help="Search and summarize")
    search.add_argument("-c", "--chatrequest", type=str, help="Directly use chatbot")
    search.add_argument("-w", "--websearch", type=str, help="Search the web and summarize the results")
    search.add_argument("-n", "--newsearch", type=str, help="Search for news specifically and summarize the results")
    search.add_argument("-m", "--model", type=str, help="Specify the model to use", default="mistral")
    search.add_argument("-o", "--output", type=str, help="Specify output file", default=None)

    # Docsearch command
    docsearch = subparsers.add_parser("docsearch", help="Document search and summarize")
    docsearch.add_argument("-t", "--textsummary", type=str, help="Path to a text file to summarize")
    docsearch.add_argument("-p", "--pdfsummary", type=str, help="Path to a PDF file to summarize")
    docsearch.add_argument("-d", "--docx", type=str, help="Path to a docx to summarize")
    docsearch.add_argument("-m", "--model", type=str, help="Specify the model to use", default="mistral")
    docsearch.add_argument("-o", "--output", type=str, help="Specify output file", default=None)


    args = parser.parse_args()

### SEARCH QUERY ###
    # chat with the model directly
    if args.command == "search":
        if args.chatrequest:
            chat_output = Main.chatrequest(args.chatrequest, model=args.model, input_modifiers="")
            Main.check_output(chat_output, args.output)

        if args.websearch:
            chat_output = Main.chatrequest(Main.web_search(args.websearch), model=args.model, input_modifiers="Extract detailed summary of this internet search without any unnecessary information.")
            Main.check_output(chat_output, args.output)
    #Searches and summarizes news 
        if args.newsearch:
            newsearch_out = Main.newssearch(args.newsearch)
            chat_output = Main.chatrequest(newsearch_out[1], model=args.model, 
                                        input_modifiers="Extract detailed summary of these news accurately.")
            Main.check_output(chat_output, args.output)
            if  args.output != None: 
                
                with open(args.output, "a") as file:
                    print(f"\n\n## REFERENCES\n", newsearch_out[0], file=file) 


### DOCUMENT SEARCH ###
    elif args.command == "docsearch":
    # summarize a pdf file
        if args.pdfsummary:
            pdf_text = DocsImport.PdfToText(args.pdfsummary)
            summary_pdf = Main.chatrequest(pdf_text, model=args.model, 
                                        input_modifiers="Extract detailed summary of this text. Do not include any unnecessary information.")
            Main.check_output(summary_pdf, args.output)
        
        # summarize a text file
        if args.textsummary:
            txt_text = DocsImport.TxtToText(args.textsummary)
            summary_txt = Main.chatrequest(txt_text, model=args.model, 
                                        input_modifiers="Extract detailed summary of this text. Do not include any unnecessary information.")
            Main.check_output(summary_txt, args.output)

        # summarize a docx file
        if args.textsummary:
            docx_text = DocsImport.DocxToText(args.textsummary)
            summary_txt = Main.chatrequest(docx_text, model=args.model, 
                                        input_modifiers="Extract detailed summary of this text. Do not include any unnecessary information.")
            Main.check_output(summary_txt, args.output)


    # List all models installed
    if args.list_models == True:
        Main.list_models()

if __name__ == "__main__":
        main()