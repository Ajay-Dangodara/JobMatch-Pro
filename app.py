import streamlit as st
import pdfplumber
import cohere
from streamlit_extras.add_vertical_space import add_vertical_space

# Streamlit Page Configuration
st.set_page_config(page_title="JobMatch Pro - AI Resume Screener", page_icon="📄", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        .stButton>button { 
            width: 100%;
            border-radius: 8px;
            font-size: 18px;
            padding: 10px;
        }
        .stTextArea textarea {
            border-radius: 8px;
            font-size: 16px;
        }
        .stFileUploader label {
            font-size: 18px;
        }
        .sidebar-content {
            font-size: 16px;
            line-height: 1.6;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Cohere API Setup
co = cohere.Client("your-cohere-api")

# Sidebar Instructions
with st.sidebar:
    st.title("JobMatch Pro 🏆")
    st.write("🔹 AI-powered resume screening tool for HR professionals.")
    st.markdown("""
    ### How to Use:
    - 📂 **Upload** resumes in PDF format.
    - 📝 **Paste** the job description.
    - 🚀 **Click** 'Analyze Resumes' to rank them.
    - 📊 **Review** the ranked resumes with AI-powered scores.
    """, unsafe_allow_html=True)
    add_vertical_space(2)
    st.markdown("💡 *Tip:* Upload multiple resumes for better comparison!")

# Function to Extract Text from PDF
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text.strip()

# Function to Rank Resumes
def rank_resumes_rerank(resumes, job_description):
    texts = [res["text"] for res in resumes]
    response = co.rerank(query=job_description, documents=texts, top_n=len(texts), model="rerank-english-v2.0")
    
    ranked_resumes = []
    for result in response.results:
        ranked_resumes.append({"filename": resumes[result.index]["filename"], "score": result.relevance_score * 100})  # Convert to percentage
    
    return sorted(ranked_resumes, key=lambda x: x["score"], reverse=True)

# Function to Assign 5-Star Ratings 
def get_star_rating(score):
    yellow_half_star = '<span style="color:#FFD700;">&#x2BEA;</span>' 
    if score >= 95:
        return "⭐⭐⭐⭐⭐ 🏆 (Outstanding)"
    elif score >= 85:
        return f"⭐⭐⭐⭐{yellow_half_star} (Excellent)"
    elif score >= 75:
        return "⭐⭐⭐⭐ (Very Good)"
    elif score >= 65:
        return f"⭐⭐⭐{yellow_half_star} (Good)"
    elif score >= 55:
        return "⭐⭐⭐ (Average)"
    elif score >= 45:
        return f"⭐⭐{yellow_half_star} (Below Average)"
    elif score >= 35:
        return "⭐⭐ (Needs Improvement)"
    elif score >= 25:
        return f"⭐{yellow_half_star} (Weak Match)"
    elif score >= 15:
        return "⭐ (Poor Match)"
    else:
        return "❌ No Match (Not Suitable)"

# App Header
st.title("📄 JobMatch Pro - AI Resume Screener")
st.subheader("🔍 Find the Best Match for Your Job Posting")
add_vertical_space(1)

# File Upload & Job Description Input
uploaded_files = st.file_uploader("📌 Upload Resumes (PDF Only)", accept_multiple_files=True, type=["pdf"])
job_description = st.text_area("📝 Paste Job Description Here", height=200, placeholder="Enter the job description...")

add_vertical_space(1)

# Button to Analyze Resumes
if st.button("🚀 Analyze Resumes", use_container_width=True):
    if not uploaded_files or not job_description.strip():
        st.error("❌ Please upload resumes and provide a valid job description.")
    else:
        st.info("⏳ Processing resumes... This may take a few seconds.")
        
        # Extract text from PDFs
        resumes = [{"filename": file.name, "text": extract_text_from_pdf(file)} for file in uploaded_files]
        
        # Rank resumes using Rerank API
        ranked = rank_resumes_rerank(resumes, job_description)
        
        st.subheader("📊 Ranked Resumes")
        for i, res in enumerate(ranked, 1):
            stars = get_star_rating(res['score'])
            st.markdown(f"**{i}. {res['filename']}** — Score: `{res['score']:.2f}%` {stars}", unsafe_allow_html=True)
        
        st.success("✅ Analysis complete!")
