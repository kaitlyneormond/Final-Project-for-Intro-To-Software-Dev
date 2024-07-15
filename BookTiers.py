import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json

#Author: Kaitlyn Ormond
#Date Written: 7/15/2024
#Assignment: Final Project
#This is a program meant to store, save, and load a tier list of books.
#The user can add book information, including Title, Author, Genre, Personal Rating(1-5), and Tier.
#Tiers include S-Tier, A-Tier, B-Tier, C-Tier,and D-Tier. Information can be edited or deleted after the book is saved.
#Tier lists can be saved and loaded. 

class BookTierListManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Tier List Manager")
        self.geometry("400x300")
        self.books = []
        self.create_main_window()

    def create_main_window(self):
        self.main_label = tk.Label(self, text="Welcome to Book Tier List Manager")
        self.main_label.pack(pady=10)

        self.add_book_button = tk.Button(self, text="Add Book", command=self.show_add_book_window)
        self.add_book_button.pack(pady=5)

        self.view_tier_list_button = tk.Button(self, text="View Tier List", command=self.show_view_tier_list_window)
        self.view_tier_list_button.pack(pady=5)

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=5)

    def show_add_book_window(self):
        self.add_book_window = tk.Toplevel(self)
        self.add_book_window.title("Add a New Book")

        tk.Label(self.add_book_window, text="Title").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(self.add_book_window)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_book_window, text="Author").grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(self.add_book_window)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_book_window, text="Genre").grid(row=2, column=0, padx=5, pady=5)
        self.genre_entry = tk.Entry(self.add_book_window)
        self.genre_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.add_book_window, text="Personal Rating (1-5)").grid(row=3, column=0, padx=5, pady=5)
        self.rating_entry = tk.Entry(self.add_book_window)
        self.rating_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.add_book_window, text="Tier").grid(row=4, column=0, padx=5, pady=5)
        self.tier_var = tk.StringVar()
        self.tier_dropdown = ttk.Combobox(self.add_book_window, textvariable=self.tier_var, values=["S-Tier", "A-Tier", "B-Tier", "C-Tier", "D-Tier"])
        self.tier_dropdown.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(self.add_book_window, text="Save", command=self.save_book).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self.add_book_window, text="Cancel", command=self.add_book_window.destroy).grid(row=5, column=1, padx=5, pady=5)

    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()
        tier = self.tier_var.get()

        if title and author and genre and rating and tier:
            book = {
                "title": title,
                "author": author,
                "genre": genre,
                "rating": rating,
                "tier": tier
            }
            self.books.append(book)
            self.add_book_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    def show_view_tier_list_window(self):
        self.view_tier_list_window = tk.Toplevel(self)
        self.view_tier_list_window.title("Your Book Tier List")

        self.book_listbox = tk.Listbox(self.view_tier_list_window)
        self.book_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for book in self.books:
            self.book_listbox.insert(tk.END, f"{book['title']} - {book['tier']}")

        self.edit_book_button = tk.Button(self.view_tier_list_window, text="Edit Book", command=self.edit_book)
        self.edit_book_button.pack(pady=5)

        self.delete_book_button = tk.Button(self.view_tier_list_window, text="Delete Book", command=self.delete_book)
        self.delete_book_button.pack(pady=5)

        self.save_to_file_button = tk.Button(self.view_tier_list_window, text="Save to File", command=self.save_to_file)
        self.save_to_file_button.pack(pady=5)

        self.load_from_file_button = tk.Button(self.view_tier_list_window, text="Load from File", command=self.load_from_file)
        self.load_from_file_button.pack(pady=5)

        self.back_button = tk.Button(self.view_tier_list_window, text="Back", command=self.view_tier_list_window.destroy)
        self.back_button.pack(pady=5)

    def edit_book(self):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            selected_book = self.books[selected_index[0]]
            self.show_edit_book_window(selected_book, selected_index[0])

    def show_edit_book_window(self, book, index):
        self.edit_book_window = tk.Toplevel(self)
        self.edit_book_window.title("Edit Book Details")

        tk.Label(self.edit_book_window, text="Title").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(self.edit_book_window)
        self.title_entry.insert(0, book["title"])
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.edit_book_window, text="Author").grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(self.edit_book_window)
        self.author_entry.insert(0, book["author"])
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.edit_book_window, text="Genre").grid(row=2, column=0, padx=5, pady=5)
        self.genre_entry = tk.Entry(self.edit_book_window)
        self.genre_entry.insert(0, book["genre"])
        self.genre_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.edit_book_window, text="Personal Rating (1-5)").grid(row=3, column=0, padx=5, pady=5)
        self.rating_entry = tk.Entry(self.edit_book_window)
        self.rating_entry.insert(0, book["rating"])
        self.rating_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.edit_book_window, text="Tier").grid(row=4, column=0, padx=5, pady=5)
        self.tier_var = tk.StringVar()
        self.tier_dropdown = ttk.Combobox(self.edit_book_window, textvariable=self.tier_var, values=["S-Tier", "A-Tier", "B-Tier", "C-Tier", "D-Tier"])
        self.tier_dropdown.set(book["tier"])
        self.tier_dropdown.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(self.edit_book_window, text="Update", command=lambda: self.update_book(index)).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self.edit_book_window, text="Cancel", command=self.edit_book_window.destroy).grid(row=5, column=1, padx=5, pady=5)

    def update_book(self, index):
        self.books[index] = {
            "title": self.title_entry.get(),
            "author": self.author_entry.get(),
            "genre": self.genre_entry.get(),
            "rating": self.rating_entry.get(),
            "tier": self.tier_var.get()
        }
        self.edit_book_window.destroy()
        self.view_tier_list_window.destroy()
        self.show_view_tier_list_window()

    def delete_book(self):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            del self.books[selected_index[0]]
            self.view_tier_list_window.destroy()
            self.show_view_tier_list_window()

    def save_to_file(self):
        with open("book_tier_list.json", "w") as file:
            json.dump(self.books, file)
        messagebox.showinfo("Save to File", "Book tier list saved successfully.")

    def load_from_file(self):
        try:
            with open("book_tier_list.json", "r") as file:
                self.books = json.load(file)
            self.view_tier_list_window.destroy()
            self.show_view_tier_list_window()
            messagebox.showinfo("Load from File", "Book tier list loaded successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Load from File", "No saved book tier list found.")

if __name__ == "__main__":
    app = BookTierListManager()
    app.mainloop()
