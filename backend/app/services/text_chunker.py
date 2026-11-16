def chunk_text(
    text: str,
    chunk_size=1000,
    overlap: int = 150
) -> list[str]:
    if chunk_size<=0:
        raise ValueError("Chunk size must be positive.")
    if overlap<0 or overlap>=chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")
    text = text.strip()
    if not text:
        return []
    chunks = []
    start = 0
    while start<len(text):
        end = min(start+chunk_size,len(text))
        if end<len(text):
            boundary = max(
                text.rfind(".",start+chunk_size//2,end),
                text.rfind("\n",start+chunk_size//2,end)
            )
            if boundary != -1:
                end = boundary+1
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end>=len(text):
            break
        start = end-overlap
    return chunks