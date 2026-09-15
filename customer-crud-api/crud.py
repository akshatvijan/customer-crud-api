from database import get_connection


def create_customer(name, email, phone, city, age):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        insert into customers (name, email, phone, city, age)
        values (%s, %s, %s, %s, %s);
    """

    cur.execute(query, (name, email, phone, city, age))

    conn.commit()

    cur.close()
    conn.close()


def get_customers():
    conn = get_connection()
    cur = conn.cursor()

    query = """
        select customer_id, name, email, phone, city, age, created_at
        from customers
        order by customer_id;
    """

    cur.execute(query)
    customers = cur.fetchall()

    cur.close()
    conn.close()

    return customers


def get_customer_by_id(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        select customer_id, name, email, phone, city, age, created_at
        from customers
        where customer_id = %s;
    """

    cur.execute(query, (customer_id,))
    customer = cur.fetchone()

    cur.close()
    conn.close()

    return customer


def update_customer(customer_id, name, phone, city):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        update customers
        set name = %s,
            phone = %s,
            city = %s
        where customer_id = %s;
    """

    cur.execute(query, (name, phone, city, customer_id))

    rows_updated = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return rows_updated


def delete_customer(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        delete from customers
        where customer_id = %s;
    """

    cur.execute(query, (customer_id,))

    rows_deleted = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return rows_deleted


if __name__ == "__main__":
    create_customer(
        "Test Customer",
        "test.customjher@example.com",
        "9876500000",
        "Delhi",
        25
    )
    print("create_customer:", "success")

    customers = get_customers()
    print("get_customers:", len(customers))

    customer = get_customer_by_id(1)
    print("get_customer_by_id:", customer)

    updated = update_customer(
        1,
        "Updated Customer",
        "9999999999",
        "Noida"
    )
    print("update_customer:", updated)

    deleted = delete_customer(301)
    print("delete_customer:", deleted)