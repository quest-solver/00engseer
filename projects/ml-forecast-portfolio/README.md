# B100 Biodiesel Demand Forecast - Quebec Maritime Case

## Overview
Decision-support framework for B100 biodiesel demand forecasting
and maritime infrastructure feasibility in a Quebec research case,
developed during postdoctoral research at Université de Sherbrooke
in collaboration with Innovation Maritime (IMAR).

The project integrates maritime traffic forecasting, commodity price
modeling, and IMO Net-Zero regulatory scenarios into a unified
analytical framework for strategic port planning.

## Key Findings
- Traffic ceiling constrains fuel adoption more than price alone
- Regulatory tightening progressively increases B100 activation
- Transit vessel participation amplifies demand magnitude significantly
- Long-horizon uncertainty requires scenario-based planning, not point forecasts
- The hybrid ML model (HW + XGB) outperforms classical methods on
  volatile maritime series

## Data Sources
- Maritime traffic (calling/transit): transformed research outputs
  derived from maritime information systems; vessel-level data is not included
- B100 price proxy: DOE biodiesel series + Bloomberg commodity data
- Exogenous drivers: crude oil, heating oil, soybean oil, gasoline,
  EU carbon permits, USD/CAD exchange rate

## Public Data And Compliance
This repository is intended as a public portfolio artifact. It excludes raw
vessel-level records, private operational data, credentials, local runtime files,
and any source material that could identify confidential research partners or
operations.

The included CSV files are transformed modeling inputs and outputs used to
demonstrate the forecasting workflow. Before adding new data, verify that it is
aggregated, non-sensitive, and appropriate for public release.

## Methodology
The project follows CRISP-DM, with two parallel modeling tracks:

**Traffic Modeling (Calling & Transit)**
- Holt-Winters exponential smoothing as classical baseline
- XGBoost regressor trained on HW residuals for error correction
- XGBoost classifier on the error series to detect zero-crossing
  patterns - used as a feature to capture behavioral shifts in
  the residual structure
- Confidence intervals computed at both error and setpoint levels

**B100 Price Modeling**
- Same hybrid architecture applied to the B100 price index
- Exogenous features engineered with lags and rolling means

**Final Output**
Hybrid forecast = HW baseline + XGB error correction

## Notebooks

### `RUN_features.ipynb`
Engineered exogenous features: lags and rolling means for both
raw series and residuals. Runs on any Python platform (Jupyter).

### `HoltWinter_w_folds.ipynb`
Holt-Winters forecasting with cross-validation folds and
exploratory analysis. Runs on any Python platform (Jupyter).
Reflects exploratory thinking - prioritizes output analysis
over code cleanliness.

### `XGBoost_consumption_Passage_hybrid.ipynb`
### `XGBoost_consumption_Scale_hybrid.ipynb`
### `XGBoost_B100_structured_hybrid.ipynb`
XGBoost residual correction models for transit, calling, and
B100 respectively. Designed to run on Google Colab (uses
Colab-specific features). Purpose is strategic efficiency,
not strict replicability.

## Data Structure
```
data/
|-- calling/
|   |-- TargetXGB_scale.csv              <- target series for XGB
|   `-- full_consumption_scale_hybrid_df.csv  <- final forecast output
|-- transit/
|   |-- TargetXGB_passage.csv
|   `-- full_consumption_passage_hybrid_df.csv
|-- b100/
|   |-- TargetXGB_b100.csv
|   `-- b100_structured_hybrid_df.csv    <- extended CI columns
`-- engineered/
    `-- XGB_FULL_exogenous_input.csv     <- all engineered features
```

**Column structure (calling/transit):**
`Date | series_value | HW_forecast | XGB_error_future | CI_upper`

Historical period: only `series_value` populated.
Forecast horizon: all columns populated.

**Column structure (b100):**
Same as above plus `CI_lower | real_CI_upper | real_CI_lower`
CI columns = pure error correction values.
real_CI columns = correction anchored to actual setpoint.

## Dashboards
Power BI dashboards showing:
- Vessel Calling Potential Capacity & Forecast (ML vs Classical vs Historical)
- B100 Price Forecast (ML vs Classical, with confidence intervals)
- Policy-Driven IMO Scenario Analysis - Standard/Direct and
  Minimum/Base fuel requirement trajectories under different
  traffic expectations and regulatory intensities

Interactive sliders allow scenario exploration across calling
expectation, transit expectation, and IMO regulatory targets.

## Note
Raw vessel-level AIS data and private operational records are not included.
All data in this repository represents
transformed and engineered outputs produced during the research.
