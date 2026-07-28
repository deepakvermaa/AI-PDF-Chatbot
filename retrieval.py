import numpy as np

def retrieve_context(question, model, index, chunks):
    question_embedding = model.encode(
        question,
        convert_to_numpy=True
    )

    question_embedding = question_embedding.astype("float32")
    question_embedding = question_embedding.reshape(1, -1)

    number_of_chunks = 3

    distances, indices = index.search(
        question_embedding,
        number_of_chunks
    )

    retrieved_chunks = []

    for chunk_index in indices[0]:
        retrieved_chunks.append(
            chunks[chunk_index].page_content
        )

    context = "\n\n".join(retrieved_chunks)

    return context