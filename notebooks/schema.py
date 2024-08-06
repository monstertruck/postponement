from pydantic import BaseModel
from typing import List, Optional


class NBAArena(BaseModel):
    """Pydantic model for NBA Arena."""
    
    lat: float
    lon: float
    name: str
    

class NBATeam(BaseModel):
    """Pydantic model for NBA team."""
    
    teamTricode: str
    

class WeatherSummary(BaseModel):
    """Pydantic model for summarizing weather for a day."""
    
    temp_high_f: float
    temp_low_f: float
    precipitation_mm: float
    wind_max_mph: float
    

class NBAGame(BaseModel):
    """Pydantic model for an NBA game."""

    game_id: str
    game_code: str
    home_team: NBATeam
    venue: NBAArena
    home_datetime: str
    

class NBAGameWeather(NBAGame):
    """Pydantic model for an NBA game with a weather summary for date/venue."""

    weather_summary: WeatherSummary
    

class RegularSeason(BaseModel):
    """Pydantic model for an NBA regular season."""
    
    games: List[NBAGame]