from PIL import Image

# Specify the file path
file_path = "qr_code (1).txt"

# Create a new white image with a size of 100x100 pixels
width, height = 100, 100
image = Image.new("1", (width, height), 1)  # "1" mode for 1-bit pixels, with initial white pixels (1)

try:
    with open(file_path, "r") as file:
        for y, line in enumerate(file):
            # Remove leading and trailing whitespace (including newline characters)
            line = line.strip()

            try:
                # Convert the line content to an integer
                number = int(line)

                # Convert the integer to binary
                binary_representation = bin(number)[2:].zfill(width)  # Pad with zeros to match the image width

                # Set the pixel colors in the image based on the binary representation
                for x, bit in enumerate(binary_representation):
                    pixel_color = 0 if bit == '0' else 1
                    image.putpixel((x, y), pixel_color)

            except ValueError:
                # Handle the case where the line does not contain a valid number
                print(f"Skipping invalid line: {line}")

    # Save the bitmap image
    image.save("output.bmp")
    print("Bitmap image saved as 'output.bmp'.")

except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
