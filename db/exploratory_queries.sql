-- Top 10 companies by ROE

SELECT
company_name,
roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;

-- Top 10 companies by ROCE

SELECT
company_name,
roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;

-- Highest Market Cap

SELECT
company_id,
market_cap_crore
FROM market_cap
ORDER BY market_cap_crore DESC
LIMIT 10;

-- Highest EPS

SELECT
company_id,
eps
FROM profitandloss
ORDER BY eps DESC
LIMIT 10;

-- Highest Net Profit

SELECT
company_id,
net_profit
FROM profitandloss
ORDER BY net_profit DESC
LIMIT 10;