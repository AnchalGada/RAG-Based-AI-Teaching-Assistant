<div align="center">

# 🎓 RAG-Based AI Teaching Assistant

<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge&logo=ollama&logoColor=white"/>
<img src="https://img.shields.io/badge/Whisper-Local%20STT-4A90D9?style=for-the-badge&logo=audiomack&logoColor=white"/>
<img src="https://img.shields.io/badge/RAG-Powered-FF6B6B?style=for-the-badge"/>
<img src="https://img.shields.io/badge/100%25-Offline-00C851?style=for-the-badge"/>

<br/>

> **Ask any question about your course → Get directed to the exact video & timestamp instantly.**

*Built for the Sigma Web Development Course · Powered by local LLMs · Zero cloud dependency*

---

</div>

## 🧠 What Is This?

**CourseRAG** is a fully offline Retrieval-Augmented Generation (RAG) system for video-based courses. Students ask natural language questions like *"Where is CSS Flexbox taught?"* and get directed to the **exact video and timestamp** — no more scrubbing through hours of footage.

The entire pipeline runs **locally on your machine** using Ollama — no OpenAI API, no subscriptions, no data leaving your system.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎬 **Full Pipeline** | Video → MP3 → Transcript → Embeddings → Answers |
| 🗣️ **Whisper Transcription** | Auto-transcribes with Hindi → English translation |
| 🔍 **Semantic Search** | `bge-m3` embeddings for deep contextual understanding |
| 🤖 **LLM Answers** | `llama3.2` generates human-like, timestamp-aware responses |
| ⚡ **100% Local** | Runs entirely via Ollama — fully private & offline |
| 🎯 **Timestamp Aware** | Guides users to the exact moment in the right video |

---

## 🏗️ Architecture

```
📹 videos/
    │
    ▼  video_to_mp3.py (ffmpeg)
🎵 audios/
    │
    ▼  mp3_to_json.py (Whisper)
📄 jsons/
    │
    ▼  preprocess_json.py (bge-m3 embeddings)
💾 embeddings.joblib
    │
    ▼  process_incoming.py (cosine similarity + llama3.2)
💬 Answer with Video Title & Timestamp
```

## 📂 Project Structure

```
RAG-Based-AI-Teaching-Assistant/
│
├── 📄 video_to_mp3.py        # Step 1: Convert lecture videos → MP3
├── 📄 mp3_to_json.py         # Step 2: Transcribe & translate → JSON chunks
├── 📄 preprocess_json.py     # Step 3: Generate & store embeddings
├── 📄 process_incoming.py    # Step 4: Answer user queries via RAG
│
├── 📄 requirements.txt       # Python dependencies
├── 📄 .gitignore
│
├── 📁 videos/                # ← Place your lecture videos here
├── 📁 audios/                # ← Auto-generated MP3s (gitignored)
└── 📁 jsons/
    └── sample.json           # Sample transcript format
```

> ⚠️ `embeddings.joblib` is auto-generated locally and is **not** included in this repo.

---

## 🚀 Getting Started

### Prerequisites

Make sure these are installed before you begin:

- ✅ Python 3.9+
- ✅ [ffmpeg](https://ffmpeg.org/download.html) — installed and on PATH
- ✅ [Ollama](https://ollama.com/) — installed and running

---

### Step 1 — Clone the Repo

```bash
git clone https://github.com/AnchalGada/RAG-Based-AI-Teaching-Assistant.git
cd RAG-Based-AI-Teaching-Assistant
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Pull Models via Ollama

```bash
ollama pull bge-m3       # Embedding model
ollama pull llama3.2     # LLM for generating answers
```

### Step 4 — Add Your Videos

Place lecture videos inside the `videos/` folder using this naming format:

```
<Title> #<Number>.mp4

Example:  Introduction to CSS #15.mp4
```

---

## ⚙️ Running the Pipeline

> Run **Steps 1–3 only once** (or whenever you add new videos). Step 4 is your daily driver.

```bash
# Step 1 — Convert videos to MP3
python video_to_mp3.py

# Step 2 — Transcribe MP3s → JSON chunks (takes time ⏳)
python mp3_to_json.py

# Step 3 — Generate embeddings
python preprocess_json.py

# Step 4 — Ask your questions! 🎉
python process_incoming.py
```

---

## 💬 Example Interaction

```
Ask a Question: Where is inline CSS taught?

 Inline CSS is covered in Video #15 — "Inline, Internal & External CSS".
 You can find it starting around the 6:17 mark (377 seconds). The video
 also covers the difference between inline, internal, and external CSS.
 Check out Video #4 at 9:44 as well for a quick mention of inline CSS!
```

---

## 🛠️ Tech Stack

<div>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper-Local%20STT-blue?style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![ffmpeg](https://img.shields.io/badge/ffmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white)

</div>

| Component | Technology |
|---|---|
| 🎙️ Speech-to-Text | OpenAI Whisper `medium` model |
| 🔢 Embeddings | `bge-m3` via Ollama |
| 🤖 LLM | `llama3.2` via Ollama |
| 📐 Similarity Search | scikit-learn cosine similarity |
| 💾 Storage | pandas + joblib |
| 🎬 Video Processing | ffmpeg via subprocess |

---

## 🔧 Customization

You can easily tweak these settings inside the scripts:

| Parameter | File | Default | Options |
|---|---|---|---|
| Whisper model | `mp3_to_json.py` | `medium` | `tiny` `base` `large` |
| Source language | `mp3_to_json.py` | `hi` (Hindi) | Any language code |
| Embedding model | `preprocess_json.py` | `bge-m3` | Any Ollama model |
| LLM model | `process_incoming.py` | `llama3.2` | `deepseek-r1` etc. |
| Top results (k) | `process_incoming.py` | `5` | Any integer |

---
## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repo
2. Create your branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<div align="center">

Made by [AnchalGada](https://github.com/AnchalGada)

⭐ **Star this repo if you found it helpful!** ⭐

</div>
