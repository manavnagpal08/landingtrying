import streamlit as st

st.set_page_config(page_title="AI Website", layout="wide")

# Load the custom CSS (your Tailwind-like design system)
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- HERO SECTION ----
st.markdown("""
<div class="grain" style="padding:120px 20px; text-align:center;">
    <h1 class="text-gradient" style="font-size:60px; font-weight:800;">
        Build Faster With AI
    </h1>
    <p style="max-width:650px; margin:20px auto; font-size:20px; color:hsl(215 20% 65%);">
        Next-gen AI platform that automates workflows with stunning precision.
    </p>

    <div style="margin-top:40px;">
        <a class="cta-btn glow-effect hover-lift" href="#" style="
            padding:16px 36px;
            border-radius:12px;
            background:var(--gradient-primary);
            color:black;
            font-weight:600;
            font-size:18px;
            box-shadow:var(--shadow-glow);
            transition:var(--transition-bounce);
            display:inline-block;
        ">Get Started</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- FEATURES SECTION ----
st.markdown("""
<div style="padding:80px 20px;">
    <h2 style="text-align:center; font-size:40px; margin-bottom:40px;">Features</h2>

    <div class="feature-grid" style="
        display:grid;
        grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));
        gap:30px;
        max-width:1100px;
        margin:auto;
    ">
        <div class="feature-card hover-lift glow-effect" style="
            background:var(--gradient-card);
            padding:30px;
            border-radius:20px;
            box-shadow:var(--shadow-card);
        ">
            <h3>⚡ Ultra Fast</h3>
            <p>Optimized AI execution with near-zero latency.</p>
        </div>

        <div class="feature-card hover-lift glow-effect" style="
            background:var(--gradient-card);
            padding:30px;
            border-radius:20px;
        ">
            <h3>🧠 Smart Automation</h3>
            <p>Automate tasks with intelligent workflows.</p>
        </div>

        <div class="feature-card hover-lift glow-effect" style="
            background:var(--gradient-card);
            padding:30px;
            border-radius:20px;
        ">
            <h3>🔒 Secure</h3>
            <p>Bank-level encryption with advanced access control.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- HOW IT WORKS SECTION ----
st.markdown("""
<div style="padding:100px 20px;">
    <h2 style="text-align:center; font-size:40px; margin-bottom:40px;">How It Works</h2>
    
    <div style="max-width:900px; margin:auto;">
        <div class="hover-lift" style="padding:20px; border-left:3px solid hsl(200 100% 50%); margin-bottom:30px;">
            <h3>1. Connect Your Data</h3>
            <p>Link your workflows, documents, and apps.</p>
        </div>

        <div class="hover-lift" style="padding:20px; border-left:3px solid hsl(200 100% 50%); margin-bottom:30px;">
            <h3>2. AI Understands Context</h3>
            <p>Your tasks are analyzed using advanced AI models.</p>
        </div>

        <div class="hover-lift" style="padding:20px; border-left:3px solid hsl(200 100% 50%);">
            <h3>3. Automation Runs Instantly</h3>
            <p>Get intelligent, real-time output with zero effort.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- CTA SECTION ----
st.markdown("""
<div class="animate-float grain" style="
    padding:100px 20px;
    text-align:center;
    background:var(--gradient-primary);
    border-radius:30px;
    max-width:1200px;
    margin:60px auto;
    color:black;
">
    <h2 style="font-size:40px; font-weight:700;">Ready to unlock AI power?</h2>
    <p style="font-size:20px; margin-top:10px;">
        Start building, automating, and deploying — instantly.
    </p>

    <a class="cta-btn hover-lift" href="#" style="
        margin-top:30px;
        display:inline-block;
        padding:16px 40px;
        background:black;
        color:white;
        border-radius:12px;
        font-weight:600;
        font-size:18px;
        transition:var(--transition-bounce);
    ">Start Free</a>
</div>
""", unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("""
<div style="padding:40px; text-align:center; opacity:0.5;">
    © 2025 Your Website — All rights reserved.
</div>
""", unsafe_allow_html=True)
