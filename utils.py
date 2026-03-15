import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def load_hotel_data(csv_name="hotel_bookings.csv"):
    """
    Load the Hotel Booking Demand dataset. https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data
    """
    path = DATA_DIR / csv_name
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    return pd.read_csv(path)


def get_data_path():
    """Return the data directory path."""
    return DATA_DIR
