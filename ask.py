from loader import load_resources
from retrieval import retrieve_context
from generator import generate_answer


def main():
    client, model, index, chunks = load_resources()

    print("PDF Chatbot Ready!")
    
    while True:
        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            print("Goodbye!")
            break
        
        print("\nSearching document...")

        context = retrieve_context(
            question,
            model,
            index,
            chunks
        )

        print("Generating answer...")
        
        try:
            answer = generate_answer(
                client,
                question,
                context
            )

            print("\nAnswer:")
            print(answer)

        except Exception as error:
            print(f"\nError: {error}")

if __name__ == "__main__":
    main()