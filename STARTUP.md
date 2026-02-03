# 🚀 Voxcribe – Startup Commands

This file exists so you **never have to remember commands**.
Just open it and **copy–paste**.

---

## 🐍 Start Backend (Whisper + FastAPI)

> Runs the Python Whisper transcription server

```powershell
cd backend
.\venv\Scripts\activate
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

✅ Backend URL:

```
http://localhost:8000
```

✅ API Docs (Swagger):

```
http://localhost:8000/docs
```

---

## ⚛️ Start Frontend (Next.js)

> Run this in a **new terminal window**

```powershell
cd ..
npm run dev
```

✅ Frontend URL:

```
http://localhost:3000
```

---

## 🟢 Easy Mode (Recommended)

If you don’t want to type commands at all, use the scripts below.

### Start Backend

```powershell
backend\start-backend.ps1
```

### Start Frontend

```powershell
start-frontend.ps1
```

---

## 🔁 Daily Workflow (TL;DR)

1. Open **Terminal 1**

   ```powershell
   backend\start-backend.ps1
   ```
2. Open **Terminal 2**

   ```powershell
   start-frontend.ps1
   ```
3. Open browser:

   ```
   http://localhost:3000
   ```

---

## 🧠 Notes

* Backend must be running before transcription works
* Whisper runs locally (no internet required after model download)
* Two servers are required because Whisper needs Python

---

✅ You can now forget the commands. Just open this file 😄
