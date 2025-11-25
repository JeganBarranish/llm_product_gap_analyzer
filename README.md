# LLM-Based Product Feature Gap Analyzer

**Project:** LLM-Based Product Feature Gap Analyzer  
**Purpose:** Given one or more product descriptions (your product) and competitor product descriptions,
the system identifies missing or weaker features, summarizes strengths & weaknesses, and suggests prioritized feature additions.

This repository is a GitHub-ready template for the project. It includes:
- Retrieval + Embeddings (Chroma/FAISS placeholder)
- RAG-style prompts + LLM integration (uses `transformers` or OpenAI API)
- Streamlit demo app for interactive usage
- Sample dataset placeholder and utilities

The uploaded reference PDF used in earlier conversation is placed under `data/LLM_final.pdf`.

## Quickstart (local)

1. Create virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Prepare product descriptions:
   - Place your product and competitor descriptions as JSON/CSV in `data/` (see `data/sample_products.json`).

3. Run the Streamlit demo:
   ```bash
   streamlit run app/streamlit_app.py
   ```

## Project Structure

```
llm_product_gap_analyzer/
├── app/
│   └── streamlit_app.py
├── data/
│   └── sample_products.json
│   └── LLM_final.pdf
├── scripts/
│   ├── analyzer.py
│   ├── embeddings.py
│   └── prompts.py
├── notebooks/
├── requirements.txt
└── README.md
```

## Notes

- This repo contains template scripts. Running full training or model downloads requires internet (not available in this environment).
- You can use OpenAI API or local Hugging Face models for generation.
- I can also push this to a GitHub repo or convert into a Colab notebook on request.
