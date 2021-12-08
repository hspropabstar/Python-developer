SELECT DISTINCT(T.goods_type_name) as most_popular_category from goods g
inner join
(SELECT sum(total), goods_id  from orders 
GROUP by goods_id
ORDER BY SUM(total) DESC LIMIT 1) o
on o.goods_id = g.goods_type_id
inner JOIN goods_type t
on o.goods_id = T.goods_type_id