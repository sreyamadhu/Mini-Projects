import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.units import inch
import webbrowser
import os

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Generator")

        self.products = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Product Name").grid(row=0, column=0)
        tk.Label(self.root, text="Quantity").grid(row=0, column=1)
        tk.Label(self.root, text="Amount per Unit").grid(row=0, column=2)

        self.product_name = tk.Entry(self.root)
        self.product_name.grid(row=1, column=0)
        self.quantity = tk.Entry(self.root)
        self.quantity.grid(row=1, column=1)
        self.amount = tk.Entry(self.root)
        self.amount.grid(row=1, column=2)

        tk.Button(self.root, text="Add Product", command=self.add_product).grid(row=1, column=3)
        tk.Button(self.root, text="Generate Bill", command=self.generate_bill).grid(row=2, columnspan=4)

        self.product_listbox = tk.Listbox(self.root, width=50)
        self.product_listbox.grid(row=3, columnspan=4)

    def add_product(self):
        product_name = self.product_name.get()
        quantity = self.quantity.get()
        amount = self.amount.get()

        if not product_name or not quantity or not amount:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        try:
            quantity = int(quantity)
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Input Error", "Quantity must be an integer and Amount must be a float")
            return

        total = quantity * amount
        self.products.append([product_name, quantity, f"${amount:.2f}", f"${total:.2f}"])
        self.product_listbox.insert(tk.END, f"{product_name}: {quantity} x ${amount:.2f} = ${total:.2f}")

        self.product_name.delete(0, tk.END)
        self.quantity.delete(0, tk.END)
        self.amount.delete(0, tk.END)

    def generate_bill(self):
        if not self.products:
            messagebox.showwarning("Input Error", "No products added")
            return

        pdf_file = 'bill.pdf'
        document = SimpleDocTemplate(pdf_file, pagesize=A4)
        styles = getSampleStyleSheet()
        style_title = styles['Title']

        title = Paragraph("Bill Receipt", style_title)

        table_data = [['Product', 'Quantity', 'Amount per Unit', 'Total']]
        table_data.extend(self.products)

        total_amount = sum(float(item[3][1:]) for item in self.products)
        table_data.append(['', '', 'Total Amount', f"${total_amount:.2f}"])

        table = Table(table_data, hAlign='LEFT', colWidths=[2*inch, 1*inch, 1.5*inch, 1.5*inch])
        table.setStyle(TableStyle([


            ("BOX", (0,0), (-1, -1), 1, colors.black),
            ('GRID', (0, 0), (4, 4), 1, colors.black),
            ('BACKGROUND', (0, 0), (3, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]))

        footer = Paragraph("Thank you for your purchase!", styles['Normal'])

        elements = [title, table, footer]
        document.build(elements)

        messagebox.showinfo("Success", f"Bill generated and saved as {pdf_file}")

        # Open the generated PDF
        webbrowser.open('file://' + os.path.realpath(pdf_file))

if __name__ == "__main__":
    root = tk.Tk()
    app = BillApp(root)
    root.mainloop()
