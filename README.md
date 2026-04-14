markdown
# February 2026 Sector Indices Performance Dashboard

This project provides a user-friendly, interactive dashboard for analyzing the performance of various financial sector indices for February 2026. It is built using Python and the Dash web application framework.

## Features
- Visualize daily performance metrics for sector indices (e.g., FADX15, FADGI, FADSI, FADXI15, FADXSI).
- Filter data dynamically by selecting specific indices and date ranges.
- Generate real-time, interactive line and bar charts for closing values and daily percentage changes.
- Export analyzed data in spreadsheet-compatible formats such as XLSX.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Install the necessary libraries by running:

bash
pip install pandas dash plotly openpyxl


### Installation
1. Clone the repository:
   bash
   git clone https://github.com/your-repo/february-2026-sector-indices-dashboard.git
   
2. Navigate to the project directory:
   bash
   cd february-2026-sector-indices-dashboard
   
3. Place the `Indices_Summary_FEB_0.xlsx` file in the project directory.

### Running the Application
1. Run the application script:
   bash
   python app.py
   
2. Open your web browser and navigate to http://127.0.0.1:8050/ to view the dashboard.

## Usage
1. Select a sector index from the dropdown menu.
2. Pick a date range using the date picker.
3. View the performance graph and daily percentage change graph.
4. To download the analyzed data, click the export button (feature to be implemented).

## Future Enhancements
- Add data export functionality in CSV and JSON formats.
- Introduce more advanced analytical tools such as moving averages and correlation matrices.
- Enable integration with live data feeds for real-time updates.
- Include a help section with educational resources and use-case examples.

## Contributing
We welcome contributions! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the Open Data Commons Open Database License (ODbL).
