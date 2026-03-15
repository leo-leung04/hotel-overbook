"""Download Hotel Booking Demand dataset from Kaggle."""

import shutil
from pathlib import Path

import kagglehub

PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"


def download_hotel_bookings():
    path = kagglehub.dataset_download("jessemostipak/hotel-booking-demand")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for f in Path(path).iterdir():
        shutil.copy(f, DATA_DIR / f.name)
    print(f"Done. Data saved to {DATA_DIR}")


if __name__ == "__main__":
    download_hotel_bookings()
