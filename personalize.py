#!/usr/bin/env python3
"""
personalize.py — content-only swap of the rebuilt portfolio to Varun Y R.
Runs after build_clean.py. Changes ONLY content (projects, skills, identity,
experience, education, achievements, socials, images) — no JS/CSS/animation
or structural code is modified.
"""
import os, re, json, shutil, glob

LEETCODE_URL = "https://leetcode.com/u/varunyr1224/"  # linked from the social icons

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "client-build")
IMG = os.path.join(OUT, "assets/images")

# Copy the persistent project screenshots into the build (build_clean.py wipes
# client-build/, so these live in static-src/project-images/ and are restored
# here on every run).
for p in glob.glob(os.path.join(SRC, "static-src/project-images/*")):
    shutil.copy2(p, os.path.join(IMG, os.path.basename(p)))

# Resume PDF (downloaded by the hero "Resume" button).
shutil.copy2(os.path.join(SRC, "static-src/Varun_Y_R_Resume.pdf"),
             os.path.join(OUT, "Varun_Y_R_Resume.pdf"))

# VYR brand favicon set (overrides the scraped Yamin icons).
for fn in ("favicon.ico", "apple-touch-icon.png", "favicon-32.png", "icon-512.png"):
    shutil.copy2(os.path.join(SRC, "static-src/brand", fn), os.path.join(OUT, fn))

# --------------------------------------------------------------------------
# CONTENT
# --------------------------------------------------------------------------
ME = {
    "name": "Varun Y R",
    "role": "Full-Stack Software Engineer",
    "email": "varunyr1224@gmail.com",
    "github": "https://github.com/gt-varun",
    "linkedin": "https://www.linkedin.com/in/varun-yr-b37687311/",
    "location": "Bengaluru, India",
}

BIO = ("I'm a full-stack software engineer and final-year B.E. (Information Science) "
       "student running two simultaneous production internships across web, desktop, "
       "and mobile. I build and ship REST APIs, AI-powered features, and cloud "
       "infrastructure end-to-end — from design through deployment and QA.")

SKILLS = [
    {"title": "Languages", "skills": ["Java", "JavaScript (ES6+)", "Python", "C", "Swift"]},
    {"title": "Frontend", "skills": ["React.js", "Electron", "Chrome Extensions", "HTML5", "CSS3"]},
    {"title": "Backend & APIs", "skills": ["Node.js", "Express.js", "REST API Design", "JWT", "OAuth 2.0", "Stripe"]},
    {"title": "Databases & Cloud", "skills": ["MongoDB", "MySQL", "AWS (EC2/S3)", "Google Cloud", "CI/CD", "Git"]},
    {"title": "AI / ML & Tools", "skills": ["TensorFlow", "HuggingFace", "OpenCV", "Generative AI", "Postman"]},
]

PROJECTS = [
    {
        "title": "BharatAssist AI",
        "category": "AI Agents",
        "description": "AI-powered government-scheme advisor that matches Indian citizens to welfare schemes they're eligible for — in their own language.",
        "longDescription": "BharatAssist AI is a multilingual platform that helps Indian citizens discover and apply for government welfare schemes. It intelligently matches 50+ schemes to a user's eligibility from their profile, explains requirements in plain language across multiple Indian languages, and lets users track applications end to end. Built with React 18 + TypeScript on the front end and Supabase (PostgreSQL) for data and auth.",
        "image": "assets/images/varun-bharatassist.png",
        "tags": ["React", "TypeScript", "Supabase", "PostgreSQL", "AI"],
        "demoLink": "https://bharat-assist-ai-olive.vercel.app",
        "codeLink": "https://github.com/gt-varun/BharatAssist-AI",
    },
    {
        "title": "BTP Parking Intelligence",
        "category": "Data Analysis",
        "description": "Full-stack MERN platform backed by a scikit-learn model trained on a 298,450-record Bangalore Traffic Police dataset.",
        "longDescription": "A full-stack MERN conversion of the Bangalore Traffic Police parking-intelligence prototype. Every hardcoded placeholder from the original was replaced with a real model trained on a 298,450-record BTP dataset (Python + pandas + scikit-learn), surfacing genuine violation, challan, and junction analytics. MongoDB + Mongoose data layer, Node/Express API, and a React dashboard with a live violation map of Bengaluru.",
        "image": "assets/images/varun-btp-parking.png",
        "tags": ["MERN", "MongoDB", "Python", "scikit-learn", "React"],
        "demoLink": "https://btp-parking-intelligence.vercel.app",
        "codeLink": "https://github.com/gt-varun/btp-parking-intelligence",
    },
    {
        "title": "Mindful AI",
        "category": "Machine Learning",
        "description": "Real-time multimodal emotion detection fusing voice, facial expression, and heart rate into one output with sub-2-second latency.",
        "longDescription": "A real-time AI pipeline that fuses three simultaneous signal types — voice, facial expression, and heart rate — into a single unified emotion output, achieving under 2-second end-to-end latency on standard hardware. Built in a 72-hour sprint and ranked 6th nationally (top 6%) out of 100+ teams at the AI Verse Hackathon, BMSCE.",
        "image": "assets/images/varun-mindful-ai.svg",
        "tags": ["Python", "TensorFlow", "OpenCV", "Computer Vision", "Multimodal"],
        "demoLink": "",
        "codeLink": "",
    },
    {
        "title": "Quizmify",
        "category": "Professional Work",
        "description": "AI-powered quiz platform: generate intelligent quizzes, share via unique codes, and track real-time results with analytics.",
        "longDescription": "A full-stack quiz platform with 8 REST API endpoints (quiz creation, participation, scoring) supporting concurrent multi-user sessions with zero race conditions and instant result delivery. Generate AI-assisted quizzes, share them with unique join codes, and track live results with detailed analytics.",
        "image": "assets/images/varun-quizmify.png",
        "tags": ["React", "Node.js", "Express", "MongoDB", "AI"],
        "demoLink": "https://quizmify-delta.vercel.app",
        "codeLink": "https://github.com/gt-varun/Quizmify",
    },
    {
        "title": "Criminal Case Management System",
        "category": "Professional Work",
        "description": "MERN legal platform with 3-role RBAC, JWT auth, 12+ tested REST endpoints, evidence uploads, and a Chart.js analytics dashboard.",
        "longDescription": "A role-based (RBAC) case-management system for criminal cases, complaints, and records. Three access-controlled roles, JWT authentication, 12+ tested REST endpoints, evidence/photo uploads via Multer, and a React dashboard with advanced filtering and Chart.js statistics that cut case-retrieval time by ~70% versus the prior manual process.",
        "image": "assets/images/varun-criminal-case.svg",
        "tags": ["MERN", "JWT", "RBAC", "Chart.js", "Multer"],
        "demoLink": "",
        "codeLink": "https://github.com/gt-varun/Criminal-case-mangement",
    },
    {
        "title": "Namma Metro",
        "category": "Professional Work",
        "description": "Full-stack Bengaluru Metro route finder (MERN): station selector, route & fare cards, and line maps.",
        "longDescription": "A full-stack MERN app for navigating the Bengaluru Metro: pick origin and destination stations to find optimal routes, browse lines, stations, and fare information. Express + Mongoose API with a seeded MongoDB of stations and lines, and a React front end with route, period, and station components.",
        "image": "assets/images/varun-namma-metro.svg",
        "tags": ["MERN", "MongoDB", "Express", "React", "Node.js"],
        "demoLink": "",
        "codeLink": "https://github.com/gt-varun/namma_metro",
    },
    {
        "title": "JWT Docker Service",
        "category": "Professional Work",
        "description": "Containerized full-stack authentication service: JWT register/login flow with a Dockerized Node/Express backend.",
        "longDescription": "A containerized authentication service demonstrating a complete JWT register/login flow. Node.js + Express backend packaged with Docker for reproducible deployment, token-based session handling, and a lightweight front end for registration and login.",
        "image": "assets/images/varun-jwt-docker.png",
        "tags": ["Node.js", "Express", "JWT", "Docker", "MongoDB"],
        "demoLink": "https://jwt-docker-project.vercel.app",
        "codeLink": "https://github.com/gt-varun/JWT_DOCKER_PROJECT",
    },
]

EXPERIENCE = [
    {
        "company": "Spiked AI", "role": "Product Developer Intern",
        "period": "01/2026 – Present", "location": "Remote · Los Angeles, CA",
        "points": [
            "Architected a cross-platform Electron desktop app (Windows & macOS) supporting 2 live audio-capture modes (Zoom/Meet + offline), reducing transcript delivery latency to under 1 second per segment.",
            "Built a Node.js/Express backend handling OS-level permission flows (microphone, screen recording) across 3 OS environments, cutting permission-related onboarding failures to 0.",
            "Integrated the Recall AI Desktop SDK for real-time audio streaming, reducing manual setup from 5 steps to 1 by automating SDK initialisation on first launch.",
            "Wrote 15+ integration tests across audio capture and permission flows; delivered 100% on time across 2 sprint cycles in a 3-person squad.",
        ],
    },
    {
        "company": "einsteini.ai", "role": "Product Developer Intern",
        "period": "09/2025 – Present", "location": "Remote · Los Angeles, CA",
        "points": [
            "Shipped browser extensions for LinkedIn and X (Twitter) using Chrome Extension APIs, resolving 4 cross-platform bugs that had blocked ~30% of users from core functionality.",
            "Designed and implemented a full Stripe subscription system (5 payment states, webhooks, free-trial logic, automated billing) — enabling the product's first paid revenue stream.",
            "Led an AWS-to-GCP migration across 6 services after a security incident, restoring 100% uptime within 48 hours with zero data loss.",
            "Debugged 3 critical OAuth 2.0 failures (Google, Microsoft, LinkedIn) that had blocked new-user registration for 2+ weeks, reducing login error rate to 0%.",
        ],
    },
]

EDUCATION = [
    {"title": "B.E. Information Science", "org": "Jyothy Institute of Technology, VTU",
     "period": "Expected 06/2027 · Bengaluru", "detail": "CGPA: 9.26 / 10"},
    {"title": "Class XII (CBSE)", "org": "Sri Chaitanya Techno School",
     "period": "2023 · Bengaluru", "detail": "88.4%"},
    {"title": "Class X (CBSE)", "org": "Sri Chaitanya Techno School",
     "period": "2021 · Bengaluru", "detail": "91.6%"},
]

ACHIEVEMENTS = [
    {"title": "6th Place — Nationally", "org": "AI Verse Hackathon, BMSCE",
     "detail": "Top 6% of 100+ teams · 72-hour sprint · Dec 2024"},
    {"title": "2nd Place — CSI Coding Challenge", "org": "Jyothy Institute of Technology",
     "detail": "Institute-level competitive programming"},
    {"title": "Competitive Programming", "org": "LeetCode · GeeksforGeeks",
     "detail": "Active in Data Structures & Algorithms practice"},
]

# --------------------------------------------------------------------------
# STYLE HELPERS (inline styles → no dependency on compiled Tailwind classes)
# --------------------------------------------------------------------------
MONO = "font-family:'Geist Mono',ui-monospace,monospace"
RED = "#ef4444"
def esc(s): return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))

def section_header(label, title):
    return (
        f'<div style="margin-bottom:2.5rem">'
        f'<p style="{MONO};font-size:11px;letter-spacing:.25em;text-transform:uppercase;color:{RED};margin:0 0 .6rem">{esc(label)}</p>'
        f'<h2 style="font-size:clamp(2rem,5vw,3.25rem);font-weight:800;letter-spacing:-.02em;color:#fff;margin:0">{esc(title)}</h2>'
        f'</div>'
    )

def wrap(id_, inner):
    return (f'<div style="max-width:1100px;margin:0 auto;padding:0 1.5rem">{inner}</div>')

def card(inner):
    return (f'<div data-reveal data-reveal-from="translateY(30px)" '
            f'style="background:rgba(0,0,0,.4);border:1px solid rgba(63,63,70,.5);'
            f'border-left:3px solid {RED};border-radius:8px;padding:1.5rem 1.75rem;margin-bottom:1.25rem">{inner}</div>')

# --------------------------------------------------------------------------
# 1. data.js  (drives skill tabs + project carousel)
# --------------------------------------------------------------------------
data_js = (
    "/* data.js — Varun Y R portfolio content (projects + skills).\n"
    " * Consumed by main.js to drive the skills tabs and project carousel. */\n"
    "window.SKILLS = " + json.dumps(SKILLS, indent=2, ensure_ascii=False) + ";\n"
    "window.PROJECTS = " + json.dumps(PROJECTS, indent=2, ensure_ascii=False) + ";\n"
)
open(os.path.join(OUT, "js/data.js"), "w", encoding="utf-8").write(data_js)

# --------------------------------------------------------------------------
# 2. placeholder images (projects without a live screenshot + avatar)
# --------------------------------------------------------------------------
def placeholder_svg(title, sub):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0a0a0a"/><stop offset="1" stop-color="#1a0606"/></linearGradient></defs>
  <rect width="1200" height="675" fill="url(#g)"/>
  <rect x="40" y="40" width="1120" height="595" fill="none" stroke="#7f1d1d" stroke-width="2" opacity="0.5"/>
  <text x="80" y="120" fill="#ef4444" font-family="monospace" font-size="22" letter-spacing="6">// CASE FILE</text>
  <text x="80" y="340" fill="#ffffff" font-family="monospace" font-size="64" font-weight="bold">{esc(title)}</text>
  <text x="80" y="400" fill="#a1a1aa" font-family="monospace" font-size="26">{esc(sub)}</text>
  <circle cx="600" cy="337" r="220" fill="none" stroke="#dc2626" stroke-width="1" opacity="0.15"/>
</svg>'''

open(os.path.join(IMG, "varun-mindful-ai.svg"), "w").write(placeholder_svg("Mindful AI", "Multimodal Emotion Detection · ML"))
open(os.path.join(IMG, "varun-criminal-case.svg"), "w").write(placeholder_svg("Criminal Case Mgmt", "MERN · JWT · RBAC"))
open(os.path.join(IMG, "varun-namma-metro.svg"), "w").write(placeholder_svg("Namma Metro", "Bengaluru Metro Route Finder · MERN"))
# Profile photo (varun-avatar.png) is copied from static-src/project-images/.

# --------------------------------------------------------------------------
# 3. index.html transforms
# --------------------------------------------------------------------------
html = open(os.path.join(OUT, "index.html"), encoding="utf-8").read()

# 3a. global identity string replacements
repl = {
    "Yamin Hossain": ME["name"],
    "issan.yamin@gmail.com": ME["email"],
    "github.com/RobinMillford": "github.com/gt-varun",
    "RobinMillford": "gt-varun",
    "/in/yamin-hossain-38a3b3263": "/in/varun-yr-b37687311",
    "varun-y-r": "varun-yr-b37687311",
    "Mohakhali, Bangladesh": "Bengaluru, India",
    "Junior AI Developer @ Betopia Limited": "Product Developer Intern @ Spiked AI",
    "Betopia Limited": "Spiked AI",
    "kaggle.com/yaminh": "leetcode.com/u/varunyr1224",
    'aria-label="Kaggle"': 'aria-label="LeetCode"',
    "www.researchgate.net/profile/Yamin-Hossain-6?ev=hdr_xprf": "github.com/gt-varun",
    "scholar.google.com/citations?user=cjafjKIAAAAJ&amp;hl=en": "github.com/gt-varun",
    "open.spotify.com/user/ly6fajas6b9a8v9zxgx26x0fk?si=3y4RW1XnSa-RRoxOQU4c3w": "github.com/gt-varun",
    "boxd.it/5OYgT": "github.com/gt-varun",
    "trakt.tv/users/gt-varun": "github.com/gt-varun",
    # nav logo: "Y"(gradient) | "amin"(white) | ".ai"(red)  ->  "Varun" | (removed) | " Y R"
    # Collapse "Varun" into ONE text node so prettier's line breaks can't insert a gap.
    'bg-gradient-to-r from-red-500 to-red-600 bg-clip-text text-transparent font-extrabold">Y</span>':
        'text-white font-extrabold">Varun</span>',
    '<span class="text-white">amin</span>': '',
    # footer logo (single span) + any remaining brand spans / ".ai" suffix
    ">Yamin</span": ">Varun</span",
    ">.ai</span": "> Y R</span",
    "@yamin_hossain": "@varunyr",
    # skill-tab aria-labels (DOM order maps to SKILLS order)
    "View Machine Learning skills (current)": "View Languages skills (current)",
    "View Natural Language Processing skills": "View Frontend skills",
    "View Computer Vision skills": "View Backend & APIs skills",
    "View AI Engineering skills": "View Databases & Cloud skills",
    "View Data Engineering skills": "View AI / ML & Tools skills",
    "AI Systems Engineer &amp; Data Scientist": ME["role"],
    "AI Systems Engineer and Data Scientist": ME["role"],
    "AI Systems Engineer": ME["role"],
    "Machine Learning Engineer": "Full-Stack Developer",
    "AI Engineer Bangladesh": "Software Engineer Bengaluru",
    "www.yaminhossain.com": "varunyr.dev",
    "www.yaminhossain.fun": "varunyr.dev",
    "Gemini_Generated_Image_Yamin.png": "varun-avatar.png",
    "assets/images/gemini-generated-image-yamin.png": "assets/images/varun-avatar.png",
}
for a, b in repl.items():
    html = html.replace(a, b)

# 3b. replace whole bespoke sections (keep <section> wrapper, swap inner)
def replace_section_inner(h, id_, inner_html):
    m = re.search(r'<section[^>]*id="' + id_ + r'"[^>]*>', h)
    if not m:
        return h
    start = m.end()
    depth, i = 1, start
    for mm in re.finditer(r'<(/?)section\b', h[start:]):
        depth += -1 if mm.group(1) else 1
        if depth == 0:
            end = start + mm.start()
            return h[:start] + inner_html + h[end:]
    return h

def remove_section(h, id_):
    """Delete an entire <section id="..."> ... </section> block + nav links to it."""
    m = re.search(r'<section[^>]*id="' + id_ + r'"[^>]*>', h)
    if not m:
        return h
    depth = 0
    for mm in re.finditer(r'<(/?)section\b[^>]*>', h[m.start():]):
        depth += -1 if mm.group(1) else 1
        if depth == 0:
            h = h[:m.start()] + h[m.start() + mm.end():]
            break
    # drop any nav/footer anchor pointing at this section
    h = re.sub(r'<a[^>]*href="[^"]*#' + id_ + r'"[^>]*>.*?</a>', "", h, flags=re.S)
    return h

# Remove the "Psych Evaluation" (personal media: Spotify/Letterboxd/Trakt) section.
html = remove_section(html, "personal")

# About
about_inner = wrap("about", section_header("Intelligence Brief", "The Operative") +
    f'<p style="max-width:760px;color:#d4d4d8;font-size:1.1rem;line-height:1.8">{esc(BIO)}</p>')
html = replace_section_inner(html, "about", about_inner)

# Experience — "Field Operations" timeline (ID cards + ACTIVE MISSION + log)
def exp_entry(i, e):
    active = "Present" in e["period"]
    dot = RED if active else "#52525b"
    pts = "".join(
        f'<li style="margin:.5rem 0;padding-left:1.3rem;position:relative;color:#d4d4d8;'
        f'font-size:.95rem;line-height:1.6">'
        f'<span style="position:absolute;left:0;top:.5em;width:7px;height:7px;'
        f'background:{RED};box-shadow:0 0 6px {RED}"></span>{esc(p)}</li>'
        for p in e["points"])
    badge = ("" if not active else
             f'<span style="{MONO};font-size:11px;color:{RED};border:1px solid {RED};'
             f'border-radius:6px;padding:.25rem .75rem;letter-spacing:.06em">◆ ACTIVE MISSION</span>')
    return (
        f'<div data-reveal data-reveal-from="translateX(24px)" '
        f'style="position:relative;padding-left:2.4rem;margin-bottom:2.5rem">'
        # timeline node
        f'<span style="position:absolute;left:-7px;top:.3rem;width:15px;height:15px;border-radius:50%;'
        f'background:{dot};border:3px solid #0a0a0a;box-shadow:0 0 14px {dot if active else "transparent"}"></span>'
        # date + badge row
        f'<div style="display:flex;flex-wrap:wrap;gap:.9rem;align-items:center;margin-bottom:.8rem">'
        f'<span style="{MONO};font-size:12px;color:#a1a1aa;letter-spacing:.04em;display:inline-flex;align-items:center;gap:.45rem">'
        f'<span style="width:8px;height:8px;background:{RED};display:inline-block"></span>{esc(e["period"])}</span>{badge}</div>'
        # card
        f'<div style="display:flex;gap:1.3rem;background:rgba(239,68,68,.05);'
        f'border:1px solid rgba(239,68,68,.35);border-left:4px solid {RED};'
        f'border-radius:12px;padding:1.5rem 1.6rem;box-shadow:0 0 24px rgba(239,68,68,.06)">'
        # ID badge
        f'<div style="flex-shrink:0;text-align:center;border:1px solid rgba(63,63,70,.7);'
        f'border-radius:8px;padding:.5rem .75rem;height:fit-content">'
        f'<div style="{MONO};font-size:9px;color:#71717a;letter-spacing:.1em">ID</div>'
        f'<div style="{MONO};font-size:1.4rem;font-weight:800;color:{RED};line-height:1.1">{str(i+1).zfill(2)}</div></div>'
        # content
        f'<div style="flex:1;min-width:0">'
        f'<h3 style="margin:0;color:#fafafa;font-size:1.35rem;font-weight:800;letter-spacing:-.01em">{esc(e["role"])}</h3>'
        f'<div style="{MONO};font-size:13px;color:{RED};font-weight:700;letter-spacing:.05em;margin:.2rem 0 .55rem">{esc(e["company"].upper())}</div>'
        f'<div style="{MONO};font-size:12px;color:#a1a1aa;margin-bottom:1.1rem">{esc(e["location"])} · {esc(e.get("type","Internship"))}</div>'
        f'<div style="{MONO};font-size:11px;color:{RED};letter-spacing:.1em;margin-bottom:.4rem">OPERATIONAL LOG:</div>'
        f'<ul style="list-style:none;padding:0;margin:0">{pts}</ul>'
        f'</div></div></div>')

exp_timeline = (
    f'<div style="position:relative;max-width:900px">'
    f'<div style="position:absolute;left:0;top:.5rem;bottom:1rem;width:2px;'
    f'background:linear-gradient(to bottom,{RED},rgba(239,68,68,.12))"></div>'
    + "".join(exp_entry(i, e) for i, e in enumerate(EXPERIENCE))
    + '</div>')
html = replace_section_inner(html, "experience", wrap("experience",
    section_header("Mission Log", "Field Operations") + exp_timeline))

# Education
edu_cards = ""
for e in EDUCATION:
    edu_cards += card(
        f'<div style="display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem;align-items:baseline">'
        f'<h3 style="margin:0;color:#fafafa;font-size:1.2rem;font-weight:700">{esc(e["title"])}</h3>'
        f'<span style="{MONO};font-size:12px;color:#a1a1aa">{esc(e["period"])}</span></div>'
        f'<p style="color:#d4d4d8;margin:.4rem 0 .2rem">{esc(e["org"])}</p>'
        f'<p style="{MONO};font-size:13px;color:{RED};margin:0">{esc(e["detail"])}</p>')
html = replace_section_inner(html, "education", wrap("education",
    section_header("Academic Records", "Academic Archive") + edu_cards))

# Publications -> Achievements
ach_cards = ""
for a in ACHIEVEMENTS:
    ach_cards += card(
        f'<h3 style="margin:0 0 .3rem;color:#fafafa;font-size:1.15rem;font-weight:700">{esc(a["title"])}</h3>'
        f'<p style="color:#d4d4d8;margin:0 0 .2rem">{esc(a["org"])}</p>'
        f'<p style="{MONO};font-size:13px;color:#a1a1aa;margin:0">{esc(a["detail"])}</p>')
# a simple LeetCode profile link in the Achievements section
leetcode_link = (
    f'<a href="{LEETCODE_URL}" target="_blank" rel="noopener noreferrer" '
    f'style="display:inline-flex;align-items:center;gap:.5rem;{MONO};font-size:.95rem;'
    f'color:{RED};text-decoration:none;border:1px solid {RED};border-radius:8px;'
    f'padding:.6rem 1.1rem;margin-top:.5rem">'
    f'LEETCODE » leetcode.com/u/varunyr1224 ↗</a>')
html = replace_section_inner(html, "publications", wrap("publications",
    section_header("Commendations", "Achievements") + ach_cards + leetcode_link))

# Contact — keep the original "THE SIGNAL" design, personalise it in place.
# Remove the duplicate second email / phone / location entries (Yamin had two).
html = re.sub(
    r'<div class="flex items-center gap-2"><a href="mailto:robinmill4d@gmail.com".*?</div>',
    "", html, flags=re.S)
html = re.sub(
    r'<div class="flex items-center gap-2"><p[^>]*>\+880 \(197\) 794-0357</p></div>',
    "", html)
html = re.sub(
    r'<div class="flex items-center gap-2"><p[^>]*>Dhaka, Bangladesh</p></div>',
    "", html)
# Swap the remaining details to Varun's.
html = html.replace("+91 (630) 101-1373", "+91 86186 68003")
html = html.replace("Andhra Pradesh, India", "Bengaluru, India")
html = html.replace("data science opportunity", "full-stack or AI engineering opportunity")
html = html.replace("DATA_SCIENCE &amp; MACHINE_LEARNING", "FULL_STACK &amp; AI_ENGINEERING")
html = html.replace("DATA_SCIENCE & MACHINE_LEARNING", "FULL_STACK & AI_ENGINEERING")
html = html.replace("DHAKA_BD", "BENGALURU_IN")

# 3c. project thumbnail strip — regenerate for the new projects
THUMB_TPL = '''<div data-case-card="true"><button class="relative flex-shrink-0 group cursor-pointer overflow-hidden rounded-sm transition-all duration-500 w-[160px] h-[110px] md:w-[200px] md:h-[130px] border border-zinc-800/60 hover:border-red-500/40 hover:shadow-[0_0_15px_rgba(220,38,38,0.15)]" aria-label="View case file: {title}" tabindex="0"><img alt="{title}" loading="lazy" decoding="async" class="object-cover transition-all duration-700 scale-100 brightness-50 saturate-0 group-hover:brightness-75 group-hover:saturate-50" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent" src="{img}"/><div class="absolute inset-0 transition-opacity duration-500 bg-gradient-to-t from-black/90 via-red-950/30 to-red-950/10 group-hover:from-black/70"></div><div class="scanline-overlay opacity-50"></div><div class="absolute top-1.5 left-1.5 z-20 font-mono text-[10px] font-bold tracking-widest px-1.5 py-0.5 rounded-sm bg-black/60 text-red-400/70 group-hover:text-red-400">#{num:03d}</div><div class="absolute bottom-1.5 left-1.5 right-1.5 z-20"><p class="font-mono text-[9px] md:text-[10px] uppercase tracking-wider truncate text-zinc-200 group-hover:text-zinc-300">{title}</p></div></button></div>'''

thumbs = "".join(THUMB_TPL.format(title=esc(p["title"]), img=p["image"], num=i + 1)
                 for i, p in enumerate(PROJECTS))
# replace inner of the horizontal strip container
m = re.search(r'<div[^>]*class="[^"]*hide-scrollbar[^"]*"[^>]*>', html)
if m:
    start = m.end()
    depth, i = 1, start
    for mm in re.finditer(r'<(/?)div\b', html[start:]):
        depth += -1 if mm.group(1) else 1
        if depth == 0:
            end = start + mm.start()
            html = html[:start] + thumbs + html[end:]
            break

# 3c-ii. Align the static featured-viewer + skill-panel initial content with the
#        new data[0]/SKILLS[0]. main.js locates those widgets by matching the
#        first item's text, so the initial labels must match the new content
#        (this also gives no-JS users correct content).
html = html.replace("Qurany AI", PROJECTS[0]["title"])      # featured title + alt anchor
html = html.replace("LangGraph", PROJECTS[0]["tags"][0])    # first tag anchor -> React
# skill-panel heading (scoped to its specific h3 so the project filter chip stays)
html = re.sub(r'(<h3 class="text-xl md:text-3xl font-bold font-mono uppercase[^"]*">\s*)Machine Learning(\s*</h3>)',
              r'\g<1>' + SKILLS[0]["title"] + r'\g<2>', html)
html = html.replace("Neural Networks", SKILLS[0]["skills"][0])  # first skill row anchor -> Java

# 3d-2. remove footer "Made with ♥" span (+ its leading separator)
html = re.sub(
    r'<span class="text-zinc-400">•</span>\s*<span class="flex items-center gap-1">Made with\s*<svg.*?</svg>\s*</span>',
    "", html, flags=re.S,
)
# 3d-3. nav/footer label: Publications -> Achievements (section id stays #publications)
html = html.replace(">Publications<", ">Achievements<")

# 3e. hero "Access Dossier" button -> a download link for the resume PDF
html = re.sub(
    r'<button(\b[^>]*)>((?:(?!</?button).)*?)Access Dossier(.*?)</button>',
    r'<a\1 href="Varun_Y_R_Resume.pdf" download aria-label="Download Varun Y R resume">\2Resume\3</a>',
    html, flags=re.S,
)
# the contact-card "Access Dossier" is an <a> to Yamin's Google Drive — repoint
# it to the local resume PDF, then relabel the remaining occurrence.
html = html.replace(
    'href="https://drive.google.com/file/d/1iSJFPRbDO_9zftAOn4-regAKCTnt-Uo3/view?usp=drive_link" target="_blank" rel="noopener noreferrer"',
    'href="Varun_Y_R_Resume.pdf" download rel="noopener"')
html = html.replace("Access Dossier", "Resume")

# 3f. favicon links → VYR icons (fix broken external ref + add crisp PNG)
html = html.replace("https://varunyr.dev/favicon-16x16.png", "favicon-32.png")
html = html.replace(
    '<link rel="icon" href="favicon.ico" />',
    '<link rel="icon" href="favicon.ico" />'
    '<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png" />',
    1)

# 3g. PWA manifest → Varun + VYR icons
manifest = {
    "name": "Varun Y R | Full-Stack & AI Developer",
    "short_name": "Varun YR",
    "description": "Portfolio of Varun Y R — Full-Stack and AI Developer building production web, desktop, and AI applications.",
    "start_url": "/", "display": "standalone",
    "background_color": "#000000", "theme_color": "#ef4444",
    "orientation": "portrait-primary",
    "icons": [
        {"src": "/favicon.ico", "sizes": "48x48", "type": "image/x-icon"},
        {"src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png", "purpose": "any maskable"},
        {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
    ],
    "categories": ["portfolio", "technology"], "lang": "en", "dir": "ltr",
}
open(os.path.join(OUT, "site.webmanifest"), "w").write(json.dumps(manifest, indent=2))

open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)
print(f"personalized: {len(PROJECTS)} projects, {len(SKILLS)} skill groups, "
      f"{len(EXPERIENCE)} jobs, {len(EDUCATION)} edu, {len(ACHIEVEMENTS)} achievements")
