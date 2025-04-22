from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

# FastAPI অ্যাপ তৈরি করা হচ্ছে
app = FastAPI()

# CORS Middleware সেট করা
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # সব উৎস (origin) থেকে রিকোয়েস্ট অনুমোদন
    allow_credentials=True,
    allow_methods=["*"],  # সব HTTP মেথড (GET, POST, PUT, DELETE ইত্যাদি)
    allow_headers=["*"],  # সব ধরনের হেডার অনুমোদন
)

# Root এন্ডপয়েন্ট উদাহরণ
@app.get("/")
def read_root():
    return {"message": "Welcome to the Image Upload API"}

# ইমেজ আপলোড এন্ডপয়েন্ট
@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # ফাইলের নাম এবং সেভ করার লোকেশন
    save_path = f"uploaded_images/{file.filename}"

    # ফোল্ডার না থাকলে ফোল্ডার তৈরি করা
    os.makedirs("uploaded_images", exist_ok=True)

    # ফাইল সেভ করা
    with open(save_path, "wb") as image_file:
        shutil.copyfileobj(file.file, image_file)

    return {"filename": file.filename, "message": "Image uploaded successfully!"}
