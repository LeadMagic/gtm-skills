# Revenue Forecasting — Framework Notes

## Primary Sources

- Clari, Five Sales Forecasting Metrics: <https://pages.clari.com/rs/866-BBG-005/images/Clari-Five_Sales_Forecasting_Metrics.pdf>
- Clari, Forecasting Blueprint: <https://pages.clari.com/rs/866-BBG-005/images/forecasting-blueprint-fof.pdf>
- Winning by Design, revenue architecture resources: <https://winningbydesign.com/>
- Stage 2 Capital, John McMahon deal coaching: <https://www.stage2.capital/blog/coaching-your-salesperson-through-a-deal-that-is-pushing.-3-minute-role-play-with-john-mcmahon-board-member-at-mongodb-snowflake-and-sprinklr>
- Dave Kellogg, triangulation forecasts: <https://www.kellblog.com/use-triangulation-forecasts-for-better-conversations-about-the-forecast/>
- Dave Kellogg, sales management cadences and forecasting rules: <https://www.kellblog.com/a-ten-point-sales-management-framework-for-enterprise-saas-startups/>

## Calculation Rules

1. Define the forecasted revenue type before adding values.
2. Preserve point-in-time snapshots so movement can be explained.
3. Segment historical conversion and timing when the underlying motions differ.
4. Show raw amount, judgment category, calculated probability, and scenario inclusion separately.
5. Never treat a weighted pipeline total as guaranteed revenue.
6. Report concentration, sample size, missing fields, and outlier treatment.

## Accuracy Measures

- Absolute error: `abs(actual - forecast)`.
- Percentage error: `abs(actual - forecast) / actual`, with an explicit zero-actual rule.
- Directional bias: signed `forecast - actual` over repeated periods.
- Slip rate: opportunities moved beyond the forecast period divided by eligible open opportunities.
- Commit attainment: actual eligible revenue divided by the final committed amount.
