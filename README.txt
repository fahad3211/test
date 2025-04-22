🛠 কিভাবে চালাবেন:

১. টার্মিনালে ফোল্ডারে যান:
   cd image_upload_api

২. venv তৈরি করুন:
   python -m venv venv

৩. venv চালু করুন:

   Windows:
       venv\Scripts\activate

   Mac/Linux:
       source venv/bin/activate

৪. প্যাকেজ ইনস্টল করুন:
   pip install -r requirements.txt

৫. সার্ভার চালু করুন:
   uvicorn main:app --reload

৬. ব্রাউজারে যান:
   http://127.0.0.1:8000/docs
   এখানে ছবি আপলোড করতে পারবেন।
