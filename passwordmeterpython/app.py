# import streamlit as st
# import re
# import random
# import string
# import time

# # Function to evaluate password strength
# def password_strength(password):
#     length = len(password)
#     score = 0

#     # Check password length
#     if length >= 8:
#         score += 1
#     if length >= 12:
#         score += 1

#     # Check for numbers
#     if re.search(r"\d", password):
#         score += 1

#     # Check for uppercase letters
#     if re.search(r"[A-Z]", password):
#         score += 1

#     # Check for special characters
#     if re.search(r"[\W_]", password):
#         score += 1

#     # Determine strength
#     if score == 5:
#         return "Strong", 100, "💪"  # Strong password emoji
#     elif score >= 3:
#         return "Medium", 60, "😐"  # Medium password emoji
#     else:
#         return "Weak", 30, "😟"  # Weak password emoji

# # Function to generate a strong password
# def generate_strong_password():
#     length = 12
#     all_characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(all_characters) for _ in range(length))
#     return password

# # Streamlit app UI setup
# st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

# # Add custom CSS for animated gradient on text
# st.markdown("""
#     <style>
#         @keyframes gradient {
#             0% { color: #ff7e5f; }
#             25% { color: #feb47b; }
#             50% { color: #6a11cb; }
#             75% { color: #2575fc; }
#             100% { color: #ff7e5f; }
#         }

#         .gradient-text {
#             font-size: 50px;
#             font-weight: bold;
#             background: linear-gradient(to right, #ff7e5f, #feb47b, #6a11cb, #2575fc);
#             background-clip: text;
#             color: transparent;
#             display: inline-block;
#             animation: gradient 4s ease infinite;
#         }

#         html, body {
#             height: 100%;
#             margin: 0;
#             padding: 0;
#             background: linear-gradient(to right, #daa1ca, );  /* Gradient from pink to orange */
#             color: white;
#         }

#         .stApp {
#             background: none;  /* No background override for Streamlit app container */
#             height: 100%;  /* Make sure it takes full height */
#         }

#         .password-strength-box {
#             padding: 20px;
#             border-radius: 8px;
#             text-align: center;
#             font-size: 20px;
#             color: white;
#             font-weight: bold;
#             margin-top: 10px;
#             animation: slideUp 1s ease-out;
#             opacity: 1;  /* Ensure it stays visible */
#         }

#         .strong { background-color: green; }
#         .medium { background-color: orange; }
#         .weak { background-color: red; }

#         .stButton>button {
#             font-size: 16px;
#             padding: 12px 30px;
#             background-color: #32a852;
#             color: white;
#             border-radius: 5px;
#             border: none;
#             transition: background-color 0.3s ease;
#             animation: fadeIn 4s ease-in-out;
#         }

#         .stButton>button:hover {
#             background-color: #28a745;
#         }

#         .stTextArea>div>div>textarea {
#             background-color: #f4f4f9;
#             font-size: 16px;
#             padding: 10px;
#             border-radius: 8px;
#             animation: fadeIn 5s ease-in-out;
#         }

#         .stCheckbox>div>label {
#             font-size: 14px;
#             color: #fff;
#         }

#         /* Animations */
#         @keyframes fadeIn {
#             0% { opacity: 0; }
#             100% { opacity: 1; }
#         }

#         @keyframes slideUp {
#             0% { opacity: 0; transform: translateY(20px); }
#             100% { opacity: 1; transform: translateY(0); }
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Add the animated gradient text title
# st.markdown('<h1 class="gradient-text">Password Strength Meter & Generator</h1>', unsafe_allow_html=True)

# # Password input from the user
# password = st.text_input("Enter your password:", type="password")

# # Add a gap and some emojis after the input box
# st.write("👀 Let's check how strong your password is!")  # Some emojis after input
# st.write("")  # Empty line for a gap

# # Password strength evaluation and progress bar
# if password:
#     strength, strength_score, emoji = password_strength(password)
    
#     # Show the strength status with emoji
#     st.write(f"Password strength: **{strength}** {emoji}")
    
#     # Progress bar
#     st.progress(strength_score)
    
#     # Color-coded password strength indicator
#     strength_class = "strong" if strength == "Strong" else "medium" if strength == "Medium" else "weak"
#     st.markdown(f'<div class="password-strength-box {strength_class}">{strength}</div>', unsafe_allow_html=True)

#     # Password tips
#     time.sleep(0.5)  # Small delay before showing tips
#     st.info("""**Tips for a Strong Password**:
#     - Include at least one lowercase letter, one uppercase letter, one number, and one special character.
#     - Passwords should be at least 12 characters long.
#     - Avoid using common words or predictable patterns.
#     """, icon="ℹ️")

# # Button to generate a new strong password
# if st.button("Generate a Strong Password"):
#     # Adding some animation delay before generating password
#     time.sleep(1)
    
#     new_password = generate_strong_password()
#     st.write(f"Generated Strong Password: **{new_password}**")
    
#     # Evaluate strength of generated password
#     generated_strength, generated_score, generated_emoji = password_strength(new_password)
#     st.write(f"Strength of Generated Password: **{generated_strength}** {generated_emoji}")
    
#     # Progress bar for generated password strength
#     st.progress(generated_score)
    
#     # Show strength with color-coded box
#     generated_strength_class = "strong" if generated_strength == "Strong" else "medium" if generated_strength == "Medium" else "weak"
#     st.markdown(f'<div class="password-strength-box {generated_strength_class}">{generated_strength}</div>', unsafe_allow_html=True)
    
#     # Display password in a text box for easy copying
#     st.text_area("Generated Password (You can copy it)", value=new_password, height=100)
#     st.success("Click to copy the generated password!")


###################################












       





import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating and Feedback
    if score == 4:
        feedback.append("✅ Strong Password!")
        strength = 'Strong'
        color = 'green'
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
        strength = 'Moderate'
        color = 'yellow'
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
        strength = 'Weak'
        color = 'red'
    
    # Calculate strength percentage (score out of 4)
    strength_percentage = (score / 4) * 100

    return strength, feedback, color, strength_percentage

def main():
    # Streamlit App Header
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

    # Add custom CSS to style the background color and header
    st.markdown("""
        <style>
            body {
                background-color: #f4f4f9;
                color: #333;
                font-family: 'Arial', sans-serif;
            }
            .stApp {
                background-color: #996A7B;
            }
            h1 {
                color: #004d40;
            }
            h3 {
                color: #00796b;
            }
            .stButton>button {
                background-color: #3F031F;
                color: white;
                border-radius: 8px;
                font-size: 16px;
            }
            .stButton>button:hover {
                background-color: #301f33;
                color: white;  /* Change text color to white on hover */
            }
        </style>
    """, unsafe_allow_html=True)
         

    # st.title("🔐 Password Strength Checker")
    st.markdown("<h1 style='color: #25083f;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
    st.markdown("### Check the strength of your password with this interactive tool!")
    
    # User Input for Password
    password = st.text_input("Enter your password", type="password", placeholder="Your password here...")
    
    if password:
        # Check password strength
        strength, feedback, color, strength_percentage = check_password_strength(password)

        # Display Strength Feedback
        st.markdown(f"### Password Strength: **{strength}**", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {color};'>{strength} Password!</h3>", unsafe_allow_html=True)
        
        # Display Detailed Feedback
        for message in feedback:
            st.markdown(message)
        
        # Show the Password Strength Slider (Percentage)
        st.markdown(f"### Strength: {strength_percentage}%")
        st.slider("Password Strength", min_value=0, max_value=100, value=int(strength_percentage), step=1)

        # Suggest Strong Password
        if strength == 'Weak':
            st.markdown("#### Suggestions to improve your password:")
            st.markdown("- Make your password at least 8 characters long.")
            st.markdown("- Use both uppercase and lowercase letters.")
            st.markdown("- Include numbers (e.g., 1-9).")
            st.markdown("- Add special characters like !@#$%^&*.")

        # Button to generate a strong password (Bonus Feature)
        if strength != 'Strong':
            if st.button("Generate a Strong Password"):
                strong_password = generate_strong_password()
                st.markdown(f"### Suggested Strong Password: **{strong_password}**")
                st.markdown("🔒 Copy this password to use!")

# Function to Generate Strong Password
def generate_strong_password():
    length = 12  # Strong passwords should be longer
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    main()

