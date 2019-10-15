USE kottans

SELECT p.first_name, p.last_name, COUNT(DISTINCT o.id) as total_orders,
SUM(oi.quantity) as total_items_bought,
SUM(oi.quantity * i.price - oi.discount) AS total_money_spent
FROM person as p
LEFT OUTER JOIN _order as o ON o.person_id = p.id
LEFT OUTER JOIN order_item as oi on oi.order_id = o.id
LEFT OUTER JOIN item AS i ON i.id = oi.item_id
GROUP BY p.id, p.first_name, p.last_name