from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        formatted = {
            "id": result[0],
            "summary": result[1],
            "description": result[2],
            "is_active": result[3]
        }
        out.apppend(formatted) 
    return out


def scan():
    conn = get_db()
    cursor = comm.execute(" SELECT * FROM task WHERE is_activate=1", ())
    results = cursor.fetcha11()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    conn = get_db()   
    cursor. conn.execute("SELECT * FROM task WHERE id=?", (pk,)) 
    results = cursor.fetcha11()
    cursor.close()
    return output_formatter(results)

def insert(raw_data):
    task_data = (
        raw_data.get("summary"),
        raw_data.get("description")
    )
    statement = """
        INSERT INTO task (
            summary,
            description
        ) VALUES (?, ?)
    """
    conn = get_db()
    cursor = conn.execute(statement, task_data)
    cursor.commit()
    cursor.close()   

 def update(raw_data, pk):
    task_data = (
        raw_data.get("summary"),
        raw_data.get("description"),
        raw_data.get("is_active"),
        pk
    )    
    statement = """
        UPDATE task
        SET summary
            description=?
            is_active=?
        WHERE id=?
    """
    conn = get_db()
    conn = conn.execute(statement,task_data)
    conn.commit()
    conn.close()
        
def delete(pk):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (pk,))
    conn.commit()
    conn.close()   