# import streamlit as st

# st.set_page_config(layout="wide")

# # Custom CSS for Glassmorphism
# st.markdown(f"""
#     <style>
#     /* Background with scale to prevent white cast */
#     .stApp {{
#         background: url("https://www.taaltech.com/wp-content/uploads/2025/02/TL-on-plant-Engineering-Top-Trends-in-Plant-Engineering-for-EPC-Projects-in-2025-banner-002.jpg");
#         background-size: cover;
#     }}
    
#     .stApp::before {{
#         content: "";
#         position: fixed;
#         top: -10px; left: -10px; right: -10px; bottom: -10px;
#         background: inherit;
#         filter: blur(12px) brightness(0.7);
#         transform: scale(1.1); 
#         z-index: -1;
#     }}

#     /* GLASS EFFECT BOX */
#     .query-output-box {{
#         background: rgba(255, 255, 255, 0.05); /* Very light white transparency */
#         backdrop-filter: blur(20px) saturate(180%); /* Frosted glass effect */
#         -webkit-backdrop-filter: blur(20px) saturate(180%);
#         border: 1px solid rgba(255, 255, 255, 0.2); /* Thin 'glass' edge */
#         border-radius: 24px;
#         padding: 40px;
#         color: white;
#         width: 100%;
#         max-width: 850px;
#         min-height: 300px;
#         box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37); /* Soft shadow */
#         margin: 50px auto;
#         font-family: 'Segoe UI', sans-serif;
#     }}

#     header, footer {{visibility: hidden;}}
#     </style>
#     """, unsafe_allow_html=True)

# # Layout
# if "result_text" not in st.session_state:
#     st.session_state.result_text = "The glass effect result box is now active. Your query output will appear here."

# # Center the Box
# _, center_col, _ = st.columns([1, 4, 1])
# with center_col:
#     st.markdown(f'<div class="query-output-box">{st.session_state.result_text}</div>', unsafe_allow_html=True)

# # ChatGPT Style Bar with + Icon
# prompt = st.chat_input("Ask anything or upload document...", accept_file=True)

# if prompt:
#     res = f"**Prompt:** {prompt.text}"
#     if prompt.files:
#         res += f"\n\n📂 Document: {prompt.files.name}"
#     st.session_state.result_text = res
#     st.rerun()


# import streamlit as st

# # 1. Page Setup
# st.set_page_config(layout="wide", page_title="EPC Reasoning Engine")

# # 2. CSS for FULL Glass Effect on Input Box & Result Box
# st.markdown(f"""
#     <style>
#     /* Background Fix - No white cast */
#     .stApp {{
#         background: url("https://www.taaltech.com/wp-content/uploads/2025/02/TL-on-plant-Engineering-Top-Trends-in-Plant-Engineering-for-EPC-Projects-in-2025-banner-002.jpg");
#         background-size: cover;
#         background-position: center;
#         background-attachment: fixed;
#     }}
    
#     .stApp::before {{
#         content: "";
#         position: fixed;
#         top: -10px; left: -10px; right: -10px; bottom: -10px;
#         background: inherit;
#         filter: blur(8px) brightness(0.7);
#         transform: scale(1.1); 
#         z-index: -1;
#     }}

#     /* Result Box Glass Effect */
#     .query-output-box {{
#         background: rgba(255, 255, 255, 0.05) !important;
#         backdrop-filter: blur(20px) saturate(180%) !important;
#         -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
#         border: 1px solid rgba(255, 255, 255, 0.2) !important;
#         box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
#         border-radius: 24px;
#         padding: 40px;
#         color: white;
#         width: 100%;
#         max-width: 850px;
#         min-height: 300px;
#         margin: 50px auto;
#         font-family: 'Inter', sans-serif;
#     }}

#     /* FULL GLASS INPUT BOX (Including + and Send buttons) */
#     [data-testid="stChatInput"] {{
#         background-color: transparent !important;
#         border: none !important;
#     }}

#     /* Target the inner wrapper that holds the + icon, text, and send button */
#     [data-testid="stChatInput"] > div {{
#         background: rgba(255, 255, 255, 0.1) !important;
#         backdrop-filter: blur(25px) saturate(180%) !important;
#         -webkit-backdrop-filter: blur(25px) saturate(180%) !important;
#         border: 1px solid rgba(255, 255, 255, 0.3) !important;
#         border-radius: 20px !important;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
#     }}

#     /* Make the actual typing area and button areas transparent */
#     [data-testid="stChatInput"] textarea, 
#     [data-testid="stChatInput"] div[role="button"],
#     [data-testid="stChatInput"] button {{
#         background-color: transparent !important;
#         color: white !important;
#     }}

#     /* Placeholder text color */
#     [data-testid="stChatInput"] textarea::placeholder {{
#         color: rgba(255, 255, 255, 0.6) !important;
#     }}
    
#     header, footer {{visibility: hidden;}}
#     </style>
#     """, unsafe_allow_html=True)

# # 3. Main Result Box (Centered with 1:3:1 ratio)
# if "result_text" not in st.session_state:
#     st.session_state.result_text = "Analysis result will appear here in this glass box..."

# col1, col2, col3 = st.columns([1, 3, 1]) 
# with col2:
#     st.markdown(f'<div class="query-output-box">{st.session_state.result_text}</div>', unsafe_allow_html=True)

# # 4. Chat Input with + Icon (accept_file=True)
# prompt = st.chat_input("Ask a question or upload a document...", accept_file=True)

# if prompt:
#     # Logic to update results
#     res = f"**User Query:** {prompt.text}"
#     if prompt.files:
#         res += f"\n\n📂 **Document Attached:** {prompt.files.name}"
#     st.session_state.result_text = res
#     st.rerun()


# import streamlit as st

# # 1. Page Setup
# st.set_page_config(layout="wide", page_title="EPC Reasoning Engine")

# # 2. CSS for FULL Glass Effect on Input Box & Result Box
# st.markdown(f"""
#     <style>
#     /* Background Fix - No white cast */
#     .stApp {{
#         background: url("https://www.taaltech.com/wp-content/uploads/2025/02/TL-on-plant-Engineering-Top-Trends-in-Plant-Engineering-for-EPC-Projects-in-2025-banner-002.jpg");
#         background-size: cover;
#         background-position: center;
#         background-attachment: fixed;
#     }}
    
#     .stApp::before {{
#         content: "";
#         position: fixed;
#         top: -10px; left: -10px; right: -10px; bottom: -10px;
#         background: inherit;
#         filter: blur(8px) brightness(0.7);
#         transform: scale(1.1); 
#         z-index: -1;
#     }}

#     /* Result Box Glass Effect */
#     .query-output-box {{
#         background: rgba(255, 255, 255, 0.05) !important;
#         backdrop-filter: blur(20px) saturate(180%) !important;
#         -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
#         border: 1px solid rgba(255, 255, 255, 0.2) !important;
#         box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
#         border-radius: 24px;
#         padding: 40px;
#         color: white;
#         width: 100%;
#         max-width: 850px;
#         min-height: 300px;
#         margin: 50px auto;
#         font-family: 'Inter', sans-serif;
#     }}

#     /* FULL GLASS INPUT BOX (Including + and Send buttons) */
#     /* Targets the outer container, making it invisible */
#     [data-testid="stChatInput"] {{
#         background-color: transparent !important;
#         border: none !important;
#     }}

#     /* Targets the inner div that has the actual visual elements, applying glass to that */
#     [data-testid="stChatInput"] > div {{
#         background: rgba(255, 255, 255, 0.1) !important;
#         backdrop-filter: blur(25px) saturate(180%) !important;
#         -webkit-backdrop-filter: blur(25px) saturate(180%) !important;
#         border: 1px solid rgba(255, 255, 255, 0.3) !important;
#         border-radius: 20px !important;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
#         /* Ensures the glass pane floats nicely above the bottom edge */
#         margin-bottom: 20px; 
#     }}

#     /* Make the actual typing area and button areas transparent */
#     [data-testid="stChatInput"] textarea, 
#     [data-testid="stChatInput"] div[role="button"],
#     [data-testid="stChatInput"] button {{
#         background-color: transparent !important;
#         color: white !important;
#     }}

#     /* Placeholder text color */
#     [data-testid="stChatInput"] textarea::placeholder {{
#         color: rgba(255, 255, 255, 0.6) !important;
#     }}
    
#     header, footer {{visibility: hidden;}}
#     </style>
#     """, unsafe_allow_html=True)

# # 3. Main Result Box (Centered with 1:3:1 ratio)
# if "result_text" not in st.session_state:
#     st.session_state.result_text = "Analysis result will appear here in this glass box..."

# col1, col2, col3 = st.columns([1, 3, 1]) 
# with col2:
#     st.markdown(f'<div class="query-output-box">{st.session_state.result_text}</div>', unsafe_allow_html=True)

# # 4. Chat Input with + Icon (accept_file=True)
# prompt = st.chat_input("Ask a question or upload a document...", accept_file=True)

# if prompt:
#     # Logic to update results
#     res = f"**User Query:** {prompt.text}"
#     if prompt.files:
#         res += f"\n\n📂 **Document Attached:** {prompt.files.name}"
#     st.session_state.result_text = res
#     st.rerun()



# import streamlit as st

# # 1. Page Setup
# st.set_page_config(layout="wide", page_title="EPC Reasoning Engine")

# # 2. CSS for FULL Glass Effect on Input Box & Result Box
# st.markdown("""
# <style>
# .stApp {
#     background: url("https://www.taaltech.com/wp-content/uploads/2025/02/TL-on-plant-Engineering-Top-Trends-in-Plant-Engineering-for-EPC-Projects-in-2025-banner-002.jpg");
#     background-size: cover;
#     background-position: center;
#     background-attachment: fixed;
# }

# .stApp::before {
#     content: "";
#     position: fixed;
#     inset: -10px;
#     background: inherit;
#     filter: blur(8px) brightness(0.7);
#     transform: scale(1.1);
#     z-index: -1;
# }

# /* Result Box */
# .query-output-box {
#     background: rgba(255, 255, 255, 0.05);
#     backdrop-filter: blur(20px) saturate(180%);
#     -webkit-backdrop-filter: blur(20px) saturate(180%);
#     border: 1px solid rgba(255, 255, 255, 0.2);
#     box-shadow: 0 8px 32px rgba(0,0,0,0.37);
#     border-radius: 24px;
#     padding: 40px;
#     color: white;
#     max-width: 850px;
#     min-height: 300px;
#     margin: 50px auto;
# }

# /* Chat input glass */
# [data-testid="stChatInput"] {
#     background-color: transparent;
#     border: none;
# }

# [data-testid="stChatInput"] > div {
#     background: rgba(255, 255, 255, 0.1);
#     backdrop-filter: blur(25px) saturate(180%);
#     -webkit-backdrop-filter: blur(25px) saturate(180%);
#     border: 1px solid rgba(255, 255, 255, 0.3);
#     border-radius: 20px;
# }

# [data-testid="stChatInput"] textarea,
# [data-testid="stChatInput"] button {
#     background-color: transparent;
#     color: white;
# }

# [data-testid="stChatInput"] textarea::placeholder {
#     color: rgba(255,255,255,0.6);
# }

# header, footer {visibility: hidden;}
# </style>
# """, unsafe_allow_html=True)

# # 3. Session state
# if "result_text" not in st.session_state:
#     st.session_state.result_text = "Analysis result will appear here in this glass box..."

# # 4. Result Box (Centered)
# col1, col2, col3 = st.columns([1, 3, 1])
# with col2:
#     st.markdown(
#         f'<div class="query-output-box">{st.session_state.result_text}</div>',
#         unsafe_allow_html=True
#     )

# # 5. Chat Input (Glass + +icon + send)
# prompt = st.chat_input(
#     "Ask a question or upload a document...",
#     accept_file=True
# )

# if prompt:
#     result = f"**User Query:** {prompt.text}"

#     if prompt.files:
#         result += f"\n\n📂 **Document Attached:** {prompt.files.name}"

#     st.session_state.result_text = result


import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/api/query"

# --------------------------------------------------
# 1. PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="EPC Reasoning Engine"
)

# --------------------------------------------------
# 2. GLOBAL GLASS + BACKGROUND CSS (FIXED)
# --------------------------------------------------
st.markdown("""
<style>

/* === REMOVE DEFAULT STREAMLIT PADDING === */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* === BACKGROUND IMAGE FULL SCREEN === */
.stApp {
    min-height: 100vh;
    background-image: url("https://www.taaltech.com/wp-content/uploads/2025/02/TL-on-plant-Engineering-Top-Trends-in-Plant-Engineering-for-EPC-Projects-in-2025-banner-002.jpg");
    background-size: cover;              /* IMPORTANT */
    background-position: center;         /* IMPORTANT */
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* === DARK OVERLAY (FIXED Z-INDEX) === */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(11, 77, 162, 0.45);
    z-index: 0;                           /* FIX */
}

/* Bring content above overlay */
.stApp > div {
    position: relative;
    z-index: 1;
}

/* Hide header & footer */
header, footer {
    visibility: hidden;
}

/* --------------------------------------------------
   RESULT BOX (GLASS)
-------------------------------------------------- */
.query-output-box {
    background: rgba(0, 0, 0, 0.55);   /* DARK GLASS */
    backdrop-filter: blur(22px);
    -webkit-backdrop-filter: blur(22px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    box-shadow: 0 14px 45px rgba(0,0,0,0.7);
    border-radius: 26px;
    padding: 40px;

    color: #ffffff !important;        /* FORCE WHITE */
    font-size: 16px;
    line-height: 1.7;
    word-wrap: break-word;
    white-space: normal;

    max-width: 900px;
    min-height: 150px;
    margin: 60px auto;
}

/* --------------------------------------------------
   CHAT INPUT – GLASS BAR
-------------------------------------------------- */
# [data-testid="stChatInput"] {
#     background: transparent !important;
#     border: none !important;
#     padding: 0 !important;
# }

# [data-testid="stChatInput"] > div {
#     background: rgba(255, 255, 255, 0.14) !important;
#     backdrop-filter: blur(30px) saturate(180%) !important;
#     -webkit-backdrop-filter: blur(30px) saturate(180%) !important;
#     border: 1px solid rgba(255, 255, 255, 0.35) !important;
#     border-radius: 28px !important;
#     box-shadow: 0 10px 45px rgba(0,0,0,0.5) !important;
#     max-width: 900px;
#     margin: 0 auto 20px auto;
# }

# [data-testid="stChatInput"] textarea {
#     background: transparent !important;
#     color: white !important;
#     font-size: 16px;
# }

# [data-testid="stChatInput"] textarea::placeholder {
#     color: rgba(255,255,255,0.65) !important;
# }

# [data-testid="stChatInput"] button {
#     background: transparent !important;
#     color: white !important;
#     border-radius: 50%;
# }

/* Remove bottom black gap */
[data-testid="stBottomBlockContainer"] {
    padding-bottom: 0 !important;
}
/* REMOVE STREAMLIT DEFAULT BLACK BACKGROUND */
.stApp {
    background-color: transparent !important;
}

[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}

[data-testid="stMainBlockContainer"] {
    background-color: transparent !important;
}
/* === FORCE OUTPUT TEXT TO WHITE === */

/* Markdown headers */
h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

/* Normal text (st.write, st.markdown) */
p, span, div, li {
    color: white !important;
}

/* Streamlit caption (sources) */
[data-testid="stCaption"] {
    color: rgba(255, 255, 255, 0.85) !important;
}

/* Error / warning visibility */
[data-testid="stAlert"] {
    color: white !important;
}
/* === SOURCES: FORCE PURE WHITE === */

/* Caption text (st.caption) */
[data-testid="stCaption"] {
    color: white !important;
    opacity: 1 !important;
}

/* Bullet / list items inside markdown */
ul li, ol li {
    color: white !important;
}

/* Any links that may appear in sources */
a {
    color: white !important;
    text-decoration: underline;
}
# /* Output container box */
# .rag-box {
#     background: rgba(0, 0, 0, 0.55);
#     border-radius: 14px;
#     padding: 20px;
#     margin-top: 15px;
#     border: 1px solid rgba(255,255,255,0.15);
#     box-shadow: 0 8px 25px rgba(0,0,0,0.3);
#     height:500vh;
# }

# /* Force white text inside box */
# .rag-box * {
#     color: white !important;
# }

# /* Source captions */
# [data-testid="stCaption"] {
#     color: white !important;
#     opacity: 1 !important;
# }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 3. SESSION STATE
# --------------------------------------------------
if "result_text" not in st.session_state:
    st.session_state.result_text = (
        "📄 <b>EPC Reasoning Output</b><br><br>"
        "Your document-based analysis or answer will appear here."
    )

# --------------------------------------------------
# 4. RESULT BOX (CENTERED)
# --------------------------------------------------
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown(
        f'<div class="query-output-box">{st.session_state.result_text}</div>',
        unsafe_allow_html=True
    )

# --------------------------------------------------
# 5. CHAT INPUT
# --------------------------------------------------
prompt = st.chat_input(
    "Ask a question or upload a document…",
    accept_file=True
)

# --------------------------------------------------
# 6. BACKEND LOGIC (DEMO)
# --------------------------------------------------
if prompt:
    with st.spinner("🔍 Analyzing document..."):
        payload = {
            "query": prompt.text,
            "document_name": prompt.files[0].name if prompt.files else None
        }

        try:
            # response = requests.post(BACKEND_URL, json=payload, timeout=120)
            # response.raise_for_status()
            # data = response.json()

            # # Format output nicely
            # answer = data.get("answer", "No answer returned.")
            # confidence = data.get("confidence", 0)
            # sources = data.get("sources", [])

            # output = f"""
            # <b>🧠 Answer</b><br><br>
            # {answer}<br><br>
            # <b>📊 Confidence:</b> {confidence}
            # """

            # if sources:
            #     output += "<br><br><b>📚 Sources:</b><br>"
            #     for s in sources:
            #         output += f"- {s['name']}<br>"

            # st.session_state.result_text = output
            response = requests.post(BACKEND_URL, json=payload).json()
            st.markdown('<div class="rag-box">',unsafe_allow_html=True)
            if "answer" in response:
                st.markdown("### 🧠 Answer")
                st.write(response["answer"])
            else:
                st.error("No answer returned from backend")
            if response.get("sources"):
                st.markdown("### 📚 Sources")
                for src in response["sources"]:
                    st.caption(f"📄 {src['name']}")
            st.markdown('</div',unsafe_allow_html=True)

        except requests.exceptions.RequestException as e:
            st.session_state.result_text = f"❌ Backend error: {e}"