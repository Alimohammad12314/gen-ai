import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="GDGC GEN AI LEADERBOARD",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to style the app and logo positioning
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .leaderboard-header {
        background-color: #1a73e8;
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
    }
    .club-logo {
        width: 50px;  /* Adjust logo size */
        margin: 0 auto;
        position: absolute;
        top: -60px; /* Adjust to position logo above the title */
        left: 50%;
        transform: translateX(-50%);
    }
    .badge-count, .rank-number, .user-name {
        font-size: 1.1rem;
        color: #202124;
        font-weight: bold;
        text-align: center;
    }
    .arcade-status {
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.9rem;
        text-align: center;
        color: #202124;
    }
    .status-completed {
        background-color: #e6f4ea;
        color: #137333;
    }
    .status-not-completed {
        background-color: #fce8e6;
        color: #c5221f;
    }
    .header-container {
        display: grid;
        grid-template-columns: 10% 40% 25% 25%;
        background-color: #f0f0f0;
        padding: 0.5rem;
        border-radius: 8px;
        font-weight: bold;
        color: #1a73e8;
        text-align: center;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        margin-bottom: 0.5rem;
    }
    .row-container {
        display: grid;
        grid-template-columns: 10% 40% 25% 25%;
        background-color: white;
        padding: 0.8rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# Title and description with centered logo
logo_path = "gdsc.jpeg"  # Replace with your logo file path
st.markdown(f"""
    <div class="leaderboard-header">
        <h1 style="font-weight: bold; font-size: 2.5rem;">GenAI Study Jams 2024</h1>
        <p style="font-size: 1.2rem;">
            This is an institute-level rankings leaderboard for Google 
            <span style="font-weight: bold; font-size: 1.3rem;">GenAI Study Jams 2024</span> 
            of <span style="font-weight: bold; font-size: 1.3rem;">GDGC ZHCET</span>
        </p>
    </div>
""", unsafe_allow_html=True)

# Read and process the data with tiebreaker logic
def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    df = df[['User Name', '# of Skill Badges Completed', '# of Arcade Games Completed']]
    df = df.sort_values(
        by=['# of Skill Badges Completed', '# of Arcade Games Completed'],
        ascending=[False, False]
    ).reset_index(drop=True)
    df['Rank'] = df.index + 1
    df = df[['Rank', 'User Name', '# of Skill Badges Completed', '# of Arcade Games Completed']]
    return df

# Load the leaderboard data
csv_file_path = "Zakir Husain College of Engineering and Technology - Aligarh, India [08 Nov].csv"
df = load_and_process_data(csv_file_path)

# Column headers
st.markdown("""
<div class="header-container">
    <div>Rank</div>
    <div>Name</div>
    <div>Badges Earned</div>
    <div>Arcade Game Status</div>
</div>
""", unsafe_allow_html=True)

# Display each row in the leaderboard
for index, row in df.iterrows():
    arcade_status = "Completed" if row['# of Arcade Games Completed'] > 0 else "Not Completed"
    status_class = "status-completed" if row['# of Arcade Games Completed'] > 0 else "status-not-completed"

    st.markdown(f"""
        <div class="row-container">
            <div class="rank-number">#{row['Rank']}</div>
            <div class="user-name">{row['User Name']}</div>
            <div class="badge-count">{row['# of Skill Badges Completed']} Badges</div>
            <div class="arcade-status {status_class}">{arcade_status}</div>
        </div>
    """, unsafe_allow_html=True)
