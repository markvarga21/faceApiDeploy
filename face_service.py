from utils import convert_filestorage_to_cv2_image
from deepface import DeepFace as df

def validate_faces(id_image, selfie_image):
    """A method for validating two images"""
    cv2_id_image = convert_filestorage_to_cv2_image(id_image)
    cv2_selfie_image = convert_filestorage_to_cv2_image(selfie_image)

    result = df.verify(cv2_id_image, cv2_selfie_image)
    ret = {
        'isValid': bool(result['verified']),
        'proba': round(float(1-result['distance']), 2)
    }

    return ret