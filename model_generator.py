from pydantic import BaseModel, create_model
from typing import Dict, Type

type_mapping = {
    "STRING": str,
    "NUMBER": int,
    "BOOLEAN": bool,
    "FLOAT": float
}


def generate_pydantic_model(model_name: str, schema: Dict[str, str]) -> Type[BaseModel]:
    fields = {key: (type_mapping[value], ...) for key, value in schema.items()}
    return create_model(model_name, **fields)
