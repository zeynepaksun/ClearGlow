import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functions import add_user, add_product, add_routine, add_favourite, check_user, fetch_products, fetch_routines, fetch_favourites
import sqlite3

class ClearGlowApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("ClearGlow - Skincare Tool")
        self.curr_user = None

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1) 

        self.create_login()
    
    def create_login(self):
        self.clear()
        self.frame_login = tk.Frame(self.root)
        self.frame_login.pack()

        tk.Label(self.frame_login, text="Username:").grid(row=0, column=0)
        self.entry_username = tk.Entry(self.frame_login)
        self.entry_username.grid(row=0, column=1)

        tk.Label(self.frame_login, text="Password:").grid(row=1, column=0)
        self.entry_password = tk.Entry(self.frame_login)
        self.entry_password.grid(row=1, column=1)

        self.btn_login = tk.Button(self.frame_login, text="Login", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2)
        
        self.btn_signup = tk.Button(self.frame_login, text="Signup", command=self.create_signup)
        self.btn_signup.grid(row=3, column=0, columnspan=2)

    def create_signup(self):
        self.clear()

        self.frame_signup = tk.Frame(self.root)
        self.frame_signup.pack()

        tk.Label(self.frame_signup, text="Username:").grid(row=0, column=0)
        self.new_entry_username = tk.Entry(self.frame_signup)
        self.new_entry_username.grid(row=0, column=1)

        tk.Label(self.frame_signup, text="Password:").grid(row=1, column=0)
        self.new_entry_password = tk.Entry(self.frame_signup)
        self.new_entry_password.grid(row=1, column=1)

        self.btn_signup = tk.Button(self.frame_signup, text="Signup", command=self.signup)
        self.btn_signup.grid(row=2, column=0, columnspan=2)
        
        self.btn_back_to_login = tk.Button(self.frame_signup, text="Back to Login", command=self.create_login)
        self.btn_back_to_login.grid(row=3, column=0, columnspan=2)

    def create_main(self):
        self.clear()

        self.label_user_id = tk.Label(self.root, text=f"User ID: {self.curr_user}")
        self.label_user_id.pack()

        self.controlTab = ttk.Notebook(self.root)

        self.first_tab = ttk.Frame(self.controlTab)
        self.second_tab = ttk.Frame(self.controlTab)
        self.third_tab = ttk.Frame(self.controlTab)

        self.controlTab.add(self.first_tab, text="Products")
        self.controlTab.add(self.second_tab, text="Routines")
        self.controlTab.add(self.third_tab, text="Favourites")

        self.controlTab.pack(expand=1, fill="both")

        self.create_tab_products()
        self.create_tab_routines()
        self.create_tab_favourites()


    def create_tab_products(self):
        self.products_list = tk.Listbox(self.first_tab)
        self.products_list.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.frame_add_prod = tk.Frame(self.first_tab)
        self.frame_add_prod.grid(row=1, column=0, columnspan=2, sticky="ew")

        tk.Label(self.frame_add_prod, text="Name:").grid(row=0, column=0, sticky="e")
        self.entry_product_name = tk.Entry(self.frame_add_prod)
        self.entry_product_name.grid(row=0, column=1, sticky="w")

        tk.Label(self.frame_add_prod, text="Brand:").grid(row=0, column=2, sticky="e")
        self.entry_product_brand = tk.Entry(self.frame_add_prod)
        self.entry_product_brand.grid(row=0, column=3, sticky="w")

        tk.Label(self.frame_add_prod, text="Type:").grid(row=1, column=0, sticky="e")
        self.entry_product_type = tk.Entry(self.frame_add_prod)
        self.entry_product_type.grid(row=1, column=1, sticky="w")

        tk.Label(self.frame_add_prod, text="Skin Type:").grid(row=1, column=2, sticky="e")
        self.entry_product_skin_type = tk.Entry(self.frame_add_prod)
        self.entry_product_skin_type.grid(row=1, column=3, sticky="w")

        tk.Label(self.frame_add_prod, text="Description:").grid(row=2, column=0, columnspan=4, sticky="e")
        self.entry_product_description = tk.Entry(self.frame_add_prod)
        self.entry_product_description.grid(row=2, column=1, columnspan=3, sticky="ew")

        self.btn_add_product = tk.Button(self.frame_add_prod, text="Add Product", command=self.add_product)
        self.btn_add_product.grid(row=3, column=0, columnspan=4, pady=10, sticky="nsew")


        self.first_tab.rowconfigure(0, weight=1)
        self.first_tab.columnconfigure(0, weight=1)

        self.get_products()

    def create_tab_routines(self):
        self.routines_list = tk.Listbox(self.second_tab)
        self.routines_list.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.frame_add_routine = tk.Frame(self.second_tab)
        self.frame_add_routine.grid(row=1, column=0, columnspan=2, sticky="ew")

        tk.Label(self.frame_add_routine, text="Name:").grid(row=0, column=0)
        self.entry_routine_name = tk.Entry(self.frame_add_routine)
        self.entry_routine_name.grid(row=0, column=1)

        tk.Label(self.frame_add_routine, text="Description:").grid(row=1, column=0)
        self.entry_routine_description = tk.Entry(self.frame_add_routine)
        self.entry_routine_description.grid(row=1, column=1, columnspan=1, sticky="ew")

        self.btn_add_routine = tk.Button(self.frame_add_routine, text="Add Routine", command=self.add_routine)
        self.btn_add_routine.grid(row=2, column=0, columnspan=2)

        self.second_tab.rowconfigure(0, weight=1)
        self.second_tab.columnconfigure(0, weight=1)
        self.get_routines()       

    def create_tab_favourites(self):
        self.favourites_list = tk.Listbox(self.third_tab)
        self.favourites_list.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.frame_add_favourite = tk.Frame(self.third_tab)
        self.frame_add_favourite.grid(row=1, column=0, columnspan=2, sticky="ew")

        tk.Label(self.frame_add_favourite, text="Product ID:").grid(row=0, column=0)
        self.entry_product_id = tk.Entry(self.frame_add_favourite)
        self.entry_product_id.grid(row=0, column=1)

        self.btn_add_favourite = tk.Button(self.frame_add_favourite, text="Add Favourite", command=self.add_favourite)
        self.btn_add_favourite.grid(row=1, column=0, columnspan=2)

        self.third_tab.rowconfigure(0, weight=1)
        self.third_tab.columnconfigure(0, weight=1)
        self.get_favourites()

    def get_products(self):
        self.products_list.delete(0, tk.END)
        products = fetch_products()

        for p in products:
            product_info = f"Product ID: {p[0]} - Name: {p[1]} - Brand: {p[2]} - Type: {p[3]} - Skin Type: {p[4]} - Description: {p[5]}"
            self.products_list.insert(tk.END, product_info)
            self.products_list.insert(tk.END, "-" * 50) 

    def get_routines(self):
        self.routines_list.delete(0, tk.END)
        routines = fetch_routines()

        for r in routines:
            self.routines_list.insert(tk.END, f"{r[0]}: {r[1]} - {r[2]}")
    
    def get_favourites(self):
        self.favourites_list.delete(0, tk.END)
        user_id = self.curr_user
        favourites = fetch_favourites(user_id)

        for f in favourites:
            self.favourites_list.insert(tk.END, f"User {f[1]}: Product {f[2]}")
    
    def add_product(self):
        name = self.entry_product_name.get()
        brand = self.entry_product_brand.get()
        product_type = self.entry_product_type.get()
        skin_type = self.entry_product_skin_type.get()
        description = self.entry_product_description.get()

        if name and brand and product_type and skin_type and description:
            add_product(name, brand, product_type, skin_type, description)
            self.get_products()
            messagebox.showinfo("Success", "Product Added Successfully!")

            self.entry_product_name.delete(0, tk.END)
            self.entry_product_brand.delete(0, tk.END)
            self.entry_product_type.delete(0, tk.END)
            self.entry_product_skin_type.delete(0, tk.END)
            self.entry_product_description.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill all the fields.")
    
    def add_routine(self):
        name = self.entry_routine_name.get()
        description = self.entry_routine_description.get()

        if name and description:
            add_routine(name, description)
            self.get_routines()
            messagebox.showinfo("Success", "Routine Added Successfully!")

            self.entry_routine_name.delete(0, tk.END)
            self.entry_routine_description.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill all the fields.")

    def add_favourite(self):
        product_id = self.entry_product_id.get()

        if self.curr_user and product_id:
            add_favourite(self.curr_user, int(product_id))
            self.get_favourites()
            messagebox.showinfo("Success", "Favourite Added Successfully!")

            self.entry_product_id.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill all the fields.")            

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        user = check_user(username, password)

        if user:
            self.curr_user = user[0]
            self.create_main()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    def signup(self):
        username = self.new_entry_username.get()
        password = self.new_entry_password.get()

        if username and password:
            try:
                add_user(username, password)
                messagebox.showinfo("Success", "User Added Successfully!")
                self.create_login()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists.")
        else:
            messagebox.showerror("Error", "Please fill all the fields.")

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ClearGlow")
    app = ClearGlowApplication(root)
    root.mainloop()
