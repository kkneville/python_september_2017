-- 1
SELECT SUM(billing.amount) AS revenue FROM billing
WHERE MONTH(billing.charged_datetime) = 3 AND year(billing.charged_datetime) = 2012;

-- 2
SELECT SUM(billing.amount) AS revenue FROM billing
WHERE client_id = 2;

-- 3
SELECT domain_name AS website, client_id FROM sites
WHERE client_id = 10;

-- 4
SELECT sites.client_id, COUNT(sites.site_id) AS num_of_sites , MONTH(sites.created_datetime) AS month_created, YEAR(sites.created_datetime) AS year_created  FROM sites
WHERE sites.client_id = 1 -- or 20 for part 2
GROUP BY month_created, year_created;

-- 5
SELECT sites.domain_name, COUNT(leads.leads_id) AS leads_per_site, DATE_FORMAT(leads.registered_datetime, '%b %e, %Y') AS date_generated FROM leads
JOIN sites ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN CAST('2011-01-01' AS DATE) AND CAST('2011-02-15' AS DATE)
GROUP BY sites.site_id, date_generated;

-- 6
SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads  FROM leads
JOIN sites ON leads.site_id = sites.site_id
JOIN clients ON clients.client_id = sites.client_id
WHERE leads.registered_datetime BETWEEN CAST('2011-01-01' AS DATE) AND CAST('2011-12-31' AS DATE)
GROUP BY clients.client_id;

-- 7
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, COUNT(leads.leads_id) AS 'count', MONTHNAME(leads.registered_datetime) AS month_generated FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE YEAR(leads.registered_datetime) = 2011 AND MONTH(leads.registered_datetime) BETWEEN 1 AND 6 
GROUP BY client_name, leads.registered_datetime
ORDER BY leads.registered_datetime;

-- 8.a
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, MIN(DATE_FORMAT(leads.registered_datetime, '%b %e, %Y')) AS date_generated FROM leads -- leads.registered_datetime AS date_generated
JOIN sites ON  leads.site_id = sites.site_id
JOIN clients ON clients.client_id = sites.client_id
WHERE  leads.registered_datetime BETWEEN CAST('2011-01-01' AS DATE) AND CAST('2011-12-31' AS DATE)
GROUP BY  client_name, website
ORDER BY client_name;

-- 8.2
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads FROM leads -- leads.registered_datetime AS date_generated
JOIN sites ON  leads.site_id = sites.site_id
JOIN clients ON clients.client_id = sites.client_id
GROUP BY  client_name, website
ORDER BY client_name ASC, number_of_leads DESC;

-- 9
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, SUM(billing.amount) AS total_revenue, MONTHNAME(billing.charged_datetime) AS month_charged, YEAR(billing.charged_datetime) AS year_charged FROM billing
JOIN clients ON clients.client_id = billing.client_id
GROUP BY billing.client_id, year_charged, month_charged
ORDER BY billing.client_id;

-- 10
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name) AS websites FROM  clients
JOIN sites ON sites.client_id = clients.client_id
GROUP BY clients.client_id;