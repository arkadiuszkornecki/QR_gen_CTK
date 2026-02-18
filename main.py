import qrcode
import customtkinter as ctk
from PIL import Image

class App:
    QR_SIZE = 325
    BG_COLOR = "#162440"
    FG_COLOR = "#ffffff"

    def __init__(self):
        self.qr_code_img = None
        ctk.set_appearance_mode("system")
        self.root = ctk.CTk()
        self.root.title("QR Code Generator")
        self.root.geometry("400x550")
        self.root.configure(fg_color=self.BG_COLOR)

        self.label = ctk.CTkLabel(
            self.root,
            text="QR Code Generator",
            font=("Arial", 25, "bold"),
            text_color=self.FG_COLOR,
            fg_color="transparent",
        )
        self.label.place(relx=0.5, y=15, anchor="n")

        self.label2 = ctk.CTkLabel(
            self.root,
            text="Enter the link:",
            font=("Arial", 15, "bold"),
            text_color=self.FG_COLOR,
            fg_color="transparent",
        )
        self.label2.place(x=40, y=70)

        self.link = ctk.CTkEntry(self.root, width=300, font=("Arial", 15))
        self.link.place(x=40, y=100)

        self.btn = ctk.CTkButton(
            self.root,
            text="Generate",
            font=("Arial", 12, "bold"),
            command=self.generate_qr,
            corner_radius=10,
            border_width=2,
            border_color=self.FG_COLOR,
            hover_color=self.BG_COLOR,
        )
        self.btn.place(x=40, y=140)

        self.label3 = ctk.CTkLabel(self.root, text="", fg_color="transparent")
        self.label3.place(relx=0.5, y=200, anchor="n")


    def generate_qr(self):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(self.link.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        img = img.resize((self.QR_SIZE, self.QR_SIZE), Image.NEAREST)
        self.qr_code_img = ctk.CTkImage(
            light_image=img,
            dark_image=img,
            size=(self.QR_SIZE, self.QR_SIZE),
        )
        self.label3.configure(image=self.qr_code_img)

if __name__ == "__main__":
    app = App()
    app.root.mainloop()
