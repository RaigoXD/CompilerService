from fastapi import APIRouter
from fastapi import Body

# schemas
from app.schemas.code import DataCode

# services
from app.services.index import check_sintaxis

sintaxis_verify = APIRouter()


@sintaxis_verify.post(
    path="/check_code",
    status_code=200,
    description="The code was verified successfully",
)
def check_code(data_code: DataCode = Body()):
    return check_sintaxis(data_code.code)
