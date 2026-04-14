def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_text(text, max_length=500):
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), max_length):
        chunk = " ".join(words[i:i+max_length])
        chunks.append(chunk)
    
    return chunks