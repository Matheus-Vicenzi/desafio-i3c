import uvicorn
    
if __name__ == "__main__":
    uvicorn.run("controller.ItensController:app", host="localhost", port=8000, reload=True)
