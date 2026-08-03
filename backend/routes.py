from fastapi import APIRouter


from backend.schemas import QuestionRequest, AnswerResponse
from rag.rag_pipeline import ask_question

router = APIRouter()

@router.post("/ask", response_model=AnswerResponse)
def ask_ai(request: QuestionRequest):
    answer = ask_question(request.question)
    
    return AnswerResponse(answer=answer)