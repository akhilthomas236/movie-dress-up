import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from data.data_loader import get_costumes_by_theme, get_theme_stats, search_costumes
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="Indian Movie Dress Suggestions",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .theme-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .theme-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .look-card {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .look-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .grid-card {
        background: white;
        border-radius: 10px;
        padding: 0.8rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
    }
    
    .grid-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    }
    
    .thumbnail-container {
        position: relative;
        overflow: hidden;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    .thumbnail-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        transition: transform 0.3s ease;
    }
    
    .thumbnail-image:hover {
        transform: scale(1.05);
    }
    
    .image-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(transparent, rgba(0,0,0,0.7));
        color: white;
        padding: 1rem;
        transform: translateY(100%);
        transition: transform 0.3s ease;
    }
    
    .thumbnail-container:hover .image-overlay {
        transform: translateY(0);
    }
    
    .difficulty-easy { color: #28a745; }
    .difficulty-medium { color: #ffc107; }
    .difficulty-hard { color: #dc3545; }
    
    .stats-container {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .quick-actions {
        display: flex;
        justify-content: space-around;
        margin-top: 0.5rem;
    }
    
    .costume-thumbnail {
        width: 100%;
        height: 150px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .costume-thumbnail:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .thumbnail-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.3);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
        border-radius: 8px;
    }
    
    .thumbnail-container:hover .thumbnail-overlay {
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎬 Indian Movie Dress Suggestions</h1>
        <p>Discover your perfect look inspired by iconic Indian cinema across all languages</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get current day to suggest default theme
    current_day = datetime.now().strftime("%A")
    day_theme_mapping = {
        "Monday": "Sports Monday",
        "Tuesday": "Wedding Tuesday", 
        "Wednesday": "Formal Wednesday",
        "Thursday": "Movie Thursday",
        "Friday": "Retro Friday"
    }
    
    suggested_theme = day_theme_mapping.get(current_day, "Sports Monday")
    
    # Show daily suggestion
    st.info(f"🌟 Today is {current_day}! We suggest exploring **{suggested_theme}** looks.")
    
    # Theme navigation
    themes = ["Sports Monday", "Wedding Tuesday", "Formal Wednesday", "Movie Thursday", "Retro Friday"]
    
    selected_theme = option_menu(
        menu_title="Choose Your Theme",
        options=themes,
        icons=["⚽", "💒", "👔", "🎭", "🕰️"],
        menu_icon="🎨",
        default_index=themes.index(suggested_theme),
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#667eea", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#667eea"},
        }
    )
    
    # Sidebar with stats and search
    with st.sidebar:
        st.header("📊 Theme Statistics")
        stats = get_theme_stats()
        
        for theme, count in stats.items():
            emoji = {"Sports Monday": "⚽", "Wedding Tuesday": "💒", "Formal Wednesday": "👔", 
                    "Movie Thursday": "🎭", "Retro Friday": "🕰️"}[theme]
            st.metric(f"{emoji} {theme}", f"{count} looks")
        
        st.header("🔍 Search Looks")
        search_query = st.text_input("Search by movie, actor, or character:")
        
        if search_query:
            search_results = search_costumes(search_query, selected_theme)
            st.write(f"Found {len(search_results)} results")
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.header(f"✨ {selected_theme} Looks")
    
    with col2:
        view_mode = st.selectbox("View Mode", ["List View", "Grid View"], key="view_mode")
    
    # Load and display theme-specific looks
    theme_looks = get_costumes_by_theme(selected_theme)
    
    if theme_looks.empty:
        st.warning(f"No looks available for {selected_theme} yet. Stay tuned!")
        return
    
    # Display theme description
    theme_descriptions = {
        "Sports Monday": "Get inspired by athletic and casual wear from Indian sports movies across Malayalam, Hindi, Tamil, Telugu, and other regional cinemas. Perfect for gym days, outdoor activities, and comfortable everyday wear.",
        "Wedding Tuesday": "Discover elegant traditional and modern wedding attire from beautiful Indian wedding scenes. From guest looks to bridal inspiration across different regional cultures and traditions.",
        "Formal Wednesday": "Professional and sophisticated looks from Indian movies spanning all languages. Perfect for office wear, meetings, and formal occasions with diverse cultural influences.",
        "Movie Thursday": "Glamorous and cinematic looks from various Indian movie genres across Hindi, Tamil, Telugu, Malayalam, and other regional films. Stand out with these eye-catching styles.",
        "Retro Friday": "Vintage and classic styles from different eras of Indian cinema. Embrace the timeless fashion from Bollywood classics to regional cinema gems of yesteryears."
    }
    
    st.markdown(f"*{theme_descriptions[selected_theme]}*")
    
    # Display looks based on view mode
    if view_mode == "Grid View":
        display_grid_view(theme_looks)
    else:
        display_list_view(theme_looks)

def display_look_card(look):
    """Display a single look card with thumbnail."""
    with st.container():
        # Thumbnail with overlay effect
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Small thumbnail
            st.markdown(f"""
            <div class="thumbnail-container">
                <img src="{look['image_url']}" class="thumbnail-image" alt="{look['character_name']} look">
                <div class="image-overlay">
                    <small>{look['character_name']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Look details
            st.markdown(f"""
            <div class="look-card">
                <h4>{look['title']} ({look['year']})</h4>
                <p><strong>Character:</strong> {look['character_name']} ({look['actor_name']})</p>
                <p><strong>Scene:</strong> {look['scene_description']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Additional details in expandable section
        col1, col2, col3 = st.columns(3)
        
        with col1:
            difficulty_class = f"difficulty-{look['difficulty_level'].lower()}"
            st.markdown(f"**Difficulty:** <span class='{difficulty_class}'>{look['difficulty_level']}</span>", 
                       unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**Occasion:** {look['occasion_type']}")
        
        with col3:
            st.markdown(f"**Colors:** {look['colors']}")
        
        # Expandable details
        with st.expander("👗 Styling Details"):
            st.markdown(f"**Fabrics:** {look['fabrics']}")
            st.markdown(f"**Accessories:** {look['accessories']}")
            st.markdown(f"**Styling Tips:** {look['styling_tips']}")
        
        # Action buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button(f"� View Full", key=f"view_{look['id']}"):
                # Show full image in a modal-like expander
                with st.expander("Full Size Image", expanded=True):
                    st.image(look['image_url'], caption=f"{look['character_name']} - {look['title']}", use_container_width=True)
        
        with col2:
            if st.button(f"💖 Save", key=f"save_{look['id']}"):
                st.success("Look saved to favorites!")
        
        with col3:
            if st.button(f"📱 Share", key=f"share_{look['id']}"):
                st.info("Share functionality coming soon!")
        
        with col4:
            if st.button(f"⭐ Rate", key=f"rate_{look['id']}"):
                st.info("Rating feature coming soon!")
        
        st.markdown("---")

def display_grid_view(theme_looks):
    """Display looks in a grid view with thumbnails."""
    cols = st.columns(3)
    
    for idx, (_, look) in enumerate(theme_looks.iterrows()):
        col = cols[idx % 3]
        
        with col:
            # Compact grid card
            st.markdown(f"""
            <div class="grid-card">
                <div class="thumbnail-container">
                    <img src="{look['image_url']}" class="thumbnail-image" alt="{look['character_name']} look" style="height: 150px;">
                    <div class="image-overlay">
                        <small>{look['character_name']}</small>
                    </div>
                </div>
                <h5>{look['character_name']}</h5>
                <p><small>{look['actor_name']}</small></p>
                <p><small>{look['scene_description'][:50]}...</small></p>
                
                <!-- Quick actions -->
                <div class="quick-actions">
                    <div>
                        <st.button f"👁️" key=f"quick_view_{look['id']}" help="Quick View">
                    </div>
                    <div>
                        <st.button f"💖" key=f"quick_save_{look['id']}" help="Save">
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Quick details
            difficulty_class = f"difficulty-{look['difficulty_level'].lower()}"
            st.markdown(f"<center><span class='{difficulty_class}'>{look['difficulty_level']}</span></center>", 
                       unsafe_allow_html=True)
            
            # Show details if toggled
            if st.session_state.get(f"show_details_{look['id']}", False):
                with st.expander("Details", expanded=True):
                    st.markdown(f"**Fabrics:** {look['fabrics']}")
                    st.markdown(f"**Colors:** {look['colors']}")
                    st.markdown(f"**Styling Tips:** {look['styling_tips']}")
                    if st.button("Close", key=f"close_{look['id']}"):
                        st.session_state[f"show_details_{look['id']}"] = False
                        st.rerun()

def display_list_view(theme_looks):
    """Display looks in a detailed list view."""
    for idx, (_, look) in enumerate(theme_looks.iterrows()):
        display_look_card(look)

# Footer
def show_footer():
    st.markdown("""
    ---
    <div style='text-align: center; color: #666; padding: 2rem 0;'>
        <p>Made with ❤️ for Indian Cinema Fashion Enthusiasts</p>
        <p>This app celebrates the rich visual heritage of Indian movies across all languages while providing practical fashion inspiration.</p>
        <p><em>All movie references are used for educational and cultural appreciation purposes.</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    show_footer()