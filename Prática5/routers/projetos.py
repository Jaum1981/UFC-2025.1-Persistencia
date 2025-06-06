from fastapi import APIRouter, Depends ,HTTPException
from sqlmodel import Session, select
from database import get_session
from model import Projeto

router = APIRouter(prefix="/projeto", tags=True)

@router.get("", response_model=list[Projeto])
def listar_projetos(session: Session = Depends(get_session)):
    return session.exec(select(Projeto)).all()

@router.get("/{projeto_id}", response_model=Projeto)
def 