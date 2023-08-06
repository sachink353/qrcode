import qrcode

def generate_qr_code(data, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image to a file
    qr_image.save(filename)

if __name__ == "__main__":
    # Example usage: Generate a QR code for a URL and save it as "qr_code.png"
    data = "https://sachink353.github.io/SachinTech.notes/"
    filename = "qr_code.png"
    generate_qr_code(data, filename)
