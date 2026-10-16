"""Deterministic skill comparison and roadmap utilities."""
import re

CAREERS = {
    "AI Engineer": ["Python", "SQL", "Machine Learning", "Deep Learning", "Git", "APIs", "Communication"],
    "Data Analyst": ["Excel", "SQL", "Python", "Statistics", "Data Visualization", "Communication"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "Git", "React", "APIs", "SQL"],
    "Cybersecurity Analyst": ["Networking", "Linux", "Python", "Security Fundamentals", "Incident Response", "Communication"],
    "Cloud Engineer": ["Linux", "Networking", "Python", "Git", "Docker", "Cloud Fundamentals", "CI/CD"],
}

def parse_skills(raw):
    """Split comma/newline-separated skills, stripping duplicates."""
    parts = re.split(r"[,\n;]+", raw or "")
    return list(dict((s.casefold(), s.strip()) for s in parts if s.strip()).values())

def analyze_skills(career, skills):
    required = CAREERS[career]
    known = {s.casefold() for s in skills}
    matched = [s for s in required if s.casefold() in known]
    missing = [s for s in required if s.casefold() not in known]
    return {"career": career, "required": required, "matched": matched,
            "missing": missing, "score": round(100 * len(matched) / len(required))}

def fallback_roadmap(missing):
    if not missing:
        return {"days_1_30": ["Build a small portfolio project"], "days_31_60": ["Contribute to an open-source project"], "days_61_90": ["Practice interviews and showcase your portfolio"]}
    groups = [missing[:2], missing[2:4], missing[4:]]
    return {
        "days_1_30": [f"Learn {s} fundamentals and complete a practice exercise" for s in groups[0]] or ["Revise fundamentals"],
        "days_31_60": [f"Build a mini-project using {s}" for s in groups[1]] or ["Build a project using your new skills"],
        "days_61_90": [f"Demonstrate {s} in a portfolio project" for s in groups[2]] or ["Publish a portfolio project and practice interviews"],
    }
