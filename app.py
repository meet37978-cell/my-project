import streamlit as st
import pandas as pd
import numpy as np
import cv2
import os
import io
import av
import threading
import time
import sqlite3
import hashlib

from datetime import datetime
from PIL import Image

from streamlit_webrtc import (
    webrtc_streamer,
    VideoProcessorBase,
    WebRtcMode
)

from streamlit_autorefresh import st_autorefresh

# cd D:\myproject\student_attendance
# streamlit run app.py

# ============================================================
# DATABASE (existing project module — untouched)
# ============================================================

from database import (
    create_database,
    student_exists,
    add_student,
    get_students,
    add_attendance,
    get_attendance
)


# ============================================================
# FACE ENGINE (existing project module — untouched)
# ============================================================

from face_engine import (
    detect_faces,
    get_embedding,
    face_similarity,
    draw_face_box
)


create_database()


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
FACE_FOLDER = os.path.join(BASE_DIR, "faces")
EXPORT_FOLDER = os.path.join(BASE_DIR, "exports")

os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(FACE_FOLDER, exist_ok=True)
os.makedirs(EXPORT_FOLDER, exist_ok=True)

DATABASE_PATH = os.path.join(DATA_FOLDER, "attendance.db")


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SmartAttendance System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# THEME — "CONTROL ROOM" DESIGN SYSTEM
# A clean, light, professional SaaS-admin look built around a
# teal "presence" signal (attendance = presence) with an amber
# secondary accent, on a cool slate-white canvas.
#   Sora  -> headings, page titles, big numbers (display voice)
#   Inter -> body text, tables, inputs, data (working voice)
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --bg:             #0A0F1C;
        --bg-pattern:     radial-gradient(900px 420px at 90% -8%, rgba(20,184,166,0.12), transparent 60%),
                          radial-gradient(700px 420px at -5% 8%, rgba(251,191,36,0.08), transparent 55%);
        --surface:        #121A2B;
        --surface-alt:    #172034;
        --border:         #253248;
        --border-strong:  #37496A;
        --text:           #EDF1F9;
        --text-muted:     #9DABC6;
        --text-faint:     #6C7C9B;

        --primary:        #14B8A6;
        --primary-dark:   #0D9488;
        --primary-soft:   rgba(20, 184, 166, 0.16);

        --secondary:      #FBBF24;
        --secondary-soft: rgba(251, 191, 36, 0.14);

        --success:        #22C55E;
        --success-soft:   rgba(34, 197, 94, 0.14);
        --danger:         #F87171;
        --danger-soft:    rgba(248, 113, 113, 0.14);
        --info:           #60A5FA;
        --info-soft:      rgba(96, 165, 250, 0.14);

        --radius:         16px;
        --radius-sm:      10px;
        --shadow-sm:      0 1px 2px rgba(0,0,0,0.25);
        --shadow-md:      0 8px 24px rgba(0,0,0,0.35);
    }

    /* Force a dark UI regardless of the viewer's OS/browser
       light-mode preference — without this, native form controls
       and any un-styled Streamlit chrome can render light even
       though the app's own surfaces are themed dark. */
    html {
        color-scheme: dark !important;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, sans-serif !important;
    }

    .stApp {
        background-color: var(--bg);
        background-image: var(--bg-pattern);
        color: var(--text);
    }

    /* Top toolbar / header bar */
    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stToolbar"] {
        color: var(--text) !important;
    }

    [data-testid="stDecoration"] {
        background: linear-gradient(90deg, var(--primary), var(--secondary));
    }

    /* Main content area background (covers the view container
       Streamlit renders around .block-container) */
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background-color: var(--bg);
    }

    .block-container {
        max-width: 1400px;
        padding-top: 22px;
        padding-bottom: 60px;
    }

    h1, h2, h3, h4, h5 {
        font-family: 'Sora', sans-serif !important;
        color: var(--text) !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em;
    }

    h1 { font-size: 1.9rem !important; }
    h3 { font-size: 1.15rem !important; }

    p, span, label, li { color: var(--text-muted); }

    [data-testid="stCaptionContainer"] p, .stCaption {
        text-transform: uppercase;
        letter-spacing: 0.09em;
        font-size: 0.72rem !important;
        color: var(--primary) !important;
        font-weight: 700;
    }

    /* ---------------- SIDEBAR ---------------- */

    [data-testid="stSidebar"] {
        background: var(--surface);
        border-right: 1px solid var(--border);
    }

    [data-testid="stSidebar"] > div:first-child { padding-top: 6px; }

    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 6px 4px 14px 4px;
    }

    .sidebar-brand .mark {
        width: 38px;
        height: 38px;
        border-radius: 11px;
        background: linear-gradient(140deg, var(--primary), var(--primary-dark));
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.15rem;
        box-shadow: var(--shadow-sm);
    }

    .sidebar-brand .name {
        font-family: 'Sora', sans-serif;
        font-weight: 700;
        font-size: 1.02rem;
        color: var(--text);
        line-height: 1.15;
    }

    .sidebar-brand .tag {
        font-size: 0.72rem;
        color: var(--text-faint);
    }

    [data-testid="stSidebar"] div[role="radiogroup"] { gap: 3px; }

    [data-testid="stSidebar"] div[role="radiogroup"] label {
        background: transparent;
        border-radius: 10px;
        padding: 9px 12px !important;
        border: 1px solid transparent;
        transition: all 0.15s ease;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: var(--surface-alt);
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
        background: var(--primary-soft);
        border: 1px solid rgba(13,148,136,0.25);
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
        color: var(--primary-dark) !important;
        font-weight: 700;
    }

    /* ---------------- INPUTS ---------------- */

    input, textarea {
        background: var(--surface) !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
    }

    input:focus, textarea:focus {
        border: 1px solid var(--primary) !important;
        box-shadow: 0 0 0 3px var(--primary-soft) !important;
    }

    div[data-baseweb="select"] > div {
        background: var(--surface) !important;
        color: var(--text) !important;
        border-color: var(--border) !important;
        border-radius: var(--radius-sm) !important;
    }

    /* Selectbox dropdown menu — rendered in a portal, so it
       needs its own override or it inherits the browser's dark
       native styling. */
    div[data-baseweb="popover"] div[data-baseweb="menu"],
    ul[data-baseweb="menu"] {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
    }

    li[data-baseweb="menu-item"] {
        background: var(--surface) !important;
        color: var(--text) !important;
    }

    li[data-baseweb="menu-item"]:hover {
        background: var(--primary-soft) !important;
    }

    /* ---------------- BUTTONS ---------------- */

    div.stButton > button {
        background: var(--primary);
        color: #FFFFFF;
        border: none;
        border-radius: var(--radius-sm);
        min-height: 42px;
        font-weight: 600;
        transition: filter 0.15s ease, transform 0.05s ease;
    }

    div.stButton > button:hover { filter: brightness(1.08); color: #fff; }
    div.stButton > button:active { transform: translateY(1px); }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(180deg, #10A99C, var(--primary));
        box-shadow: var(--shadow-sm);
    }

    div.stButton > button[kind="secondary"] {
        background: var(--surface);
        color: var(--text) !important;
        border: 1px solid var(--border-strong);
    }

    div.stButton > button[kind="secondary"]:hover { border-color: var(--primary); }

    div[data-testid="stDownloadButton"] > button {
        background: var(--surface);
        color: var(--primary-dark) !important;
        border: 1px solid var(--primary);
        border-radius: var(--radius-sm);
        font-weight: 600;
    }

    /* Danger-flavoured buttons — target by key prefix */
    div[class*="st-key-danger_"] div.stButton > button {
        background: var(--surface);
        color: var(--danger) !important;
        border: 1px solid rgba(220,38,38,0.35);
    }
    div[class*="st-key-danger_"] div.stButton > button:hover {
        background: var(--danger-soft);
    }

    div[class*="st-key-ghost_"] div.stButton > button {
        background: var(--surface);
        color: var(--text-muted) !important;
        border: 1px solid var(--border);
    }

    /* ---------------- METRICS ---------------- */

    div[data-testid="stMetric"] {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 18px 20px;
        box-shadow: var(--shadow-sm);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }

    div[data-testid="stMetricLabel"] {
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-size: 0.7rem !important;
        color: var(--text-faint) !important;
        font-weight: 700;
    }

    div[data-testid="stMetricValue"] {
        font-family: 'Sora', sans-serif !important;
        color: var(--text) !important;
    }

    /* ---------------- DATAFRAME ---------------- */

    [data-testid="stDataFrame"] {
        border: 1px solid var(--border);
        border-radius: var(--radius-sm);
        overflow: hidden;
        box-shadow: var(--shadow-sm);
    }

    /* ---------------- ALERTS ---------------- */

    div[data-testid="stAlert"] {
        border-radius: var(--radius-sm);
        border: 1px solid var(--border);
    }

    div[data-testid="stAlertContentSuccess"] { color: var(--success) !important; }
    div[data-testid="stAlertContentError"]   { color: var(--danger) !important; }
    div[data-testid="stAlertContentInfo"]    { color: var(--info) !important; }
    div[data-testid="stAlertContentWarning"] { color: var(--secondary) !important; }

    hr { border-color: var(--border); }

    button[data-baseweb="tab"] { color: var(--text-muted) !important; }
    button[data-baseweb="tab"][aria-selected="true"] { color: var(--primary) !important; }

    /* ---------------- BADGES / CHIPS ---------------- */

    .chip {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 0.76rem;
        font-weight: 600;
        letter-spacing: 0.01em;
    }

    .chip-present { background: var(--success-soft); color: var(--success); border: 1px solid rgba(22,163,74,0.3); }
    .chip-absent  { background: var(--danger-soft); color: var(--danger); border: 1px solid rgba(220,38,38,0.3); }
    .chip-neutral { background: var(--surface-alt); color: var(--text-muted); border: 1px solid var(--border); }
    .chip-course  { background: var(--info-soft); color: var(--info); border: 1px solid rgba(37,99,235,0.25); }

    /* ---------------- HERO BANNER ---------------- */

    .page-hero {
        border: 1px solid var(--border);
        background: var(--surface);
        border-radius: var(--radius);
        padding: 22px 26px;
        margin-bottom: 18px;
        box-shadow: var(--shadow-sm);
        position: relative;
        overflow: hidden;
    }

    .page-hero::before {
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 5px; height: 100%;
        background: var(--page-accent, var(--primary));
    }

    .page-hero .eyebrow {
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-size: 0.7rem;
        color: var(--page-accent, var(--primary));
        font-weight: 700;
        margin: 0 0 6px 0;
    }

    .page-hero h1 { margin: 0 0 4px 0 !important; }

    .page-hero .sub { color: var(--text-muted); font-size: 0.95rem; margin: 0; }

    /* ---------------- STUDENT ID CARD ROW ---------------- */

    div[class*="st-key-student_card_"] {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 14px 16px;
        margin-bottom: 10px;
        box-shadow: var(--shadow-sm);
        transition: box-shadow 0.15s ease, border-color 0.15s ease;
    }

    div[class*="st-key-student_card_"]:hover {
        box-shadow: var(--shadow-md);
        border-color: var(--border-strong);
    }

    div[class*="st-key-edit_panel_"] {
        background: var(--surface-alt);
        border: 1px dashed var(--primary);
        border-radius: var(--radius);
        padding: 16px 18px 6px 18px;
        margin: -4px 0 12px 0;
    }

    div[class*="st-key-delete_panel_"] {
        background: var(--danger-soft);
        border: 1px solid rgba(220,38,38,0.35);
        border-radius: var(--radius);
        padding: 14px 18px;
        margin: -4px 0 12px 0;
    }

    .avatar-circle {
        width: 42px;
        height: 42px;
        min-width: 42px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Sora', sans-serif;
        font-weight: 700;
        font-size: 0.95rem;
        color: #fff;
    }

    .student-name { font-weight: 700; color: var(--text); font-size: 0.98rem; }
    .student-sub { font-size: 0.8rem; color: var(--text-faint); }

    /* ---------------- CAMERA SCAN FRAME ---------------- */

    div[class*="st-key-cam_scan_"] {
        position: relative;
        border-radius: 18px;
        padding: 18px 18px 22px 18px;
        margin: 4px 0 10px 0;
        background: linear-gradient(var(--surface), var(--surface)) padding-box;
        background-image:
            linear-gradient(90deg, var(--cam-accent, var(--primary)) 3px, transparent 3px),
            linear-gradient(180deg, var(--cam-accent, var(--primary)) 3px, transparent 3px),
            linear-gradient(90deg, var(--cam-accent, var(--primary)) 3px, transparent 3px),
            linear-gradient(180deg, var(--cam-accent, var(--primary)) 3px, transparent 3px),
            linear-gradient(90deg, var(--cam-accent, var(--primary)) 3px, transparent 3px),
            linear-gradient(180deg, var(--cam-accent, var(--primary)) 3px, transparent 3px),
            linear-gradient(90deg, var(--cam-accent, var(--primary)) 3px, transparent 3px),
            linear-gradient(180deg, var(--cam-accent, var(--primary)) 3px, transparent 3px);
        background-repeat: no-repeat;
        background-size: 30px 3px, 3px 30px, 30px 3px, 3px 30px, 30px 3px, 3px 30px, 30px 3px, 3px 30px;
        background-position: 0 0, 0 0, 100% 0, 100% 0, 0 100%, 0 100%, 100% 100%, 100% 100%;
        border: 1px solid var(--border);
        overflow: hidden;
        box-shadow: var(--shadow-sm);
    }

    div[class*="st-key-cam_scan_"]::after {
        content: "";
        position: absolute;
        left: 10px; right: 10px;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--cam-accent, var(--primary)) 50%, transparent);
        opacity: 0.75;
        animation: cam-scan-move 2.6s ease-in-out infinite;
        pointer-events: none;
    }

    @keyframes cam-scan-move {
        0%   { top: 8%; }
        50%  { top: 90%; }
        100% { top: 8%; }
    }

    .cam-scan-label {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        font-size: 0.7rem;
        font-weight: 700;
        color: var(--cam-accent, var(--primary));
        margin-bottom: 10px;
    }

    .cam-scan-label .dot {
        width: 7px; height: 7px;
        border-radius: 50%;
        background: var(--cam-accent, var(--primary));
        box-shadow: 0 0 0 3px color-mix(in srgb, var(--cam-accent, var(--primary)) 25%, transparent);
    }

    div[class*="st-key-cam_scan_register"] { --cam-accent: #A78BFA; }
    div[class*="st-key-cam_scan_live"]     { --cam-accent: #F87171; }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE ACCENT COLORS
# ============================================================

PAGE_ACCENTS = {
    "Dashboard":        "#14B8A6",
    "Register Student": "#A78BFA",
    "Live Attendance":  "#F87171",
    "Students":         "#60A5FA",
    "Attendance":       "#2DD4BF",
    "Analytics":        "#FBBF24",
}

AVATAR_PALETTE = [
    "#14B8A6", "#A78BFA", "#60A5FA", "#F87171",
    "#FBBF24", "#2DD4BF", "#F472B6", "#818CF8",
]


def render_hero(eyebrow, title, subtitle, accent="#14B8A6"):
    st.markdown(
        f"""
        <div class="page-hero" style="--page-accent:{accent};">
            <p class="eyebrow">{eyebrow}</p>
            <h1>{title}</h1>
            <p class="sub">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def get_initials(name):
    name = (name or "").strip()
    if not name:
        return "?"
    parts = name.split()
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def avatar_color(seed):
    seed = seed or "x"
    idx = int(hashlib.md5(seed.encode()).hexdigest(), 16) % len(AVATAR_PALETTE)
    return AVATAR_PALETTE[idx]


def render_avatar(name):
    color = avatar_color(name)
    initials = get_initials(name)
    return f'<div class="avatar-circle" style="background:{color};">{initials}</div>'


# ============================================================
# SESSION STATE
# ============================================================

DEFAULT_STATE = {
    "registration_camera": False,
    "attendance_camera_started": False,
    "student_search": "",
    "editing_student_id": None,
    "viewing_student_id": None,
    "delete_confirm_id": None,
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


def safe_float(value):
    try:
        return float(value)
    except Exception:
        return 0.0


# ============================================================
# LOW-LEVEL SCHEMA HELPERS
# ============================================================

def get_student_columns():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(students)")
        columns = [row[1] for row in cursor.fetchall()]
        conn.close()
        return columns
    except Exception as e:
        print("Column error:", e)
        return []


def get_attendance_columns():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(attendance)")
        columns = [row[1] for row in cursor.fetchall()]
        conn.close()
        return columns
    except Exception as e:
        print("Column error:", e)
        return []


def ensure_phone_column():
    try:
        columns = get_student_columns()
        if "phone" not in columns:
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute("ALTER TABLE students ADD COLUMN phone TEXT")
            conn.commit()
            conn.close()
    except Exception as e:
        print("Phone column:", e)


ensure_phone_column()


# ============================================================
# STUDENT INFO NORMALIZER
# ============================================================

STUDENT_FIELD_ORDER = [
    "id", "student_id", "name", "phone", "course", "department",
    "semester", "division", "roll_number", "academic_year",
    "embedding", "image_path", "created_at",
]


def get_student_info(student):
    columns = get_student_columns()
    info = {field: "" for field in STUDENT_FIELD_ORDER}

    for index, column in enumerate(columns):
        if index < len(student):
            info[column] = student[index]

    return info


# ============================================================
# EDIT / DELETE HELPERS (new — implemented directly against
# the SQLite database so no changes to database.py are needed)
# ============================================================

# Fields a staff member is allowed to edit from the Students
# directory. Only columns that actually exist in the students
# table are ever written to.
EDITABLE_TEXT_FIELDS = [
    ("name", "Full Name"),
    ("phone", "Phone Number"),
    ("department", "Department"),
    ("semester", "Semester"),
    ("division", "Division"),
    ("roll_number", "Roll Number"),
    ("academic_year", "Academic Year"),
]

COURSE_OPTIONS = ["Data Science", "Full Stack", "UI/UX Design", "Video Editing"]


def update_student_record(old_student_id, new_student_id, field_values):
    """
    Updates a student's row (and keeps attendance history in sync if
    the Student ID itself is changed). Only touches columns that
    actually exist in the current schema.
    """
    try:
        columns = get_student_columns()
        attendance_columns = get_attendance_columns()

        valid_updates = {
            col: val for col, val in field_values.items()
            if col in columns
        }

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        if valid_updates:
            set_clause = ", ".join(f"{col} = ?" for col in valid_updates)
            params = list(valid_updates.values()) + [old_student_id]
            cursor.execute(
                f"UPDATE students SET {set_clause} WHERE student_id = ?",
                params
            )

        id_changed = (
            new_student_id
            and new_student_id != old_student_id
        )

        if id_changed:
            cursor.execute(
                "UPDATE students SET student_id = ? WHERE student_id = ?",
                (new_student_id, old_student_id)
            )

            if "student_id" in attendance_columns:
                cursor.execute(
                    "UPDATE attendance SET student_id = ? WHERE student_id = ?",
                    (new_student_id, old_student_id)
                )

        conn.commit()
        conn.close()
        return True, None

    except Exception as e:
        return False, str(e)


def delete_student_record(student_id, image_path=None):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        attendance_columns = get_attendance_columns()
        if "student_id" in attendance_columns:
            cursor.execute(
                "DELETE FROM attendance WHERE student_id = ?",
                (student_id,)
            )

        cursor.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )

        conn.commit()
        conn.close()

        if image_path and os.path.exists(image_path):
            try:
                os.remove(image_path)
            except Exception:
                pass

        return True, None

    except Exception as e:
        return False, str(e)


# ============================================================
# FACE DATABASE
# ============================================================

def build_face_database():
    students = get_students()
    database = []

    for student in students:
        try:
            info = get_student_info(student)
            embedding_text = info["embedding"]

            if embedding_text is None:
                continue

            embedding_text = str(embedding_text).strip()
            if embedding_text == "":
                continue

            embedding = np.array(
                [float(x.strip()) for x in embedding_text.split(",") if x.strip() != ""],
                dtype=np.float32
            )

            if len(embedding) == 0:
                continue

            database.append({
                "student_id": str(info["student_id"]),
                "name": str(info["name"]),
                "course": str(info["course"]),
                "embedding": embedding
            })

        except Exception as e:
            print("Face DB error:", e)

    return database


# ============================================================
# LIVE VIDEO PROCESSOR
# ============================================================

class AttendanceVideoProcessor(VideoProcessorBase):

    PRESENT_COLOR_BGR = (166, 184, 20)   # bright teal, BGR order
    UNKNOWN_COLOR_BGR = (113, 113, 248)  # bright red, BGR order

    def __init__(self):
        self.lock = threading.Lock()
        self.students = []
        self.recognized_students = {}
        self.threshold = 0.45
        self.attendance_cooldown = 60
        self.last_save = {}
        self.recognition_time = 0
        self.should_stop = False
        self.auto_stop_seconds = 2

    def update_students(self, students):
        with self.lock:
            self.students = students

    def save_attendance(self, student_id, confidence):
        now = time.time()
        last = self.last_save.get(student_id, 0)

        if (now - last) < self.attendance_cooldown:
            return

        try:
            current = datetime.now()
            date = current.strftime("%Y-%m-%d")
            clock = current.strftime("%H:%M:%S")

            add_attendance(student_id, date, clock, "PRESENT", confidence)
            self.last_save[student_id] = now
            print(f"Attendance marked: {student_id}")

        except Exception as e:
            print("Attendance error:", e)

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        try:
            faces = detect_faces(img)
            current = {}

            for face in faces:
                try:
                    current_embedding = get_embedding(face)
                except Exception:
                    continue

                best_student = None
                best_score = 0.0

                for student in self.students:
                    try:
                        score = face_similarity(current_embedding, student["embedding"])
                    except Exception:
                        continue

                    if score > best_score:
                        best_score = score
                        best_student = student

                if best_student is not None and best_score >= self.threshold:
                    student_id = best_student["student_id"]
                    name = best_student["name"]
                    course = best_student["course"]

                    current[student_id] = {
                        "student_id": student_id,
                        "name": name,
                        "course": course,
                        "confidence": best_score
                    }

                    self.save_attendance(student_id, best_score)

                    with self.lock:
                        if self.recognition_time == 0:
                            self.recognition_time = time.time()

                    img = draw_face_box(
                        img, face, f"{name} | PRESENT", best_score,
                        self.PRESENT_COLOR_BGR
                    )

                else:
                    img = draw_face_box(
                        img, face, "UNKNOWN", best_score,
                        self.UNKNOWN_COLOR_BGR
                    )

            with self.lock:
                self.recognized_students = current

            with self.lock:
                if (
                    self.recognition_time > 0
                    and (time.time() - self.recognition_time) >= self.auto_stop_seconds
                ):
                    self.should_stop = True

        except Exception as e:
            print("Frame processing error:", e)
            cv2.putText(
                img, "Face processing error", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, self.UNKNOWN_COLOR_BGR, 2
            )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="mark">🎓</div>
            <div>
                <div class="name">Smart Attendance System</div>
                <div class="tag">Face-recognition system</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "MENU",
        [
            "🏠 Dashboard",
            "🧾 Register Student",
            "🎥 Live Attendance",
            "🗂️ Students",
            "📋 Attendance",
            "📈 Analytics",
        ],
        label_visibility="collapsed"
    )

    page = page.split(" ", 1)[1]

    st.divider()
    st.caption("Real-Time Face Recognition")


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    render_hero(
        "Overview",
        "Attendance Dashboard",
        "Today's student attendance, at a glance.",
        accent=PAGE_ACCENTS["Dashboard"]
    )

    students = get_students()
    attendance = get_attendance()

    total = len(students)
    today = datetime.now().strftime("%Y-%m-%d")

    today_records = [row for row in attendance if str(row[2]) == today]

    present_ids = set(
        str(row[1]) for row in today_records
        if str(row[4]).upper() == "PRESENT"
    )

    present = len(present_ids)
    absent = max(total - present, 0)
    percentage = (present / total * 100) if total > 0 else 0

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Total Students", total)
    with c2:
        st.metric("🟢 Present Today", present)
    with c3:
        st.metric("🔴 Absent Today", absent)
    with c4:
        st.metric("📈 Attendance Rate", f"{percentage:.1f}%")

    st.divider()
    st.subheader("Today's Student Status")

    rows = []
    for student in students:
        info = get_student_info(student)
        student_id = str(info["student_id"])
        status = "🟢 PRESENT" if student_id in present_ids else "🔴 ABSENT"

        rows.append({
            "Student Name": info["name"],
            "Student ID": info["student_id"],
            "Course": info["course"],
            "Status": status
        })

    if rows:
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    else:
        st.info("No students registered yet.")


# ============================================================
# REGISTER STUDENT
# ============================================================

elif page == "Register Student":

    render_hero(
        "Enrollment",
        "Student Registration",
        "Register student information and enroll their face.",
        accent=PAGE_ACCENTS["Register Student"]
    )

    left, right = st.columns(2)

    with left:
        st.subheader("👤 Student Details")

        name = st.text_input("Student Name", placeholder="Enter student name")
        student_id = st.text_input("Student ID", placeholder="Example: DS001")
        phone = st.text_input("Phone Number", placeholder="Enter phone number")
        course = st.selectbox("Course", COURSE_OPTIONS)

    with right:
        st.subheader("📷 Face Enrollment")

        with st.container(key="cam_scan_register"):
            st.markdown(
                """
                <div class="cam-scan-label">
                    <span class="dot"></span>
                    Enrollment Scanner
                </div>
                """,
                unsafe_allow_html=True
            )

            if not st.session_state.registration_camera:
                st.info("Camera is currently closed.")

                if st.button("📷 START CAMERA", use_container_width=True):
                    st.session_state.registration_camera = True
                    st.rerun()

            else:
                st.success("📷 Camera is ON")
                camera_photo = st.camera_input("Take Student Face Photo")

                if camera_photo:
                    image = Image.open(io.BytesIO(camera_photo.getvalue())).convert("RGB")
                    st.image(image, caption="Captured Student Face", width=320)

                if st.button("❌ CLOSE CAMERA", use_container_width=True):
                    st.session_state.registration_camera = False
                    st.rerun()

    st.divider()

    if st.button("➕ REGISTER STUDENT", type="primary", use_container_width=True):

        name = name.strip()
        student_id = student_id.strip()
        phone = phone.strip()

        if not name:
            st.error("Enter student name.")
            st.stop()

        if not student_id:
            st.error("Enter Student ID.")
            st.stop()

        if not phone:
            st.error("Enter phone number.")
            st.stop()

        if not st.session_state.registration_camera:
            st.error("Click START CAMERA first.")
            st.stop()

        if camera_photo is None:
            st.error("Capture student's face first.")
            st.stop()

        if student_exists(student_id):
            st.error("Student ID already exists.")
            st.stop()

        image = Image.open(io.BytesIO(camera_photo.getvalue())).convert("RGB")
        frame = np.array(image)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        with st.spinner("Detecting face..."):
            faces = detect_faces(frame)

        if len(faces) == 0:
            st.error("❌ No face detected.")
            st.stop()

        if len(faces) > 1:
            st.error("❌ Multiple faces detected.")
            st.warning("Only ONE student face is allowed during registration.")
            st.stop()

        face = faces[0]

        with st.spinner("Creating face embedding..."):
            embedding = get_embedding(face)

        image_name = student_id.replace(" ", "_") + ".jpg"
        image_path = os.path.join(FACE_FOLDER, image_name)
        image.save(image_path, "JPEG", quality=95)

        embedding_string = ",".join(map(str, embedding.tolist()))

        try:
            # NOTE: passing phone= as a kwarg matches the existing
            # add_student() signature used throughout this project.
            add_student(
                student_id=student_id,
                name=name,
                course=course,
                phone=phone,
                embedding=embedding_string,
                image_path=image_path,
                created_at=datetime.now().isoformat()
            )

            ensure_phone_column()

            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET phone = ? WHERE student_id = ?",
                (phone, student_id)
            )
            conn.commit()
            conn.close()

            st.success("✅ Student registered successfully!")
            st.success("✅ Face enrolled successfully!")

            st.write(f"**Name:** {name}")
            st.write(f"**Student ID:** {student_id}")
            st.write(f"**Phone:** {phone}")
            st.write(f"**Course:** {course}")

            st.session_state.registration_camera = False
            st.balloons()

        except Exception as e:
            st.error(f"Database error: {e}")


# ============================================================
# LIVE ATTENDANCE — AUTO STOP AFTER 15 SECONDS
# ============================================================

elif page == "Live Attendance":

    render_hero(
        "Recognition",
        "Live Attendance",
        "Start camera → Face recognition → Automatic attendance.",
        accent=PAGE_ACCENTS["Live Attendance"]
    )

    for key, default in {
        "camera_running": False,
        "camera_start_time": None,
        "camera_session_id": 0,
        "recognized_result": {},
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    face_database = build_face_database()

    if not face_database:
        st.warning("No students registered yet.")
        st.info("Please register at least one student with a face from Register Student.")
        st.stop()

    st.success(f"✅ {len(face_database)} student(s) ready for recognition")
    st.write("Click **START CAMERA**. The camera will automatically stop after 15 seconds.")

    if not st.session_state.camera_running:
        if st.button("▶️ START CAMERA", type="primary", use_container_width=True):
            st.session_state.camera_running = True
            st.session_state.camera_start_time = time.time()
            st.session_state.camera_session_id += 1
            st.session_state.recognized_result = {}
            st.rerun()

    if st.session_state.camera_running:

        # ----------------------------------------------------
        # Drive the 15-second countdown with a lightweight
        # auto-refresh instead of a blocking time.sleep()+rerun
        # loop. This keeps the WebRTC video connection (tied to
        # a stable `camera_key`) alive and continuously streaming
        # for the full window, while still ticking the on-screen
        # timer and checking the auto-stop condition every 500ms.
        # ----------------------------------------------------

        st_autorefresh(
            interval=500,
            limit=None,
            key=f"live_attendance_tick_{st.session_state.camera_session_id}"
        )

        elapsed = time.time() - st.session_state.camera_start_time
        remaining = max(0, 15 - int(elapsed))

        # Camera already ran its full 15 seconds — stop it now,
        # before rendering the video widget again, and show the
        # results view. No auto-restart happens after this.
        if elapsed >= 15:
            st.session_state.camera_running = False
            st.session_state.camera_start_time = None
            st.success("✅ Camera automatically stopped after 15 seconds.")
            st.rerun()

        st.info(f"📷 Camera active — automatic stop in {remaining} second(s)")

        camera_key = "attendance_camera_" + str(st.session_state.camera_session_id)

        with st.container(key="cam_scan_live"):
            st.markdown(
                """
                <div class="cam-scan-label">
                    <span class="dot"></span>
                    Live Recognition Scanner
                </div>
                """,
                unsafe_allow_html=True
            )

            ctx = webrtc_streamer(
                key=camera_key,
                mode=WebRtcMode.SENDRECV,
                video_processor_factory=AttendanceVideoProcessor,
                media_stream_constraints={"video": True, "audio": False},
                async_processing=True
            )

        if ctx.video_processor:
            ctx.video_processor.update_students(face_database)

        st.divider()
        st.subheader("🟢 Attendance Result")

        if ctx.video_processor:
            with ctx.video_processor.lock:
                recognized = dict(ctx.video_processor.recognized_students)

            if recognized:
                for student in recognized.values():
                    st.success(f"🟢 {student['name']} — PRESENT")
                    st.write(f"Course: {student['course']}")
                    st.write(f"Confidence: {student['confidence'] * 100:.1f}%")
                    st.session_state.recognized_result = recognized
            else:
                st.info("🔍 Looking for registered face...")

    else:
        if st.session_state.recognized_result:
            st.success("✅ Attendance completed automatically.")
            st.subheader("Recognized Student(s)")

            for student in st.session_state.recognized_result.values():
                st.success(f"🟢 {student['name']} — PRESENT")
        else:
            st.info("Click START CAMERA to begin attendance.")


# ============================================================
# STUDENTS — directory with View / Edit / Delete
# ============================================================

elif page == "Students":

    render_hero(
        "Directory",
        "Students",
        "Everyone currently enrolled — view, edit, or remove a record.",
        accent=PAGE_ACCENTS["Students"]
    )

    students = get_students()

    if not students:
        st.info("No students registered.")
        st.stop()

    schema_columns = get_student_columns()

    # ---------------- toolbar ----------------

    tc1, tc2 = st.columns([3, 1])

    with tc1:
        search_query = st.text_input(
            "Search",
            value=st.session_state.student_search,
            placeholder="Search by name, Student ID, or course...",
            label_visibility="collapsed"
        )
        st.session_state.student_search = search_query

    with tc2:
        st.metric("Total Enrolled", len(students))

    infos = [get_student_info(s) for s in students]

    if search_query.strip():
        q = search_query.strip().lower()
        infos = [
            info for info in infos
            if q in str(info["name"]).lower()
            or q in str(info["student_id"]).lower()
            or q in str(info["course"]).lower()
        ]

    st.caption(f"{len(infos)} student(s) shown")
    st.write("")

    if not infos:
        st.info("No students match your search.")

    for info in infos:

        sid = str(info["student_id"])
        is_editing = st.session_state.editing_student_id == sid
        is_viewing = st.session_state.viewing_student_id == sid
        is_deleting = st.session_state.delete_confirm_id == sid

        with st.container(key=f"student_card_{sid}"):

            row = st.columns([0.6, 2.6, 1.6, 1.6, 1.8, 0.8, 0.8, 0.8])

            with row[0]:
                st.markdown(render_avatar(info["name"]), unsafe_allow_html=True)

            with row[1]:
                st.markdown(
                    f'<div class="student-name">{info["name"]}</div>'
                    f'<div class="student-sub">ID: {info["student_id"]}</div>',
                    unsafe_allow_html=True
                )

            with row[2]:
                st.markdown(
                    f'<span class="chip chip-course">📚 {info["course"] or "—"}</span>',
                    unsafe_allow_html=True
                )

            with row[3]:
                st.markdown(f'<div class="student-sub">📞 {info["phone"] or "—"}</div>', unsafe_allow_html=True)

            with row[4]:
                created = str(info["created_at"] or "—")[:10]
                st.markdown(f'<div class="student-sub">🗓️ {created}</div>', unsafe_allow_html=True)

            with row[5]:
                if st.button("👁", key=f"view_{sid}", help="View details", use_container_width=True):
                    st.session_state.viewing_student_id = None if is_viewing else sid
                    st.session_state.editing_student_id = None
                    st.session_state.delete_confirm_id = None
                    st.rerun()

            with row[6]:
                if st.button("✏️", key=f"edit_{sid}", help="Edit student", use_container_width=True):
                    st.session_state.editing_student_id = None if is_editing else sid
                    st.session_state.viewing_student_id = None
                    st.session_state.delete_confirm_id = None
                    st.rerun()

            with row[7]:
                if st.button("🗑️", key=f"delete_{sid}", help="Delete student", use_container_width=True):
                    st.session_state.delete_confirm_id = None if is_deleting else sid
                    st.session_state.editing_student_id = None
                    st.session_state.viewing_student_id = None
                    st.rerun()

            # ---------------- VIEW PANEL ----------------

            if is_viewing:
                st.divider()

                vc1, vc2 = st.columns([1, 3])

                with vc1:
                    image_path = info.get("image_path")
                    if image_path and os.path.exists(str(image_path)):
                        st.image(str(image_path), width=140)
                    else:
                        st.markdown(
                            f'<div style="width:120px;">{render_avatar(info["name"])}</div>',
                            unsafe_allow_html=True
                        )

                with vc2:
                    st.write(f"**Full Name:** {info['name']}")
                    st.write(f"**Student ID:** {info['student_id']}")
                    st.write(f"**Phone:** {info['phone'] or '—'}")
                    st.write(f"**Course:** {info['course'] or '—'}")

                    for col_key, label in [
                        ("department", "Department"), ("semester", "Semester"),
                        ("division", "Division"), ("roll_number", "Roll Number"),
                        ("academic_year", "Academic Year"),
                    ]:
                        if col_key in schema_columns and info.get(col_key):
                            st.write(f"**{label}:** {info[col_key]}")

                    st.write(f"**Registered:** {info['created_at'] or '—'}")

                if st.button("Close", key=f"close_view_{sid}"):
                    st.session_state.viewing_student_id = None
                    st.rerun()

            # ---------------- EDIT PANEL ----------------

            if is_editing:
                with st.container(key=f"edit_panel_{sid}"):
                    st.markdown("**✏️ Edit Student Details**")

                    ec1, ec2 = st.columns(2)

                    with ec1:
                        new_student_id = st.text_input(
                            "Student ID", value=str(info["student_id"]),
                            key=f"in_sid_{sid}"
                        )
                        new_name = st.text_input(
                            "Full Name", value=str(info["name"]),
                            key=f"in_name_{sid}"
                        )
                        new_phone = st.text_input(
                            "Phone Number", value=str(info["phone"] or ""),
                            key=f"in_phone_{sid}"
                        )

                    with ec2:
                        course_value = str(info["course"] or COURSE_OPTIONS[0])
                        course_index = (
                            COURSE_OPTIONS.index(course_value)
                            if course_value in COURSE_OPTIONS else 0
                        )
                        new_course = st.selectbox(
                            "Course", COURSE_OPTIONS, index=course_index,
                            key=f"in_course_{sid}"
                        )

                        extra_values = {}
                        for col_key, label in [
                            ("department", "Department"), ("semester", "Semester"),
                            ("division", "Division"), ("roll_number", "Roll Number"),
                            ("academic_year", "Academic Year"),
                        ]:
                            if col_key in schema_columns:
                                extra_values[col_key] = st.text_input(
                                    label, value=str(info.get(col_key) or ""),
                                    key=f"in_{col_key}_{sid}"
                                )

                    st.write("")
                    sc1, sc2, _ = st.columns([1, 1, 3])

                    with sc1:
                        save_clicked = st.button(
                            "💾 Save Changes", key=f"save_{sid}",
                            type="primary", use_container_width=True
                        )

                    with sc2:
                        with st.container(key=f"ghost_cancel_{sid}"):
                            cancel_clicked = st.button(
                                "Cancel", key=f"cancel_{sid}", use_container_width=True
                            )

                    if cancel_clicked:
                        st.session_state.editing_student_id = None
                        st.rerun()

                    if save_clicked:
                        new_student_id = new_student_id.strip()
                        new_name = new_name.strip()
                        new_phone = new_phone.strip()

                        if not new_name:
                            st.error("Name cannot be empty.")
                            st.stop()

                        if not new_student_id:
                            st.error("Student ID cannot be empty.")
                            st.stop()

                        if new_student_id != sid and student_exists(new_student_id):
                            st.error("That Student ID is already in use by another student.")
                            st.stop()

                        field_values = {
                            "name": new_name,
                            "phone": new_phone,
                            "course": new_course,
                        }
                        field_values.update(extra_values)

                        ok, err = update_student_record(sid, new_student_id, field_values)

                        if ok:
                            st.success("✅ Student details updated.")
                            st.session_state.editing_student_id = None
                            st.rerun()
                        else:
                            st.error(f"Update failed: {err}")

            # ---------------- DELETE CONFIRM PANEL ----------------

            if is_deleting:
                with st.container(key=f"delete_panel_{sid}"):
                    st.markdown(
                        f"⚠️ **Delete {info['name']} ({info['student_id']})?** "
                        "This permanently removes their profile and attendance history."
                    )

                    dc1, dc2, _ = st.columns([1, 1, 3])

                    with dc1:
                        with st.container(key=f"danger_confirm_{sid}"):
                            confirm_clicked = st.button(
                                "🗑️ Confirm Delete", key=f"confirm_delete_{sid}",
                                use_container_width=True
                            )

                    with dc2:
                        with st.container(key=f"ghost_cancel_del_{sid}"):
                            cancel_del_clicked = st.button(
                                "Cancel", key=f"cancel_delete_{sid}", use_container_width=True
                            )

                    if cancel_del_clicked:
                        st.session_state.delete_confirm_id = None
                        st.rerun()

                    if confirm_clicked:
                        ok, err = delete_student_record(sid, image_path=info.get("image_path"))

                        if ok:
                            st.success(f"🗑️ {info['name']} was deleted.")
                            st.session_state.delete_confirm_id = None
                            st.rerun()
                        else:
                            st.error(f"Delete failed: {err}")


# ============================================================
# ATTENDANCE
# ============================================================

elif page == "Attendance":

    render_hero(
        "Records",
        "Attendance",
        "Full attendance log, exportable as CSV.",
        accent=PAGE_ACCENTS["Attendance"]
    )

    attendance = get_attendance()
    students = get_students()

    name_map = {}
    for student in students:
        info = get_student_info(student)
        name_map[str(info["student_id"])] = info["name"]

    if not attendance:
        st.info("No attendance records.")

    else:
        rows = []
        for row in attendance:
            student_id = str(row[1])
            student_name = name_map.get(student_id, "Unknown Student")

            rows.append({
                "Student Name": student_name,
                "Student ID": student_id,
                "Date": row[2],
                "Time": row[3],
                "Status": row[4],
                "Confidence": f"{safe_float(row[5]) * 100:.1f}%"
            })

        df = pd.DataFrame(rows)

        f1, f2 = st.columns([2, 1])
        with f1:
            name_filter = st.text_input(
                "Filter by name or ID", placeholder="Type to filter records..."
            )
        with f2:
            date_options = ["All dates"] + sorted(df["Date"].unique().tolist(), reverse=True)
            date_filter = st.selectbox("Date", date_options)

        filtered = df.copy()
        if name_filter.strip():
            q = name_filter.strip().lower()
            filtered = filtered[
                filtered["Student Name"].str.lower().str.contains(q)
                | filtered["Student ID"].str.lower().str.contains(q)
            ]
        if date_filter != "All dates":
            filtered = filtered[filtered["Date"] == date_filter]

        st.caption(f"{len(filtered)} record(s)")
        st.dataframe(filtered, use_container_width=True, hide_index=True)

        csv_data = filtered.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Attendance CSV",
            data=csv_data,
            file_name="attendance.csv",
            mime="text/csv",
            use_container_width=True
        )


# ============================================================
# ANALYTICS
# ============================================================

elif page == "Analytics":

    render_hero(
        "Insights",
        "Attendance Analytics",
        "Trends across days and students.",
        accent=PAGE_ACCENTS["Analytics"]
    )

    students = get_students()
    attendance = get_attendance()
    total = len(students)

    if not attendance:
        st.info("No attendance data yet.")

    else:
        df = pd.DataFrame(
            attendance,
            columns=["ID", "Student_ID", "Date", "Time", "Status", "Confidence"]
        )

        name_map = {}
        for student in students:
            info = get_student_info(student)
            name_map[str(info["student_id"])] = info["name"]

        df["Student Name"] = (
            df["Student_ID"].astype(str).map(name_map).fillna("Unknown Student")
        )

        present_records = df[df["Status"] == "PRESENT"]

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Total Students", total)
        with c2:
            st.metric("Present Records", len(present_records))
        with c3:
            st.metric("Attendance Days", df["Date"].nunique())

        st.divider()

        daily = (
            present_records.groupby("Date").size()
            .reset_index(name="Present Students")
        )

        if not daily.empty:
            st.subheader("📊 Daily Attendance")
            st.bar_chart(daily.set_index("Date"), color="#14B8A6")

        summary = (
            present_records.groupby("Student Name").size()
            .reset_index(name="Present Days")
            .sort_values("Present Days", ascending=False)
        )

        if not summary.empty:
            st.subheader("👥 Student Attendance")
            st.dataframe(summary, use_container_width=True, hide_index=True)