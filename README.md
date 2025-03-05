![image](https://github.com/user-attachments/assets/864593e8-01f5-4a42-bc6a-1ea3993489ad)


---

### `(ENG)`  🚀 What Is FastAPI?

#### FastAPI is a modern, high-performance web framework for building APIs with Python based on standard type hints. It has the following key features:

---

🌟 `Fast to run:` **It offers very high performance, on par with NodeJS and Go, thanks to Starlette and Pydantic.**

⚡ `Fast to code:` **It allows for significant increases in development speed.**

🐞 `Reduced number of bugs:` **It reduces the possibility for human-induced errors.**

🖥️ `Intuitive:` **It offers great editor support, with completion everywhere and less time debugging.**

📖 `Straightforward:` **It’s designed to be uncomplicated to use and learn, so you can spend less time reading documentation.**

📝 `Short:` **It minimizes code duplication.**

🛡️ `Robust:` **It provides production-ready code with automatic interactive documentation.**

📜 `Standards-based:` **It’s based on the open standards for APIs, OpenAPI, and JSON Schema.**

---

### `(UZ)` 🚀 FastAPI nima?

#### FastAPI - bu standart turdagi maslahatlar asosida Python bilan API yaratish uchun zamonaviy, yuqori samarali web-framework. U quyidagi asosiy xususiyatlarga ega:

---

⚡ `Tez ishga tushish:` **U Starlette va Pydantic tufayli NodeJS va Go bilan bir xilda juda yuqori unumdorlikni taklif etadi.**

💻 `Tez kodlash:` **Bu rivojlanish tezligini sezilarli darajada oshirish imkonini beradi.**

🐞 `Xatolar soni kamaytirildi:` **Bu inson tomonidan qo'zg'atilgan xatolar ehtimolini kamaytiradi.**

🖥️ `Intuitiv:` **U hamma joyda tugallangan va nosozliklarni tuzatishga kamroq vaqt sarflaydigan ajoyib muharrir yordamini taklif etadi.**

📖 `To'g'ridan-to'g'ri:` **Uni ishlatish va o'rganish oson bo'lishi uchun yaratilgan, shuning uchun hujjatlarni o'qishga kamroq vaqt sarflashingiz mumkin.**

📝 `Qisqa:` **Kodning takrorlanishini kamaytiradi.**

📜 `Standartlarga asoslangan:` **U API, OpenAPI va JSON sxemasi uchun ochiq standartlarga asoslangan.**

---



## 🚀 Install FastAPI

📌 The first step is to install FastAPI and Uvicorn using pip:

```shell
python -m pip install fastapi uvicorn[standard]
```

```shell
pip install fastapi uvicorn[standard]
```

---

## 🏁 First Step - Create a First API

---

📌 `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### **▶️ Run the First API App With Uvicorn**

📌 Run the live server using Uvicorn:

---

```shell
$ uvicorn main:app --reload
```

or

```shell
fastapi dev main.py
```

---

### ✅ **Check the Response**

📌 Open your browser to `http://127.0.0.1:8000`, which will make your browser send a request to your application. It will then send a JSON response.

---

### 📜 **Check the Interactive API Documentation**

📌 Now open `http://127.0.0.1:8000/docs` in your browser.

---

### 📑 **Check the Alternative Interactive API Documentation**

📌 Now, go to `http://127.0.0.1:8000/redoc` in your browser.

---

### 🔥 **Important HTTP Methods (Muhim HTTP Methodlari)**

##### Quyida keltirilgan yo‘nalishlar mavjud:

---

- `GET`: **Ma'lumot olish**
- `POST`: **Ma'lumot yuborish**
- `PUT`: **Ma'lumotni yangilash**
- `DELETE`: **Ma'lumotni o'chirish**
- `PATCH`: **Ma'lumotni qisman yangilash**

---

### 🌟 **Example API Endpoints**

```python
from fastapi import FastAPI

app = FastAPI()

data = []

@app.get("/items")
def get_items():
    return {"items": data}

@app.post("/items")
def create_item(item: dict):
    data.append(item)
    return {"message": "Item added", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if 0 <= item_id < len(data):
        deleted_item = data.pop(item_id)
        return {"message": "Item deleted", "item": deleted_item}
    return {"error": "Item not found"}

@app.patch("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if 0 <= item_id < len(data):
        data[item_id].update(item)
        return {"message": "Item updated", "item": data[item_id]}
    return {"error": "Item not found"}
```

---

### 🗄️ **Database Connection Example**

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)
```

---

### 🔄 **Concurrency vs Parallelism**

🔹 **Concurrency** allows multiple tasks to make progress without necessarily running simultaneously.
🔹 **Parallelism** executes multiple tasks at the exact same time using multiple processors.

Example:

```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} completed")

async def main():
    await asyncio.gather(task("A", 2), task("B", 1))

asyncio.run(main())
```
![image](https://github.com/user-attachments/assets/b0eca7f6-0360-4513-b962-6e61a337e08f)
![image](https://github.com/user-attachments/assets/4f80182c-dff1-4d86-803c-c93c29d747d0)
![image](https://github.com/user-attachments/assets/0323468e-85b5-415f-8b3d-4c1d342df199)
![image](https://github.com/user-attachments/assets/961a88aa-6cd0-46a8-a3f8-47665d892005)
![image](https://github.com/user-attachments/assets/ac8204ff-bd7b-446c-af80-558e8d5daf66)
![image](https://github.com/user-attachments/assets/188ae46a-28b4-49e5-bbda-482f256b65c2)
![image](https://github.com/user-attachments/assets/8ba3f676-da3d-4800-8c01-07e3d81f34b3)

---
![image](https://github.com/user-attachments/assets/ceda7fc6-af56-422a-82af-80533b54d59f)
![image](https://github.com/user-attachments/assets/0221bab9-d23a-45cb-bcb5-51fa7e0820c6)
![image](https://github.com/user-attachments/assets/8646d922-4a2d-474c-a863-6e1d8fdb7fa6)
![image](https://github.com/user-attachments/assets/ac250aba-844d-4cc0-91f8-29088d87196f)
![image](https://github.com/user-attachments/assets/bc6d3de1-71c2-49b5-b5a0-721d6e153143)
![image](https://github.com/user-attachments/assets/2e5e2cb2-70e7-43d9-9795-ae2e40494fc7)

---

### 🎯 **Xulosa (Conclusion)**

#### FastAPI - bu yuqori samarali va kuchli API yaratish uchun mo‘ljallangan framework. U oddiy ishlash, avtomatik hujjatlashtirish va yuqori tezlikni ta’minlaydi. 🚀

