from app.db_connect import connect 


def get_posts():
    conn = connect()
    with conn.cursor() as cur:
        sql = f"""
               SELECT p.id, title, body, created, author_id, u.user_name FROM user u
               INNER JOIN post p ON p.author_id = u.id
               """
        cur.execute(sql)
        return cur.fetchall()


def get_post(post_id):
    conn = connect()
    with conn.cursor() as cur:
        sql = f"""
               SELECT p.title, body, created, author_id, u.user_name FROM user u
               INNER JOIN post p ON p.author_id = u.id
               WHERE p.id = %s
               """
        cur.execute(sql, (post_id,))
        return cur.fetchone()
    
   