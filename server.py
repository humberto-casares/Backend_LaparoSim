from fastapi import FastAPI, File, UploadFile, HTTPException
from database import Database
import os

app = FastAPI()
db = Database()

@app.get("/")
def home():
    return {"LaparoSim API": "Welcome to LaparoSim API"}

@app.get("/recieve_transferencia")
def recieve_transferencia(username: str):
    return {"status_code": 200, "username": username}

@app.post("/uploadFiles")
async def uploadFiles(csv_file: UploadFile = File(...), png_file: UploadFile = File(...)):
    try:
        # Define the target directories for the CSV and PNG files
        csv_directory="/var/www/html/EndoTrainer/assets/data/"
        png_directory="/var/www/html/EndoTrainer/assets/Graph3D/"

        # Create the target directories if they don't exist
        os.makedirs(csv_directory, exist_ok=True)
        os.makedirs(png_directory, exist_ok=True)

        # Save the uploaded CSV file to the CSV directory
        csv_file_path = os.path.join(csv_directory, csv_file.filename)
        with open(csv_file_path, "wb") as csv_target:
            csv_target.write(await csv_file.read())

        # Save the uploaded PNG file to the PNG directory
        png_file_path = os.path.join(png_directory, png_file.filename)
        with open(png_file_path, "wb") as png_target:
            png_target.write(await png_file.read())

        return {"status_code": 200, "status_message": "Files uploaded successfully on Server."}

    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail="Target directory not found.")
    except IsADirectoryError as e:
        raise HTTPException(status_code=400, detail="Cannot save file. Target path is a directory.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred during file upload.")