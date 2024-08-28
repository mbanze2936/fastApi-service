from typing import Dict

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from model_generator import generate_pydantic_model


# from kafka_producer import send_to_kafka  # Placeholder for Kafka integration

def generate_route(model_name: str, schema: Dict[str, str], topic: str):
    router = APIRouter()

    Model = generate_pydantic_model(model_name, schema)

    @router.post(f"/api/{model_name}")
    async def dynamic_route(data: Model):
        try:
            validated_data = data.dict()
            # Send validated_data to Kafka topic
            # send_to_kafka(topic, validated_data)  # Placeholder
            return {"status": "success", "data": validated_data}
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())

    return router
