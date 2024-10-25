from pydantic import BaseModel

class NPIExpression(BaseModel):
    expression: str

class OperationResult(BaseModel):
    expression: str
    result: float
