import streamlit as st
import scraper as sc
import ai as ai

# Streamlit app configuration
st.title("Facebook Post Generator")
st.sidebar.header("Configuration")

# Input section
url_options = {
    "John Obidi": "https://web.facebook.com/JohnObidiOfficial",
    "Emeka Nobis": "https://web.facebook.com/profile.php?id=61559856771824",
    "Charles Awuzie": "https://web.facebook.com/reformed.charles.awuzie",
    "Strive Masiyiwa": "https://web.facebook.com/strivemasiyiwa",
    "Chinaza Favour": "https://web.facebook.com/thechinazafavour",
    "Chioma Ifeanyi-Eze": "https://web.facebook.com/chioma.ifeanyieze",
    "Joy Edjeren": "https://web.facebook.com/JoyEdjerenOfficialpage"
}

selected_label = st.selectbox("Choose a style for the post:", list(url_options.keys()) + ["Custom URL"])
custom_url = st.text_input("Enter a custom URL (if 'Custom URL' selected):") if selected_label == "Custom URL" else None
url = custom_url if custom_url else url_options[selected_label]

length_option = st.selectbox("Choose the length of the post:", ["short-form", "medium-length", "long-form"])
topic = st.text_input("Enter the topic or idea for the post:")

# Generate button
if st.button("Generate"):
    if topic and url:
        st.write("Fetching posts and generating content...")
        posts = sc.scrape_facebook_posts(url)
        
        # Select top-performing post for generation
        top_post = max(posts, key=lambda x: (x['shares'], x['comments'], x['likes']))
        
        # Convert top post to bullet points
        bullet_summary = ai.blog_post_to_bullet_points(top_post['content'])
        
        # Generate Facebook post based on bullet points and selected length
        post = ai.generate_facebook_post(bullet_summary, length_option)
        
        # Display the generated post
        st.subheader("Generated Facebook Post:")
        st.write(post)
        
        # Add a copy button
        st.button("Copy to Clipboard")
    else:
        st.error("Please enter a topic and ensure the URL is valid.")

