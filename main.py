from fastapi import FastAPI
from configurations import load_configurations
from route_generator import generate_route

app = FastAPI()


# Add a simple root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI dynamic route generator"}


# Load configurations
configurations = load_configurations()["message"]

# Generate routes based on configurations
for config in configurations:
    model_name = config["app_id"]
    schema = {detail['actual_column_name']: detail['data_type'] for detail in config["column_details"]}
    topic = config["topic_name"]
    router = generate_route(model_name, schema, topic)
    app.include_router(router)

# Start the application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
