-- Total Tickets

SELECT COUNT(*) AS total_tickets
FROM tickets;


-- Open Tickets

SELECT *
FROM tickets
WHERE status = 'Open';


-- Resolved Tickets

SELECT *
FROM tickets
WHERE status = 'Resolved';


-- Tickets By Priority

SELECT
    priority,
    COUNT(*) AS total
FROM tickets
GROUP BY priority;


-- Employee Ticket Count

SELECT
    assigned_to,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY assigned_to;


-- Most Assigned Employee

SELECT
    assigned_to,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY assigned_to
ORDER BY total_tickets DESC;


-- Ticket Status Report

SELECT
    status,
    COUNT(*) AS total
FROM tickets
GROUP BY status;


-- Rank Employees By Tickets

SELECT
    assigned_to,
    COUNT(*) AS total_tickets,
    RANK() OVER(
        ORDER BY COUNT(*) DESC
    ) AS rank_no
FROM tickets
GROUP BY assigned_to;
