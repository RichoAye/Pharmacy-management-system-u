import json
from tkinter import *
from tkinter import messagebox, filedialog

# Initializing the main window
root = Tk()
root.title("Simple Pharmacy Management System")
root.configure(width=1500, height=600, bg='BLACK')

# List to store drugs
drugs = []
sales = []

def open_main_window():
    main_window = root

    def adddrug():
        drug = (entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get())
        drugs.append(drug)
        cleardrug()

    def open_delete_window():
        delete_window = Toplevel(main_window)
        delete_window.title("Delete Drug")

        def deletedrug():
            e1 = entry_delete.get().strip().lower()
            global drugs
            for drug in drugs:
                if drug[0].strip().lower() == e1:
                    drug_name = drug[0]
                    drugs.remove(drug)
                    messagebox.showinfo("Message", f"{drug_name} deleted successfully")
                    break
            else:
                messagebox.showinfo("Message", "Drug not found")

        label_delete = Label(delete_window, text="ENTER DRUG NAME TO DELETE", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry_delete = Entry(delete_window, font=("Times", 12))
        button_delete = Button(delete_window, text="DELETE DRUG", bg="white", fg="black", width=20, font=("Times", 12), command=deletedrug)

        label_delete.grid(row=0, column=0, padx=10, pady=10)
        entry_delete.grid(row=0, column=1, padx=10, pady=10)
        button_delete.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def open_search_window():
        search_window = Toplevel(main_window)
        search_window.title("Search Drug")

        def searchdrug():
            e1 = entry_search.get().strip().lower()
            for drug in drugs:
                if e1 == drug[0].strip().lower():
                    set_entries(drug)
                    messagebox.showinfo("Title", f"{drug[0]} found")
                    break
            else:
                messagebox.showinfo("Title", "Drug not found")
            

        label_search = Label(search_window, text="ENTER DRUG NAME TO SEARCH", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry_search = Entry(search_window, font=("Times", 12))
        button_search = Button(search_window, text="SEARCH DRUG", bg="white", fg="black", width=20, font=("Times", 12), command=searchdrug)

        label_search.grid(row=0, column=0, padx=10, pady=10)
        entry_search.grid(row=0, column=1, padx=10, pady=10)
        button_search.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def open_update_window():
        update_window = Toplevel(main_window)
        update_window.title("Update Drug")

        def updatedrug():
            drug_name = entry_update_name.get().strip().lower()
            new_price = entry_update_price.get().strip()
            for i, drug in enumerate(drugs):
                if drug_name == drug[0].strip().lower():
                    drugs[i] = (drug[0], new_price, drug[2], drug[3], drug[4], drug[5])
                    messagebox.showinfo("Title", f"{drug[0]} updated successfully")
                    break
            else:
                messagebox.showinfo("Title", "Drug not found")
            update_window.destroy()

        label_update_name = Label(update_window, text="ENTER DRUG NAME TO UPDATE", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry_update_name = Entry(update_window, font=("Times", 12))
        label_update_price = Label(update_window, text="ENTER NEW DRUG PRICE", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry_update_price = Entry(update_window, font=("Times", 12))
        button_update = Button(update_window, text="UPDATE DRUG", bg="white", fg="black", width=20, font=("Times", 12), command=updatedrug)

        label_update_name.grid(row=0, column=0, padx=10, pady=10)
        entry_update_name.grid(row=0, column=1, padx=10, pady=10)
        label_update_price.grid(row=1, column=0, padx=10, pady=10)
        entry_update_price.grid(row=1, column=1, padx=10, pady=10)
        button_update.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def cleardrug():
        for entry in [entry1, entry2, entry3, entry4, entry5, entry6]:
            entry.delete(0, END)

    def listdrugs():
        new_window = Toplevel(main_window)
        new_window.title("Available Drugs")

        text = Text(new_window, wrap=NONE, width=100, height=20)
        text.grid(row=0, column=0, sticky=NSEW)

        scrollbar_y = Scrollbar(new_window, orient=VERTICAL, command=text.yview)
        scrollbar_y.grid(row=0, column=1, sticky=NS)
        scrollbar_x = Scrollbar(new_window, orient=HORIZONTAL, command=text.xview)
        scrollbar_x.grid(row=1, column=0, sticky=EW)

        text.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        headers = ("Drug Name", "Drug Price", "Drug Quantity", "Drug Category", "Drug Validity Duration", "Batch Number")
        text.insert(END, "{:<20} {:<15} {:<15} {:<20} {:<25} {:<15}\n".format(*headers))
        text.insert(END, "-" * 120 + "\n")

        for drug in drugs:
            text.insert(END, "{:<20} {:<15} {:<15} {:<20} {:<25} {:<15}\n".format(*drug))

    def set_entries(values):
        for entry, value in zip([entry1, entry2, entry3, entry4, entry5, entry6], values):
            entry.delete(0, END)
            entry.insert(0, value)

    def open_sales_window():
        sales_window = Toplevel(main_window)
        sales_window.title("Sales Transaction")

        def record_sale():
            drug_name = entry_drug_name.get().strip().lower()
            quantity_sold = int(entry_quantity_sold.get().strip())
            for drug in drugs:
                if drug_name == drug[0].strip().lower():
                    current_quantity = int(drug[2])
                    if quantity_sold <= current_quantity:
                        new_quantity = current_quantity - quantity_sold
                        drugs[drugs.index(drug)] = (drug[0], drug[1], str(new_quantity), drug[3], drug[4], drug[5])
                        sales.append((drug[0], drug[1], quantity_sold, drug[3], drug[4], drug[5]))
                        messagebox.showinfo("Sales", "Sale recorded successfully")
                        sales_window.destroy()
                        break
                    else:
                        messagebox.showerror("Sales", "Insufficient quantity available")
                        break
            else:
                messagebox.showerror("Sales", "Drug not found")

        label_drug_name = Label(sales_window, text="Drug Name", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry_drug_name = Entry(sales_window, font=("Times", 12))
        label_quantity_sold = Label(sales_window, text="Quantity Sold", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry_quantity_sold = Entry(sales_window, font=("Times", 12))
        button_record_sale = Button(sales_window, text="Record Sale", bg="white", fg="black", width=20, font=("Times", 12), command=record_sale)

        label_drug_name.grid(row=0, column=0, padx=10, pady=10)
        entry_drug_name.grid(row=0, column=1, padx=10, pady=10)
        label_quantity_sold.grid(row=1, column=0, padx=10, pady=10)
        entry_quantity_sold.grid(row=1, column=1, padx=10, pady=10)
        button_record_sale.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def list_sales():
        new_window = Toplevel(main_window)
        new_window.title("Sales History")

        text = Text(new_window, wrap=NONE, width=100, height=20)
        text.grid(row=0, column=0, sticky=NSEW)

        scrollbar_y = Scrollbar(new_window, orient=VERTICAL, command=text.yview)
        scrollbar_y.grid(row=0, column=1, sticky=NS)
        scrollbar_x = Scrollbar(new_window, orient=HORIZONTAL, command=text.xview)
        scrollbar_x.grid(row=1, column=0, sticky=EW)

        text.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        headers = ("Drug Name", "Drug Price", "Quantity Sold", "Drug Category", "Drug Validity Duration", "Batch Number")
        text.insert(END, "{:<20} {:<15} {:<15} {:<20} {:<25} {:<15}\n".format(*headers))
        text.insert(END, "-" * 120 + "\n")

        for sale in sales:
            text.insert(END, "{:<20} {:<15} {:<15} {:<20} {:<25} {:<15}\n".format(*sale))

    def exit_application():
        root.destroy()

    def save_to_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(drugs, file)
            messagebox.showinfo("Save to File", "Drugs saved successfully")

    def load_from_file():
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                global drugs
                drugs = json.load(file)
            messagebox.showinfo("Load from File", "Drugs loaded successfully")

    label0 = Label(main_window, text="PHARMACY MANAGEMENT SYSTEM", bg="black", fg="white", font=("Times", 30))
    label1 = Label(main_window, text="ENTER DRUG NAME", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
    entry1 = Entry(main_window, font=("Times", 12))
    label2 = Label(main_window, text="ENTER DRUG PRICE", bd="2", relief="ridge", height="1", bg="red", fg="white", font=("Times", 12), width=25)
    entry2 = Entry(main_window, font=("Times", 12))
    label3 = Label(main_window, text="ENTER DRUG QUANTITY", bd="2", relief="ridge", bg="red", fg="white", font=("Times", 12), width=25)
    entry3 = Entry(main_window, font=("Times", 12))
    label4 = Label(main_window, text="ENTER DRUG CATEGORY", bd="2", relief="ridge", bg="red", fg="white", font=("Times", 12), width=25)
    entry4 = Entry(main_window, font=("Times", 12))
    label5 = Label(main_window, text="DRUG VALIDITY DURATION Yrs", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
    entry5 = Entry(main_window, font=("Times", 12))
    label6 = Label(main_window, text="BATCH NUMBER", bd="2", relief="ridge", bg="red", fg="white", font=("Times", 12), width=25)
    entry6 = Entry(main_window, font=("Times", 12))

    button1 = Button(main_window, text="ADD DRUG", bg="white", fg="black", width=20, font=("Times", 12), command=adddrug)
    button2 = Button(main_window, text="DELETE DRUG", bg="white", fg="black", width=20, font=("Times", 12), command=open_delete_window)
    button3 = Button(main_window, text="UPDATE DRUG", bg="white", fg="black", width=20, font=("Times", 12), command=open_update_window)
    button4 = Button(main_window, text="SEARCH DRUG", bg="white", fg="black", width=20, font=("Times", 12), command=open_search_window)
    button5 = Button(main_window, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12), command=cleardrug)
    button6 = Button(main_window, text="LIST AVAILABLE DRUGS", bg="white", fg="black", width=20, font=("Times", 12), command=listdrugs)
    button7 = Button(main_window, text="RECORD SALE", bg="white", fg="black", width=20, font=("Times", 12), command=open_sales_window)
    button8 = Button(main_window, text="VIEW SALES HISTORY", bg="white", fg="black", width=20, font=("Times", 12), command=list_sales)
    button9 = Button(main_window, text="SAVE TO FILE", bg="white", fg="black", width=20, font=("Times", 12), command=save_to_file)
    button10 = Button(main_window, text="LOAD FROM FILE", bg="white", fg="black", width=20, font=("Times", 12), command=load_from_file)
    button11 = Button(main_window, text="EXIT", bg="white", fg="black", width=20, font=("Times", 12), command=exit_application)

    label0.grid(columnspan=6, padx=10, pady=10)
    label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
    label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
    label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
    label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
    label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)
    label6.grid(row=6, column=0, sticky=W, padx=10, pady=10)

    entry1.grid(row=1, column=1, padx=40, pady=10)
    entry2.grid(row=2, column=1, padx=10, pady=10)
    entry3.grid(row=3, column=1, padx=10, pady=10)
    entry4.grid(row=4, column=1, padx=10, pady=10)
    entry5.grid(row=5, column=1, padx=10, pady=10)
    entry6.grid(row=6, column=1, padx=10, pady=10)

    button1.grid(row=1, column=4, padx=40, pady=10)
    button2.grid(row=1, column=5, padx=40, pady=10)
    button3.grid(row=2, column=4, padx=40, pady=10)
    button4.grid(row=2, column=5, padx=40, pady=10)
    button5.grid(row=3, column=4, padx=40, pady=10)
    button6.grid(row=3, column=5, padx=40, pady=10)
    button7.grid(row=4, column=4, padx=40, pady=10)
    button8.grid(row=4, column=5, padx=40, pady=10)
    button9.grid(row=5, column=4, padx=40, pady=10)
    button10.grid(row=5, column=5, padx=40, pady=10)
    button11.grid(row=6, column=4, columnspan=2, padx=40, pady=10)

open_main_window()

root.mainloop()
