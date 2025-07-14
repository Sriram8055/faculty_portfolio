import streamlit as st
import smtplib
from email.message import EmailMessage

# ----- PAGE CONFIG -----
st.set_page_config(page_title="M. Saranya | Faculty Portfolio", layout="wide")

# ----- CUSTOM CSS -----
def inject_custom_css():
    st.markdown("""
    <style>
        body { background-color: #f7f9fc; }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        h1, h2, h3 { color: #1f3b4d; }
        a { color: #007bff; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: gray;
            margin-top: 2em;
        }
        .stTextInput > div > input,
        .stTextArea > div > textarea {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 0.5em;
        }
        .stButton > button {
            background-color: #007bff;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
        }
        .stButton > button:hover {
            background-color: #0056b3;
        }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# ----- HERO SECTION -----
st.title("👩‍🏫 M. Saranya")
st.subheader("Assistant Professor | Department of AI & DS")
st.write("📍 National Engineering College, Kovilpatti")
st.write("📧 saranyaai@nec.edu.in | 📞 +91 6383260220")
st.markdown("<br>", unsafe_allow_html=True)

# ----- ABOUT -----
st.markdown("## 👩‍🎓 About Me")
st.info("""
Assistant Professor in AI & Data Science with specialization in Computer Science. Experienced in teaching and actively involved in research on deep learning, image processing, and machine learning. Passionate about technology, innovation, and continuous learning.
""")
st.markdown("<br>", unsafe_allow_html=True)

# ----- EDUCATIONAL QUALIFICATION -----
st.markdown("## 🎓 Educational Qualification")
st.markdown("""
- **M.E. in Computer Science and Engineering**  
  National Engineering College, 2024 – *CGPA: 8.72*

- **B.E. in Computer Science and Engineering**  
  PSRR College of Engineering, 2022 – *CGPA: 8.48*
""")
st.markdown("<br>", unsafe_allow_html=True)

# ----- PROFESSIONAL DETAILS -----
st.markdown("## 💼 Professional Experience")
st.markdown("""
- **Designation**: Assistant Professor  
  **Institution**: National Engineering College  
  **Period**: 03.06.2024 – Present  
  **Nature of Duties**: Teaching
""")
st.markdown("<br>", unsafe_allow_html=True)

# ----- CONFERENCE PRESENTATIONS -----
st.markdown("## 📚 Conference Presentations")
st.markdown("""
1. **Image Captioning based on Encoder Decoder Architecture**  
   *International Conference on Smart Systems (INCOS '24), May 2024*

2. **Image to Text Conversion using Deep Learning Algorithms: Survey**  
   *International Conference on Advanced Computing and Communication Systems (ICACCS '24)*
""")
st.markdown("<br>", unsafe_allow_html=True)

# ----- WORKSHOPS ATTENDED -----
st.markdown("## 🛠 Workshops Attended")
st.markdown("""
1. **IPR, Technology Transfer & Entrepreneurship**  
   Centre of Excellence in AI, NIT Tiruchirappalli  
   *Duration: 30-01-2023 to 03-02-2023*

2. **Stochastic Approximation Algorithm**  
   National Engineering College  
   *Duration: 27-04-2023 to 28-04-2023*

3. **Moodle LMS – SALIS 2023 Conference**  
   National Engineering College  
   *Date: 12-09-2023*
""")
st.markdown("<br>", unsafe_allow_html=True)

# ----- ONLINE COURSES -----
st.markdown("## 🌐 Online Courses")
st.markdown("""
- **Industrial 4.0 and Introduction to Internet of Things**  
  *NPTEL – 12 Weeks*  
  *Achievement: Elite + Silver*
""")
st.markdown("<br>", unsafe_allow_html=True)

# ----- INTERNSHIP -----
st.markdown("## 💡 Internship")
st.markdown("""
**Organization**: Kadit Innovations, Kadayanallur  
**Duration**: December 2023 – February 2024  
**Platform**: Machine Learning  
**Outcome**: Developed a weather prediction system using ML techniques.
""")
st.markdown("<br>", unsafe_allow_html=True)

# ----- PERSONAL DETAILS -----
st.markdown("## 🧾 Personal Details")
st.markdown("""
- **Name**: M. Saranya  
- **Date of Birth**: 17.04.2001  
- **Age**: 23  
- **Sex / Marital Status**: Female / Unmarried  
- **Citizenship**: Indian
""")
st.markdown("<br>", unsafe_allow_html=True)

# ----- CONTACT FORM -----
st.markdown("## 📬 Contact Me")

def send_email(name, sender_email, message):
    receiver_email = st.secrets["email"]["username"]
    email_password = st.secrets["email"]["password"]

    email_message = EmailMessage()
    email_message["Subject"] = f"Faculty Portfolio Contact - {name}"
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message.set_content(f"""
You received a new message:

Name: {name}
Email: {sender_email}

Message:
{message}
    """)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(receiver_email, email_password)
            smtp.send_message(email_message)
        return True
    except Exception as e:
        print("Email send error:", e)
        return False


with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name")
    with col2:
        email = st.text_input("Your Email")

    message = st.text_area("Message")

    submitted = st.form_submit_button("Send")
    if submitted:
        if name and email and message:
            if send_email(name, email, message):
                st.success("✅ Message sent! Thank you for reaching out.")
            else:
                st.error("❌ Failed to send message. Try again later.")
        else:
            st.warning("⚠️ Please fill in all fields.")

# ----- FOOTER -----
st.markdown("---")
st.markdown("<div class='footer'>© 2025 M. Saranya | Built with ❤️ using Streamlit</div>", unsafe_allow_html=True)
