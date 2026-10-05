from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CalculationContext:
    species_id: str
    breed_id: Optional[str]

    production_type: str
    production_level: float

    live_weight_kg: float
    age_days: Optional[int]

    days_gestation: Optional[int]
    days_lactation: Optional[int]

    milk_fat_pct: Optional[float] = None
    milk_protein_pct: Optional[float] = None

    target_daily_gain_g: Optional[float] = None

    reference_system: str = "inra2018"


if __name__ == "__main__":
    