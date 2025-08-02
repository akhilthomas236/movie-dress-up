import pandas as pd
import streamlit as st
from typing import Dict, List, Optional
import os

def clear_cache():
    """Clear all cached data."""
    st.cache_data.clear()

@st.cache_data
def load_movies() -> pd.DataFrame:
    """Load movies data from CSV file."""
    try:
        data_path = os.path.join(os.path.dirname(__file__), 'movies.csv')
        df = pd.read_csv(data_path)
        return df
    except Exception as e:
        st.error(f"Error loading movies data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_costumes() -> pd.DataFrame:
    """Load costumes data from CSV file."""
    try:
        data_path = os.path.join(os.path.dirname(__file__), 'costumes.csv')
        df = pd.read_csv(data_path)
        return df
    except Exception as e:
        st.error(f"Error loading costumes data: {e}")
        return pd.DataFrame()

def get_costumes_by_theme(theme_day: str) -> pd.DataFrame:
    """Get costumes filtered by theme day."""
    df = load_costumes()
    if df.empty:
        return df
    
    filtered_df = df[df['theme_day'] == theme_day].copy()
    
    # Add missing columns that the app expects
    if 'title' not in filtered_df.columns:
        filtered_df['title'] = 'Movie Title'  # You might want to add actual movie titles
    if 'year' not in filtered_df.columns:
        filtered_df['year'] = '2023'  # You might want to add actual years
    
    return filtered_df

def get_movie_by_id(movie_id: str) -> Optional[Dict]:
    """Get movie details by ID."""
    movies_df = load_movies()
    movie = movies_df[movies_df['id'] == movie_id]
    
    if not movie.empty:
        return movie.iloc[0].to_dict()
    return None

def search_costumes(query: str, theme_day: Optional[str] = None) -> pd.DataFrame:
    """Search costumes by movie title, actor name, or character name."""
    df = load_costumes()
    if df.empty:
        return df
    
    # Convert query to lowercase for case-insensitive search
    query = query.lower()
    
    # Search in multiple columns
    search_columns = ['character_name', 'actor_name', 'scene_description', 'movie_id']
    mask = df[search_columns].astype(str).apply(
        lambda x: x.str.lower().str.contains(query, na=False)
    ).any(axis=1)
    
    results = df[mask]
    
    # Filter by theme if specified
    if theme_day:
        results = results[results['theme_day'] == theme_day]
    
    return results

def get_theme_stats() -> Dict[str, int]:
    """Get statistics for each theme day."""
    df = load_costumes()
    if df.empty:
        return {}
    
    stats = df['theme_day'].value_counts().to_dict()
    return stats

def get_costume_by_id(costume_id):
    """Get a specific costume by ID."""
    df = load_costumes()
    if df.empty:
        return None
    
    costume = df[df['id'] == costume_id]
    return costume.iloc[0] if not costume.empty else None