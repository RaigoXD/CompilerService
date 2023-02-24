from pydantic import BaseModel
from pydantic import Field


class DataCode(BaseModel):
    code: str
