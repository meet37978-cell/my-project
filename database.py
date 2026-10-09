import sqlite3
import os
from datetime import datetime


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

DATABASE_FILE = os.path.join(
    DATA_DIR,
    "attendance.db"
)

os.makedirs(
    DATA_DIR,
    exist_ok=True
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    conn = sqlite3.connect(
        DATABASE_FILE,
        check_same_thread=False
    )

    return conn


# ============================================================
# CREATE DATABASE
# ============================================================

def create_database():

    conn = get_connection()

    cursor = conn.cursor()

    # --------------------------------------------------------
    # STUDENTS TABLE
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_id TEXT UNIQUE NOT NULL,

            name TEXT NOT NULL,

            phone TEXT,

            course TEXT,

            embedding TEXT,

            image_path TEXT,

            created_at TEXT

        )
    """)

    # --------------------------------------------------------
    # ATTENDANCE TABLE
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_id TEXT NOT NULL,

            date TEXT NOT NULL,

            time TEXT NOT NULL,

            status TEXT DEFAULT 'PRESENT',

            confidence REAL,

            UNIQUE(student_id, date)

        )
    """)

    conn.commit()

    conn.close()


# ============================================================
# ADD STUDENT
# ============================================================

def add_student(
    student_id,
    name,
    phone,
    course,
    embedding,
    image_path,
    created_at=None
):

    if created_at is None:

        created_at = datetime.now().isoformat()


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO students
        (
            student_id,
            name,
            phone,
            course,
            embedding,
            image_path,
            created_at
        )
        VALUES
        (?, ?, ?, ?, ?, ?, ?)
    """, (

        student_id,
        name,
        phone,
        course,
        embedding,
        image_path,
        created_at

    ))


    conn.commit()

    conn.close()


# ============================================================
# CHECK STUDENT EXISTS
# ============================================================

def student_exists(
    student_id
):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        SELECT id
        FROM students
        WHERE student_id = ?
    """, (
        student_id,
    ))


    result = cursor.fetchone()

    conn.close()


    return result is not None


# ============================================================
# GET ALL STUDENTS
# ============================================================

def get_students():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        SELECT

            id,
            student_id,
            name,
            phone,
            course,
            embedding,
            image_path,
            created_at

        FROM students

        ORDER BY name ASC
    """)


    rows = cursor.fetchall()

    conn.close()


    return rows


# ============================================================
# GET SINGLE STUDENT
# ============================================================

def get_student(
    student_id
):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        SELECT

            id,
            student_id,
            name,
            phone,
            course,
            embedding,
            image_path,
            created_at

        FROM students

        WHERE student_id = ?
    """, (
        student_id,
    ))


    row = cursor.fetchone()

    conn.close()


    return row


# ============================================================
# ADD ATTENDANCE
# ============================================================

def add_attendance(
    student_id,
    date,
    time,
    status="PRESENT",
    confidence=0.0
):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        INSERT OR IGNORE INTO attendance
        (
            student_id,
            date,
            time,
            status,
            confidence
        )
        VALUES
        (?, ?, ?, ?, ?)
    """, (

        student_id,
        date,
        time,
        status,
        confidence

    ))


    inserted = (
        cursor.rowcount > 0
    )


    conn.commit()

    conn.close()


    return inserted


# ============================================================
# GET ALL ATTENDANCE
# ============================================================

def get_attendance():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        SELECT

            id,
            student_id,
            date,
            time,
            status,
            confidence

        FROM attendance

        ORDER BY
            date DESC,
            time DESC
    """)


    rows = cursor.fetchall()

    conn.close()


    return rows


# ============================================================
# GET TODAY ATTENDANCE
# ============================================================

def get_today_attendance():

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        SELECT

            id,
            student_id,
            date,
            time,
            status,
            confidence

        FROM attendance

        WHERE date = ?

        ORDER BY time DESC
    """, (
        today,
    ))


    rows = cursor.fetchall()

    conn.close()


    return rows


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student(
    student_id
):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        DELETE FROM attendance
        WHERE student_id = ?
    """, (
        student_id,
    ))


    cursor.execute("""
        DELETE FROM students
        WHERE student_id = ?
    """, (
        student_id,
    ))


    deleted = (
        cursor.rowcount > 0
    )


    conn.commit()

    conn.close()


    return deleted


# ============================================================
# DELETE ALL DATA
# ============================================================

def delete_all_data():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        "DELETE FROM attendance"
    )

    cursor.execute(
        "DELETE FROM students"
    )


    conn.commit()

    conn.close()


# ============================================================
# DATABASE COUNTS
# ============================================================

def get_student_count():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        SELECT COUNT(*)
        FROM students
    """)


    count = cursor.fetchone()[0]

    conn.close()


    return count


def get_attendance_count():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
    """)


    count = cursor.fetchone()[0]

    conn.close()


    return count


# ============================================================
# INITIALIZE DATABASE
# ============================================================

create_database()


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    create_database()

    print(
        "================================"
    )

    print(
        "DATABASE READY"
    )

    print(
        "================================"
    )

    print(
        "Database:",
        DATABASE_FILE
    )

    print(
        "Students:",
        get_student_count()
    )

    print(
        "Attendance:",
        get_attendance_count()
    )