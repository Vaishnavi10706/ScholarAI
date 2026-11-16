from uuid import uuid4
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import extract_pdf_text
from app.services.text_chunker import chunk_text
from app.services.vector_store import store_chunks

router = APIRouter(prefix="/api/papers", tags=["Papers"])
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB
@router.post("/upload")
async def upload_paper(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )
    try:
        if not content:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )
        content = await file.read()
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=413,
                detail="File size must not exceed 20 MB."
            )
        if not content.startswith(b"%PDF-"):
            raise HTTPException(
                status_code=400,
                detail="Invalid PDF file."
            )
        extracted_data = extract_pdf_text(content)
        if not any(page["text"] for page in extracted_data["pages"]):
            raise HTTPException(
                status_code=422,
                detail="No extractable text found. This PDF may be scanned."
            )
        paper_id = str(uuid4())
        for page in extracted_data["pages"]:
            paper_chunks = chunk_text(page["text"])
            for index, chunk in enumerate(paper_chunks):
                all_chunks.append({
                    "text":chunk,
                    "page_number": page["page_number"],
                    "chunk_index":index
                })
        total_chunks = store_chunks(
            paper_id=paper_id,
            filename=file.filename,
            chunks=all_chunks
        )
        return {
            "message": "Research paper processed successfully!",
            "paper_id": paper_id,
            "filename": file.filename,
            "total_pages": extracted_data["total_pages"],
            "total_chunks": total_chunks,
            "embedding_status":"stored",
            "pages":[
                {
                    "page_number":page["page_number"],
                    "text_preview": page["text"][:300]
                }
                for page in extracted_data["pages"]
            ]
        }
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(status_code=500,detail=f"Paper processing failed: {str(error)}")
    finally:
        await file.close()