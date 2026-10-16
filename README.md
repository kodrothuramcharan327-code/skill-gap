# SkillGap AI 🎯

Detect skills before they become career problems. A Streamlit hackathon MVP that compares self-reported skills with curated career checklists and creates a 90-day roadmap.

## Setup

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py
```

The app works without an API key in deterministic demo mode. To enable AI roadmap generation, set `OPENAI_API_KEY` in your environment. For local use, you may copy `.env.example` to `.env` and load it in your shell, or use Streamlit secrets/environment configuration. Never commit a real API key. The default model is configurable with `OPENAI_MODEL`; use a model available to your account that supports JSON object responses.

## Demo
Choose AI Engineer, enter `Python, SQL, Git`, and click **Analyze my skills**. Review missing skills, 90-day roadmap, and download JSON.

## Limitations
Career requirements are sample curated lists, not scraped live vacancies. Coverage is a checklist percentage, not a scientific prediction of employability. Skill matching is exact after case normalization, so synonyms are not automatically recognized. Checklist progress checkboxes are session-local.
