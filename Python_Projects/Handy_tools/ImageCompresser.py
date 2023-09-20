from PIL import Image

def compress_image(input_path, output_path, quality=10):
    try:
        # Open the image file
        img = Image.open(input_path)

        # Compress and save the image with the specified quality
        img.save(output_path, optimize=True, quality=quality)

        print(f"Image compressed and saved as {output_path} with quality {quality}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_image_path = "NID_pic.jpeg"  # Replace with your input image file path
    output_image_path = "NID_pic_cmp.jpeg"  # Replace with your desired output file path
    compression_quality = 10  # Adjust the quality (0-100) as needed

    compress_image(input_image_path, output_image_path, compression_quality)
