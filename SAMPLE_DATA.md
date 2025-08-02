# Sample Data Structure

## Movies Database Sample

```csv
id,title,year,director,genre,era,poster_url,description
MOV001,Bangalore Days,2014,Anjali Menon,"Comedy,Romance",2010s,/assets/posters/bangalore_days.jpg,"Modern youth romance with contemporary fashion"
MOV002,Premam,2015,Alphonse Puthren,"Romance,Comedy",2010s,/assets/posters/premam.jpg,"Coming of age story with diverse styling across eras"
MOV003,Kumbakonam Gopals,1998,Hariharan,Comedy,1990s,/assets/posters/kumbakonam_gopals.jpg,"Classic comedy with vintage 90s fashion"
MOV004,Kireedam,1989,Sibi Malayil,Drama,1980s,/assets/posters/kireedam.jpg,"Iconic 80s styling and traditional Kerala fashion"
MOV005,Helen,2019,Mathukutty Xavier,Thriller,2010s,/assets/posters/helen.jpg,"Contemporary urban fashion and restaurant styling"
```

## Costumes Database Sample

```csv
id,movie_id,character_name,actor_name,scene_description,theme_day,occasion_type,difficulty_level,colors,fabrics,accessories,styling_tips,image_url
COS001,MOV001,Divya,Nazriya Nazim,"Wedding guest look with modern saree",Wedding Tuesday,Wedding Guest,Medium,"Pink,Gold","Silk,Chiffon","Gold jewelry,Clutch","Choose light colors for day weddings",/assets/costumes/bangalore_days_wedding.jpg
COS002,MOV002,Malar,Sai Pallavi,"College student casual look",Sports Monday,Casual,Easy,"Blue,White","Cotton,Denim","Backpack,Sneakers","Comfort over style for active days",/assets/costumes/premam_college.jpg
COS003,MOV004,Sethu,Mohanlal,"Police uniform formal look",Formal Wednesday,Professional,Hard,"Khaki,Brown","Cotton,Polyester","Belt,Badge,Cap","Crisp lines and proper fit essential",/assets/costumes/kireedam_uniform.jpg
COS004,MOV005,Helen,Anna Ben,"Restaurant server uniform",Formal Wednesday,Work Uniform,Medium,"Black,White","Cotton blend","Apron,Non-slip shoes","Professional and practical styling",/assets/costumes/helen_uniform.jpg
COS005,MOV003,Gopalan,Jayaram,"90s casual comedy look",Retro Friday,Casual,Easy,"Bright colors","Cotton","Vintage accessories","Bold patterns and colors were trendy",/assets/costumes/kumbakonam_retro.jpg
```

## Styling Tips Database

```csv
costume_id,tip_category,tip_text,priority
COS001,Color Matching,"Pink and gold complement warm skin tones perfectly",High
COS001,Occasion,"Perfect for morning wedding ceremonies",Medium
COS001,Budget,"Can recreate with budget sarees from local stores",Low
COS002,Comfort,"Choose breathable fabrics for all-day wear",High
COS002,Styling,"Roll up sleeves for casual college vibe",Medium
COS003,Fit,"Uniform should be well-tailored for professional look",High
COS003,Grooming,"Clean-shaven look essential for this character",Medium
```

## User Preferences Schema

```json
{
  "user_id": "USER001",
  "preferences": {
    "age_group": "20-30",
    "body_type": "medium",
    "style_preference": ["traditional", "modern"],
    "favorite_actors": ["Nazriya Nazim", "Sai Pallavi"],
    "favorite_movies": ["MOV001", "MOV002"],
    "occasion_frequency": {
      "casual": "daily",
      "formal": "weekly", 
      "wedding": "monthly",
      "party": "occasionally"
    },
    "budget_range": "medium",
    "complexity_preference": "easy_to_medium"
  },
  "saved_looks": ["COS001", "COS002", "COS005"],
  "tried_looks": ["COS002"],
  "ratings": {
    "COS001": 5,
    "COS002": 4,
    "COS005": 5
  }
}
```

## Sample Movie-Look Mappings by Theme

### Sports Monday
- **Sudani from Nigeria**: Soccer jerseys, athletic shorts, sneakers
- **Captain**: Cricket whites, sports casuals, team jackets
- **Finals**: Basketball jerseys, gym wear, college athletics
- **Aadu**: Adventure wear, outdoor jackets, hiking boots

### Wedding Tuesday  
- **Bangalore Days**: Modern wedding guest sarees, contemporary lehengas
- **Premam**: Traditional Kerala wedding attire, kasavu sarees
- **Queen**: Bridal fashion, heavy silk sarees, gold jewelry
- **Jacobinte Swargarajyam**: Family wedding formals, shirt-mundu combinations

### Formal Wednesday
- **Virus**: Medical scrubs, doctor coats, professional attire
- **The Great Father**: Business suits, corporate wear, police uniforms
- **Take Off**: Diplomatic wear, formal shirts, blazers
- **Lucifer**: Political formals, power suits, traditional politician wear

### Movie Thursday
- **Ustad Hotel**: Chef uniforms, artistic casuals, bohemian styles
- **Charlie**: Quirky artistic wear, backpacker style, creative looks
- **Helen**: Restaurant uniforms, urban contemporary, night-life looks
- **Kumbakonam Gopals**: Comedy character styling, exaggerated looks

### Retro Friday
- **Kireedam**: 1980s police uniforms, vintage casual wear
- **His Highness Abdullah**: Royal vintage looks, traditional formal wear
- **Manichithrathazhu**: 1990s traditional-modern mix, psychiatric drama styling
- **Spadikam**: Rugged vintage masculinity, working-class retro looks

## Color Palettes by Era

### 1980s Malayalam Cinema
- **Primary**: Bold reds, deep blues, bright yellows
- **Secondary**: Orange, magenta, forest green
- **Neutrals**: Cream, beige, dark brown

### 1990s Malayalam Cinema  
- **Primary**: Pastels, light blues, soft pinks
- **Secondary**: Mint green, lavender, peach
- **Neutrals**: Off-white, light gray, tan

### 2000s Malayalam Cinema
- **Primary**: Earth tones, maroon, navy blue
- **Secondary**: Olive green, burgundy, rust
- **Neutrals**: Khaki, chocolate brown, ivory

### 2010s+ Malayalam Cinema
- **Primary**: Contemporary palettes, minimalist colors
- **Secondary**: Coral, teal, dusty rose
- **Neutrals**: Pure white, charcoal, soft gray
