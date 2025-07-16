# PERSONA GENERATOR
# 🤖 Reddit User Persona Generator

This project was developed for the BeyondChats Generative AI internship assignment.

It is an end-to-end Python tool that:
- ✅ Scrapes a Reddit user's **posts and comments**
- ✅ Uses an **open-source LLM via Together AI**
- ✅ Generates a detailed **User Persona**
- ✅ **Cites** the specific posts or comments that support each insight (inline)

You can run it via command line or a simple Streamlit web app.

---

## 📌 **What’s Inside**

- `scraper.py` — Scrapes Reddit profiles using PRAW.
- `persona_generator.py` — Uses Together AI to generate the persona.
- `app.py` — (Optional) Streamlit frontend.
- `outputs/` — Stores generated persona `.txt` files.
- `requirements.txt` — Project dependencies.

---

## 🚀 **Features**

✅ Follows **PEP-8** style guide  
✅ Uses **Together AI** to call open-source models like **Mixtral-8x7B**  
✅ Outputs **inline citations** for every insight  
✅ Supports both **CLI** and **web app** interface  
✅ Ready for **GitHub submission**

---

## ⚙️ **Setup Instructions**

### 1️⃣ Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/reddit-persona-generator.git
cd reddit-persona-generator
