import subprocess
import json
import hashlib
from PIL import Image, ImageChops, ImageEnhance
import os


def extract_metadata(image_path):
    try:
        # Run the exiftool command to get metadata in JSON format
        process = subprocess.run(['exiftool', '-j', image_path], capture_output=True, text=True)
        # Parse the JSON output from exiftool
        metadata = json.loads(process.stdout)[0]
        return {
            "ImageWidth": metadata.get("ImageWidth", "Not available"),
            "ImageLength": metadata.get("ImageLength", "Not available"),
            "DateTime": metadata.get("DateTimeOriginal", "Not available"),
            "YCbCrPositioning": metadata.get("YCbCrPositioning", "Not available"),
            "ExifOffset": metadata.get("ExifOffset", "Not available"),
            "ResolutionUnit": metadata.get("ResolutionUnit", "Not available"),
            "GPSInfo": metadata.get("GPSInfo", "No GPS info"),
            "XResolution": metadata.get("XResolution", "Not available"),
            "YResolution": metadata.get("YResolution", "Not available"),
            "Make": metadata.get("Make", "Not available"),
            "Model": metadata.get("Model", "Not available"),
            "ISOSpeedRatings": metadata.get("ISOSpeedRatings", "Not available"),
            "ExposureProgram": metadata.get("ExposureProgram", "Not available"),
            "FNumber": metadata.get("FNumber", "Not available"),
            "ExposureTime": metadata.get("ExposureTime", "Not available"),
            "SensingMethod": metadata.get("SensingMethod", "Not available"),
            "SubSecTimeDigitized": metadata.get("SubSecTimeDigitized", "Not available"),
            "MakerNote": metadata.get("MakerNote", "Not available")
        }
    except Exception as e:
        return {"error": f"Error extracting metadata: {str(e)}"}


# Function to calculate the SHA-256 hash of an image
def calculate_image_hash(image_path):
    try:
        sha256_hash = hashlib.sha256()
        with open(image_path, "rb") as f:
            while chunk := f.read(4096):  # Read the file in chunks
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()  # Return the hex digest (hash)
    except Exception as e:
        return f"Error calculating hash: {str(e)}"

# Function to perform Error Level Analysis (ELA) for tampering detection
def error_level_analysis(image_path):
    try:
        # Open the original image
        original_image = Image.open(image_path)
        
        # Ensure the 'uploads' directory exists
        if not os.path.exists('uploads'):
            os.makedirs('uploads')

        # Path to save the ELA output
        ela_image_path = f"uploads/ela_{os.path.basename(image_path)}"
        
        # Save the image at 95% quality to see compression artifacts
        compressed_image_path = f"uploads/compressed_{os.path.basename(image_path)}"
        original_image.save(compressed_image_path, "JPEG", quality=95)
        
        # Reopen the compressed image and calculate the difference
        compressed_image = Image.open(compressed_image_path)
        ela_image = ImageChops.difference(original_image, compressed_image)
        
        # Enhance the difference to make it more visible
        extrema = ela_image.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        scale = 255.0 / max_diff if max_diff != 0 else 1
        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
        
        # Save the ELA image
        ela_image.save(ela_image_path)

        return ela_image_path
    except Exception as e:
        return f"Error performing ELA: {str(e)}"
