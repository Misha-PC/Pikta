1) Список клиентов с общей суммой покупок
>SELECT clients.user_name, SUM(products.price) 
> 
>FROM orders 
> 
>JOIN products ON orders.id_product = products.id_product
> 
>JOIN clients ON orders.id_user = clients.id_user
> 
>GROUP BY clients.user_name


2) Список клиентов, купивших телефон

>SELECT clients.user_name
> 
>FROM orders
> 
>JOIN products ON orders.id_product = products.id_product
> 
>JOIN clients ON orders.id_user = clients.id_user
> 
>WHERE products.product_name='Телефон'


3) Список товаров с количеством их заказов 

>SELECT products.product_name, COUNT(orders.id_product)
> 
>FROM orders
> 
>JOIN products ON orders.id_product = products.id_product
> 
>GROUP BY products.product_name