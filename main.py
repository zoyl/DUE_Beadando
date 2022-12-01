import tkinter as tk
import functions as fc

FONT = ("calbri", 20, "bold")


class KeyGeneratorGUI:
    def __init__(self, master):
        master.title("Key generator")
        self.plaintext = tk.StringVar(master, value="")

        # Plaintext controls
        tk.Label(master, text="Seed", fg="green", font=FONT).grid(row=0, column=0)
        self.plain_entry = tk.Entry(master, textvariable=self.plaintext, width=50, font=FONT)
        self.plain_entry.grid(row=0, column=1, padx=20)
        tk.Button(master, text="Encrypt", command=lambda: self.encrypt_callback(), font=FONT).grid(row=0, column=2)

    def encrypt_callback(self):
        key = fc.generate_key()
        privatekey = fc.private_key(self.plain_entry.get(), key)
        publickey = fc.public_key(self.plain_entry.get(), key)
        file_priv = open("private.pem", "wb")
        file_priv.write(privatekey)
        file_priv.close()
        file_pub = open("receiver.pem", "wb")
        file_pub.write(publickey)
        file_pub.close()


if __name__ == "__main__":
    root = tk.Tk()
    keygen = KeyGeneratorGUI(root)
    root.mainloop()
