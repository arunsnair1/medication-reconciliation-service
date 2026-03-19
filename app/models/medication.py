from pydantic import BaseModel, Field
from typing import Literal

class Medication(BaseModel):
    name: str
    dose: float = Field(gt=0)
    unit: str
    status: Literal["active", "stopped"]