# 🎓 RAG-BASED-AI-TEACHING-ASSISTANT

> Ask any question about your course and get directed to the **exact video and timestamp** where it's taught.

---

## 🧠 What Is This?

**RAG** is a Retrieval-Augmented Generation (RAG) system built for video-based courses. It lets students ask natural language questions like *"Where is CSS flexbox taught?"* and instantly get pointed to the right video and timestamp — no more scrubbing through hours of footage.

Built for the **Sigma Web Development Course**, this pipeline takes raw video lectures, transcribes them using Whisper, embeds the transcripts using a local embedding model, and answers student queries using a local LLM — all running **100% offline**.

---

## ✨ Features

- 🎬 **Video → MP3 → JSON → Embeddings** — fully automated pipeline
- 🗣️ **Whisper transcription** with Hindi→English translation support
- 🔍 **Semantic search** using `bge-m3` embeddings via Ollama
- 🤖 **LLM-powered answers** using `llama3.2` via Ollama
- ⚡ **Local & private** — no OpenAI API, no cloud dependency
- 🎯 **Timestamp-aware** — responses guide users to exact video moments

---

## 🏗️ Architecture

```
videos/
  └─ Raw .mp4 lecture files
        │
        ▼ video_to_mp3.py (ffmpeg)
audios/
  └─ Numbered .mp3 files
        │
        ▼ mp3_to_json.py (Whisper)
jsons/
  └─ Transcript chunks with timestamps
        │
        ▼ preprocess_json.py (bge-m3 via Ollama)
embeddings.joblib
  └─ DataFrame of chunks + embeddings
        │
        ▼ process_incoming.py (cosine similarity + llama3.2)
        └─ Answer with video title & timestamp
```

---

## 📂 Project Structure

```
courserag/
├── video_to_mp3.py       # Step 1: Convert lecture videos to MP3
├── mp3_to_json.py        # Step 2: Transcribe & translate audio → JSON chunks
├── preprocess_json.py    # Step 3: Generate and store embeddings
├── process_incoming.py   # Step 4: Answer user queries via RAG
├── embeddings.joblib     # Saved embeddings dataframe (generated)
├── prompt.txt            # Last prompt sent to LLM (auto-generated)
├── response.txt          # Last LLM response (auto-generated)
├── videos/               # Place raw lecture videos here
├── audios/               # Auto-generated MP3s
└── jsons/                # Auto-generated transcript JSONs
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [ffmpeg](https://ffmpeg.org/download.html) installed and on PATH
- [Ollama](https://ollama.com/) installed and running locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/courserag.git
cd courserag
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull Required Models via Ollama

```bash
ollama pull bge-m3      # Embedding model
ollama pull llama3.2    # LLM for answering queries
```

### 4. Add Your Videos

Place your lecture videos inside the `videos/` folder. Videos must follow this naming convention:

```
<Title> #<Number>.mp4
# Example: Introduction to CSS #15.mp4
```

---

## ⚙️ Running the Pipeline

Run each step in order the **first time**. After that, only re-run steps when new videos are added.

```bash
# Step 1 — Convert videos to MP3
python video_to_mp3.py

# Step 2 — Transcribe MP3s to JSON chunks
python mp3_to_json.py

# Step 3 — Generate embeddings (saved to embeddings.joblib)
python preprocess_json.py

# Step 4 — Ask questions!
python process_incoming.py
```

**Example interaction:**

```
Ask a Question: Where is inline CSS taught?

> Inline CSS is covered in Video #15 — "Inline, Internal & External CSS".
> You can find it starting around the 6:17 mark (377 seconds). The video
> also covers the difference between inline, internal, and external CSS.
> Check out Video #4 at 9:44 as well for a quick mention of inline CSS!
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Speech-to-Text | [OpenAI Whisper](https://github.com/openai/whisper) (`medium` model) |
| Embeddings | `bge-m3` via [Ollama](https://ollama.com/) |
| LLM | `llama3.2` via [Ollama](https://ollama.com/) |
| Similarity Search | `scikit-learn` cosine similarity |
| Data Storage | `pandas` + `joblib` |
| Video Processing | `ffmpeg` via subprocess |


## 🔧 Configuration

You can customize the following inside the scripts:

| Parameter | Location | Default | Description |
|---|---|---|---|
| Whisper model size | `mp3_to_json.py` | `medium` | Use `large` for better accuracy |
| Source language | `mp3_to_json.py` | `hi` (Hindi) | Change for other languages |
| Embedding model | `preprocess_json.py` | `bge-m3` | Any Ollama-compatible model |
| LLM model | `process_incoming.py` | `llama3.2` | Swap for `deepseek-r1` etc. |
| Top results (k) | `process_incoming.py` | `5` | Number of chunks retrieved |

---

## 📌 Notes

- **Videos and audio files are not included** in this repo due to size. Add your own to `videos/`.
- `embeddings.joblib` is generated locally and should be added to `.gitignore` if large.
- The system prompt is designed for web development courses but can be adapted for any subject by editing the prompt template in `process_incoming.py`.

---



---

## 📄 License

MIT License — feel free to use and adapt for your own courses.
