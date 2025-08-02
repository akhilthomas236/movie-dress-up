# Technical Architecture Document

## Malayalam Movie Dress Suggestions App - Technical Design

### 1. System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │────│  Python Backend │────│   Data Layer    │
│                 │    │                 │    │                 │
│ - Theme Pages   │    │ - Business Logic│    │ - Movie DB      │
│ - Search/Filter │    │ - Recommendation│    │ - Costume DB    │
│ - User Prefs    │    │ - Image Handler │    │ - User Prefs    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 2. File Structure

```
dress-up-tips/
├── app.py                 # Main Streamlit application
├── pages/                 # Theme-specific pages
│   ├── sports_monday.py
│   ├── wedding_tuesday.py
│   ├── formal_wednesday.py
│   ├── movie_thursday.py
│   └── retro_friday.py
├── data/                  # Data management
│   ├── movies.csv
│   ├── costumes.csv
│   └── data_loader.py
├── components/            # Reusable UI components
│   ├── look_card.py
│   ├── search_bar.py
│   └── filters.py
├── utils/                 # Utility functions
│   ├── image_handler.py
│   ├── recommendations.py
│   └── helpers.py
├── assets/               # Static assets
│   ├── images/
│   ├── styles.css
│   └── config.json
├── requirements.txt      # Dependencies
└── README.md            # Project documentation
```

### 3. Core Technologies

#### 3.1 Primary Stack
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **PIL/Pillow**: Image processing
- **SQLite**: Local database (development)
- **PostgreSQL**: Production database

#### 3.2 Additional Libraries
- **streamlit-option-menu**: Enhanced navigation
- **plotly**: Data visualization
- **requests**: API integrations
- **python-dotenv**: Environment configuration

### 4. Data Models

#### 4.1 Movie Model
```python
@dataclass
class Movie:
    id: str
    title: str
    year: int
    director: str
    genre: List[str]
    era: str
    poster_url: str
```

#### 4.2 Costume Model
```python
@dataclass
class Costume:
    id: str
    movie_id: str
    character_name: str
    actor_name: str
    description: str
    theme_day: str
    occasion_type: str
    difficulty_level: str
    colors: List[str]
    fabrics: List[str]
    accessories: List[str]
    styling_tips: List[str]
    image_urls: List[str]
```

### 5. Implementation Phases

#### Phase 1: Core Framework (Week 1)
- Basic Streamlit app structure
- Navigation between themed days
- Simple data loading and display

#### Phase 2: Content Integration (Week 2)
- Movie and costume database setup
- Image handling and optimization
- Theme-specific page implementation

#### Phase 3: Features (Week 3-4)
- Search and filter functionality
- User preferences and favorites
- Social sharing integration

---

## Next Steps for Implementation

1. **Environment Setup**: Create virtual environment and install dependencies
2. **Data Collection**: Gather movie stills and costume references
3. **UI Design**: Create mockups and component designs
4. **Development**: Follow phased implementation approach
5. **Testing**: User testing and feedback collection
