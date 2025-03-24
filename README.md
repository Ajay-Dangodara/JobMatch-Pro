# JobMatch Pro - AI Resume Screener

## Overview
JobMatch Pro is an AI-powered resume screening tool designed to help recruiters and HR professionals efficiently evaluate and rank job applicants based on job descriptions. By leveraging **Cohere's AI technology**, the system provides intelligent resume analysis, scoring, and ranking, streamlining the hiring process and saving valuable time for recruitment teams.

## Features
- 📂 **Resume Upload**: Supports resumes in **PDF format**.
- 📝 **Automated Resume Parsing**: Extracts key details such as skills, experience, and education.
- 📊 **AI-Driven Ranking**: Uses Cohere's **Rerank API** to compare resumes against job descriptions.
- ⭐ **5-Star Rating System**: Assigns intuitive ratings based on relevance.
- 🚀 **User-Friendly Interface**: Built with **Streamlit**, featuring a sleek and responsive design.
- 📈 **Bulk Resume Analysis**: Allows uploading multiple resumes at once for better comparison.
- 🔍 **Insights & Summaries**: Generates detailed reports on candidate suitability.

## Tech Stack
- **Programming Language:** Python
- **Libraries & Frameworks:**
  - Streamlit (UI framework)
  - pdfplumber (PDF text extraction)
  - Cohere API (AI-powered resume ranking)
- **AI Model:** Cohere Rerank for evaluating resume-job description relevance
- **Frontend:** Streamlit with custom CSS for enhanced UI

## Installation
Follow these steps to install and run the application:

1. **Clone the repository:**
   ```bash
   https://github.com/Ajay-Dangodara/JobMatch-Pro.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage
1. **Upload** resumes in **PDF format** using the file uploader.
2. **Paste** the **job description** in the provided text area.
3. Click **'Analyze Resumes'** to initiate AI-powered screening.
4. View **ranked resumes with AI-generated scores and 5-star ratings**.
5. Compare **top candidates** and make data-driven hiring decisions.

## How It Works
- **Text Extraction:** Extracts resume text using `pdfplumber`.
- **AI Ranking:** Uses **Cohere Rerank** API to match resumes to job descriptions.
- **Scoring:** Assigns relevance scores and star ratings.
- **Results Display:** Lists resumes in order of relevance, providing an intuitive overview of candidate suitability.

## Contribution
We welcome contributions! To contribute:
1. **Fork the repository**.
2. **Create a new branch** for your feature or fix.
3. **Make your changes** and test them locally.
4. **Submit a pull request** with a clear description of your updates.
