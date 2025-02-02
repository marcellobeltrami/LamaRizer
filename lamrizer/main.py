import deps.core as Main
import deps.docs_import as DocsImport
import argparse 

def main():
    
    # CLI args.
    parser = argparse.ArgumentParser(description="LamRizer CLI")
    parser.add_argument("-i","--chatrequest", type=str, help="Send a chat request to the model directly")
    parser.add_argument("-w","--websearch", type=str, help="Search the web and summarizes the results")
    parser.add_argument("-n","--newsearch", type=str, help="Search the for news specifically and summarizes the results")
    parser.add_argument("-t","--textsummary", type=str, help="Summarize a text file")
    parser.add_argument("-p","--pdfsummary", type=str, help="Summarize a PDF file")
    parser.add_argument("-m","--model", type=str, help="Specify the model to use", default="mistral")
    parser.add_argument("-lm","--list-models", action="store_true", help="List all models installed")
    args = parser.parse_args()


    # chat with the model directly
    if args.chatrequest:
        chat_output = Main.chatrequest(args.chatrequest, model=args.model, 
                                       input_modifiers="")
        print(chat_output)
    
    # summarize a pdf file
    if args.pdfsummary:
        pdf_text = DocsImport.PdfToText(args.pdfsummary)
        summary_pdf = Main.chatrequest(pdf_text, model=args.model, 
                                       input_modifiers="With a temperature of 0.2, extract detailed summary of this text. Do not include any unnecessary information.")
        print(summary_pdf)

    # Summarize an internet search
    if args.websearch:
        chat_output = Main.chatrequest(Main.web_search(args.websearch), model=args.model, 
                                       input_modifiers="Extract detailed summary of this internet search without any unnecessary information.")
        print(chat_output)

    if args.newsearch:
        chat_output = Main.chatrequest(Main.newssearch(args.newsearch), model=args.model, 
                                    input_modifiers="Extract detailed summary of these news accurately.Include searc links as references.")
        print(chat_output)


    # List all models installed
    if args.list_models:
        Main.list_models()

if __name__ == "__main__":
    main()