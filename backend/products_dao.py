from sql_connection import get_sql_connection

def get_all_product(connection):
  cursor = connection.cursor()
  query = ('''SELECT 
      products.product_id, 
      products.name, 
      products.uom_id, 
      products.price_per_unit, 
      uom.uom_name
  FROM products
  INNER JOIN uom 
      ON products.uom_id = uom.id''')

  cursor.execute(query)

  response = []

  for (product_id, name, uom_id, price_per_unit,uom_name) in cursor:
    response.append(
      {
        'product_id': product_id,
        'name' : name,
        'uom_id' : uom_id,
        'price_per_unit':price_per_unit,
        'uom_name' : uom_name
      }
    )

  return response

def insert_new_product(connection,product):
  cursor = connection.cursor()
  query = ("INSERT INTO products"
          "(name,uom_id,price_per_unit)" 
          "value(%s,%s,%s)")
  data = (product['name'], product['uom_id'], product['price_per_unit'])
  cursor.execute(query,data)
  connection.commit()

  return cursor.lastrowid

def delete_product(connection, product_id):
  cursor = connection.cursor()
  query = ("DELETE FROM products where product_id="+str(product_id))
  cursor.execute(query)
  connection.commit()

def update_product(connection, product):
    cursor = connection.cursor()
    query = ("UPDATE products SET name=%s, uom_id=%s, price_per_unit=%s "
             "WHERE product_id=%s")
    data = (product['name'], product['uom_id'], product['price_per_unit'], product['id'])
    cursor.execute(query, data)
    connection.commit()
    return product['id']


if __name__ == '__main__':
  connection = get_sql_connection()
  print(delete_product(connection,6))