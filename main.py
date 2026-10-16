"""Run with: streamlit run main.py"""
import streamlit as st
from model import generate_roadmap
from tools import CAREERS, analyze_skills, parse_skills

st.set_page_config(page_title="SkillGap AI", page_icon="🎯", layout="centered")
st.title("🎯 SkillGap AI")
st.caption("Detect skills before they become career problems.")
st.write("Compare your current skills with a sample career skill profile and get a personalized learning roadmap.")

career = st.selectbox("Choose your dream career", list(CAREERS))
st.caption(f"Sample skills in this {career} checklist ({len(CAREERS[career])}):")
st.write(", ".join(CAREERS[career]))

with st.expander("Browse all career skill profiles"):
    for career_name, required_skills in CAREERS.items():
        st.markdown(f"**{career_name}**")
        st.write(", ".join(required_skills))

with st.form("student_profile"):
    name = st.text_input("Your name (optional)", max_chars=80)
    skills_raw = st.text_area("Your existing skills (comma-separated)", placeholder="Python, SQL, Git", height=100)
    submitted = st.form_submit_button("Analyze my skills", type="primary")

if submitted:
    skills = parse_skills(skills_raw)
    if not skills:
        st.warning("Enter at least one skill to continue.")
    else:
        analysis = analyze_skills(career, skills)
        st.subheader(f"Results{f' for {name}' if name else ''}")
        st.metric("Sample career skill coverage", f"{analysis['score']}%")
        st.progress(analysis["score"] / 100)
        st.caption("Coverage is based on a curated demo checklist, not a validated employability prediction or live job-market data.")
        st.success("Matched skills: " + (", ".join(analysis["matched"]) or "None yet"))
        if analysis["missing"]:
            st.warning("Skills to develop: " + ", ".join(analysis["missing"]))
        else:
            st.info("You match all skills in this sample checklist. Keep building practical experience!")
        with st.spinner("Creating your roadmap..."):
            roadmap, source = generate_roadmap(analysis)
        st.subheader("Your 90-day roadmap")
        st.caption(source)
        for title, key in [("Days 1–30: Foundations", "days_1_30"), ("Days 31–60: Practice", "days_31_60"), ("Days 61–90: Portfolio", "days_61_90")]:
            st.markdown(f"**{title}**")
            for task in roadmap[key]:
                st.checkbox(task, key=f"{key}:{task}")
        report = {"analysis": analysis, "roadmap": roadmap, "source": source}
        import json
        st.download_button("Download results (JSON)", json.dumps(report, indent=2), "skillgap_report.json", "application/json")
