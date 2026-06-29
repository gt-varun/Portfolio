/* data.js — Varun Y R portfolio content (projects + skills).
 * Consumed by main.js to drive the skills tabs and project carousel. */
window.SKILLS = [
  {
    "title": "Languages",
    "skills": [
      "Java",
      "JavaScript (ES6+)",
      "Python",
      "C",
      "Swift"
    ]
  },
  {
    "title": "Frontend",
    "skills": [
      "React.js",
      "Electron",
      "Chrome Extensions",
      "HTML5",
      "CSS3"
    ]
  },
  {
    "title": "Backend & APIs",
    "skills": [
      "Node.js",
      "Express.js",
      "REST API Design",
      "JWT",
      "OAuth 2.0",
      "Stripe"
    ]
  },
  {
    "title": "Databases & Cloud",
    "skills": [
      "MongoDB",
      "MySQL",
      "AWS (EC2/S3)",
      "Google Cloud",
      "CI/CD",
      "Git"
    ]
  },
  {
    "title": "AI / ML & Tools",
    "skills": [
      "TensorFlow",
      "HuggingFace",
      "OpenCV",
      "Generative AI",
      "Postman"
    ]
  }
];
window.PROJECTS = [
  {
    "title": "BharatAssist AI",
    "category": "AI Agents",
    "description": "AI-powered government-scheme advisor that matches Indian citizens to welfare schemes they're eligible for — in their own language.",
    "longDescription": "BharatAssist AI is a multilingual platform that helps Indian citizens discover and apply for government welfare schemes. It intelligently matches 50+ schemes to a user's eligibility from their profile, explains requirements in plain language across multiple Indian languages, and lets users track applications end to end. Built with React 18 + TypeScript on the front end and Supabase (PostgreSQL) for data and auth.",
    "image": "assets/images/varun-bharatassist.png",
    "tags": [
      "React",
      "TypeScript",
      "Supabase",
      "PostgreSQL",
      "AI"
    ],
    "demoLink": "https://bharat-assist-ai-olive.vercel.app",
    "codeLink": "https://github.com/gt-varun/BharatAssist-AI"
  },
  {
    "title": "BTP Parking Intelligence",
    "category": "Data Analysis",
    "description": "Full-stack MERN platform backed by a scikit-learn model trained on a 298,450-record Bangalore Traffic Police dataset.",
    "longDescription": "A full-stack MERN conversion of the Bangalore Traffic Police parking-intelligence prototype. Every hardcoded placeholder from the original was replaced with a real model trained on a 298,450-record BTP dataset (Python + pandas + scikit-learn), surfacing genuine violation, challan, and junction analytics. MongoDB + Mongoose data layer, Node/Express API, and a React dashboard with a live violation map of Bengaluru.",
    "image": "assets/images/varun-btp-parking.png",
    "tags": [
      "MERN",
      "MongoDB",
      "Python",
      "scikit-learn",
      "React"
    ],
    "demoLink": "https://btp-parking-intelligence.vercel.app",
    "codeLink": "https://github.com/gt-varun/btp-parking-intelligence"
  },
  {
    "title": "Mindful AI",
    "category": "Machine Learning",
    "description": "Real-time multimodal emotion detection fusing voice, facial expression, and heart rate into one output with sub-2-second latency.",
    "longDescription": "A real-time AI pipeline that fuses three simultaneous signal types — voice, facial expression, and heart rate — into a single unified emotion output, achieving under 2-second end-to-end latency on standard hardware. Built in a 72-hour sprint and ranked 6th nationally (top 6%) out of 100+ teams at the AI Verse Hackathon, BMSCE.",
    "image": "assets/images/varun-mindful-ai.svg",
    "tags": [
      "Python",
      "TensorFlow",
      "OpenCV",
      "Computer Vision",
      "Multimodal"
    ],
    "demoLink": "",
    "codeLink": ""
  },
  {
    "title": "Quizmify",
    "category": "Professional Work",
    "description": "AI-powered quiz platform: generate intelligent quizzes, share via unique codes, and track real-time results with analytics.",
    "longDescription": "A full-stack quiz platform with 8 REST API endpoints (quiz creation, participation, scoring) supporting concurrent multi-user sessions with zero race conditions and instant result delivery. Generate AI-assisted quizzes, share them with unique join codes, and track live results with detailed analytics.",
    "image": "assets/images/varun-quizmify.png",
    "tags": [
      "React",
      "Node.js",
      "Express",
      "MongoDB",
      "AI"
    ],
    "demoLink": "https://quizmify-delta.vercel.app",
    "codeLink": "https://github.com/gt-varun/Quizmify"
  },
  {
    "title": "Criminal Case Management System",
    "category": "Professional Work",
    "description": "MERN legal platform with 3-role RBAC, JWT auth, 12+ tested REST endpoints, evidence uploads, and a Chart.js analytics dashboard.",
    "longDescription": "A role-based (RBAC) case-management system for criminal cases, complaints, and records. Three access-controlled roles, JWT authentication, 12+ tested REST endpoints, evidence/photo uploads via Multer, and a React dashboard with advanced filtering and Chart.js statistics that cut case-retrieval time by ~70% versus the prior manual process.",
    "image": "assets/images/varun-criminal-case.svg",
    "tags": [
      "MERN",
      "JWT",
      "RBAC",
      "Chart.js",
      "Multer"
    ],
    "demoLink": "",
    "codeLink": "https://github.com/gt-varun/Criminal-case-mangement"
  },
  {
    "title": "Namma Metro",
    "category": "Professional Work",
    "description": "Full-stack Bengaluru Metro route finder (MERN): station selector, route & fare cards, and line maps.",
    "longDescription": "A full-stack MERN app for navigating the Bengaluru Metro: pick origin and destination stations to find optimal routes, browse lines, stations, and fare information. Express + Mongoose API with a seeded MongoDB of stations and lines, and a React front end with route, period, and station components.",
    "image": "assets/images/varun-namma-metro.svg",
    "tags": [
      "MERN",
      "MongoDB",
      "Express",
      "React",
      "Node.js"
    ],
    "demoLink": "",
    "codeLink": "https://github.com/gt-varun/namma_metro"
  },
  {
    "title": "JWT Docker Service",
    "category": "Professional Work",
    "description": "Containerized full-stack authentication service: JWT register/login flow with a Dockerized Node/Express backend.",
    "longDescription": "A containerized authentication service demonstrating a complete JWT register/login flow. Node.js + Express backend packaged with Docker for reproducible deployment, token-based session handling, and a lightweight front end for registration and login.",
    "image": "assets/images/varun-jwt-docker.png",
    "tags": [
      "Node.js",
      "Express",
      "JWT",
      "Docker",
      "MongoDB"
    ],
    "demoLink": "https://jwt-docker-project.vercel.app",
    "codeLink": "https://github.com/gt-varun/JWT_DOCKER_PROJECT"
  }
];
