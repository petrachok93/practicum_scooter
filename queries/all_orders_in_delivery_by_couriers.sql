SELECT login,
       count(*)
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY login;