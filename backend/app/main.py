from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.responses import FileResponse
from app.database import SessionLocal, init_db
from app.models import Operation
from app.schemas import NPIExpression, OperationResult
from app.npi import evaluate_npi
import csv

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend React endpoint
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_event():
    await init_db()

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/calculate", response_model=OperationResult)
async def calculate(expression: NPIExpression, db: AsyncSession = Depends(get_db)):
    try:
        tokens = expression.expression.split()
        result = evaluate_npi(tokens)
        db_operation = Operation(expression=expression.expression, result=result)
        db.add(db_operation)
        await db.commit()
        return {"expression": expression.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/export_csv")
async def export_csv(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Operation))
    operations = result.scalars().all()
    with open("operations.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Expression", "Result"])
        for operation in operations:
            writer.writerow([operation.id, operation.expression, operation.result])
    return FileResponse("operations.csv", media_type='text/csv', filename="operations.csv")
