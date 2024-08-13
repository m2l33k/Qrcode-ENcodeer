import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

class QRCodeEncoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Encoder")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Text Entry
        self.text_label = tk.Label(self.root, text="Enter text to encode:", font=('Helvetica', 12))
        self.text_label.pack(pady=10)

        self.text_var = tk.StringVar()
        self.text_entry = tk.Entry(self.root, textvariable=self.text_var, font=('Helvetica', 14))
        self.text_entry.pack(pady=10, padx=20, fill=tk.X)

        # Generate QR Code Button
        self.generate_button = tk.Button(self.root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=20)

        # Display QR Code
        self.qr_image_label = tk.Label(self.root)
        self.qr_image_label.pack(pady=20)

    def generate_qr_code(self):
        text = self.text_var.get()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to encode.")
            return

        try:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')

            # Convert QR code to Tkinter-compatible image
            img_tk = ImageTk.PhotoImage(img)
            self.qr_image_label.config(image=img_tk)
            self.qr_image_label.image = img_tk

        except Exception as e:
            messagebox.showerror("Generation Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeEncoderApp(root)
    root.mainloop()
