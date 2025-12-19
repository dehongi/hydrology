# Hydrology Library

A comprehensive Python library for hydrological and advanced hydrological calculations, covering foundational and advanced university-level topics. This library aims to modernize the laborious spreadsheet calculations common in traditional hydrology courses.

## Features

- **Precipitation**: Areal averages (Thiessen, Isohyetal), IDF relationships.
- **Evapotranspiration**: Penman-Monteith, Thornthwaite, Priestley-Taylor.
- **Infiltration**: Horton, Green-Ampt, SCS Curve Number.
- **Runoff & Hydrographs**: Rational method, Unit Hydrographs, SCS Unit Hydrograph.
- **Flood Routing**: Muskingum method, Level pool routing.
- **Groundwater**: Darcy flow, Theis and Thiem solutions.
- **Statistics**: Frequency analysis (Gumbel, Log-Pearson Type 3).

## Detailed Module Overview

### 🌧️ Precipitation (`hydrology/precipitation.py`)
- **Areal Averages**: Methods for calculating mean rainfall over a catchment.
  - `arithmetic_mean`: Simple average of station data.
  - `thiessen_polygons`: Area-weighted average based on station proximity.
  - `isohyetal_method`: Contour-weighted average using points of equal rainfall.
- **IDF Relationships**: Intensity-Duration-Frequency curves using the Sherman equation.

### 🍃 Evapotranspiration (`hydrology/evapotranspiration.py`)
- **Thornthwaite**: Temperature-based PET estimation, ideal for monthly water balance.
- **Priestley-Taylor**: Radiation-based PET estimation for moist surfaces.
- **Penman-Monteith (FAO-56)**: The standard aerodynamic-plus-energy-balance method for reference ET.

### 💧 Infiltration (`hydrology/infiltration.py`)
- **Horton's Equation**: Empirical model for infiltration capacity decay over time.
- **Green-Ampt Method**: Physics-based model considering soil suction and hydraulic conductivity.
- **SCS Curve Number**: Watershed-scale abstraction and runoff depth estimation.

### 🌊 Runoff & Hydrographs (`hydrology/runoff.py`)
- **Rational Method**: Peak discharge estimation for small urban catchments.
- **Unit Hydrograph (UH)**: Derivation and convolution for direct runoff hydrographs.
- **SCS Triangular UH**: Synthetic unit hydrograph for ungauged watersheds.

### 🏘️ Flood Routing (`hydrology/routing.py`)
- **Muskingum Method**: Standard channel routing considering wedge and prism storage.
- **Level Pool Routing**: Reservoir routing using the storage-indication method.

### 🕳️ Groundwater (`hydrology/groundwater.py`)
- **Darcy's Law**: Fundamental equation for flow through porous media.
- **Steady State (Thiem)**: Well hydraulics for confined/unconfined steady flow.
- **Unsteady State (Theis)**: Transient drawdown analysis using the Well Function.

### 📊 Statistics (`hydrology/statistics.py`)
- **Frequency Analysis**: Extreme value analysis for flood risk.
  - **Gumbel (EVI)**: Double-exponential distribution for annual maximums.
  - **Log-Pearson Type 3 (LP3)**: Used for flood frequency in the US (Bulletin 17B/C).

## Installation

```bash
# Clone the repository
git clone https://github.com/dehongi/hydrology.git
cd hydrology

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the library and dependencies
pip install -e ".[dev]"
```

## Running Verification

```bash
# Run unit tests
python3 -m pytest tests/

# Run the demo script
python3 examples/demo.py
```
