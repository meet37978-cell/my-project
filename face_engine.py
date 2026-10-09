import cv2
import numpy as np

from insightface.app import FaceAnalysis


# =========================================================
# GLOBAL MODEL
# =========================================================

_model = None


# =========================================================
# LOAD FACE MODEL
# =========================================================

def load_face_model():

    global _model


    if _model is None:

        print(
            "Loading InsightFace model..."
        )


        _model = FaceAnalysis(

            name="buffalo_l",

            providers=[
                "CPUExecutionProvider"
            ]

        )


        _model.prepare(

            ctx_id=0,

            det_size=(
                640,
                640
            )

        )


        print(
            "InsightFace model loaded!"
        )


    return _model


# =========================================================
# DETECT FACES
# =========================================================

def detect_faces(
    frame
):

    model = load_face_model()


    faces = model.get(
        frame
    )


    return faces


# =========================================================
# GET FACE EMBEDDING
# =========================================================

def get_embedding(
    face
):

    embedding = face.embedding


    embedding = np.asarray(

        embedding,

        dtype=np.float32

    )


    norm = np.linalg.norm(
        embedding
    )


    if norm == 0:

        return embedding


    embedding = (
        embedding / norm
    )


    return embedding


# =========================================================
# FACE SIMILARITY
# =========================================================

def face_similarity(
    embedding1,
    embedding2
):

    embedding1 = np.asarray(

        embedding1,

        dtype=np.float32

    )


    embedding2 = np.asarray(

        embedding2,

        dtype=np.float32

    )


    norm1 = np.linalg.norm(
        embedding1
    )


    norm2 = np.linalg.norm(
        embedding2
    )


    if (
        norm1 == 0
        or norm2 == 0
    ):

        return 0.0


    embedding1 = (
        embedding1 / norm1
    )


    embedding2 = (
        embedding2 / norm2
    )


    similarity = np.dot(

        embedding1,

        embedding2

    )


    return float(
        similarity
    )


# =========================================================
# DRAW FACE
# =========================================================

def draw_face_box(

    frame,

    face,

    name,

    confidence,

    color

):

    box = face.bbox.astype(
        int
    )


    x1, y1, x2, y2 = box


    # -----------------------------------------------------
    # FACE BOX
    # -----------------------------------------------------

    cv2.rectangle(

        frame,

        (x1, y1),

        (x2, y2),

        color,

        3

    )


    # -----------------------------------------------------
    # LABEL
    # -----------------------------------------------------

    label = (

        f"{name} | "

        f"{confidence * 100:.1f}%"

    )


    text_y = max(
        y1 - 10,
        25
    )


    cv2.putText(

        frame,

        label,

        (x1, text_y),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.65,

        color,

        2,

        cv2.LINE_AA

    )


    return frame