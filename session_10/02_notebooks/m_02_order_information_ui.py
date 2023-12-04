"""Provides the user interface elements and components.
No real data validation and processing is done at this point.
"""
import tkinter as tk
from tkinter import ttk

from m_01_basic_ui import BasicApplication

class OrderInformationUI(BasicApplication):
    
    MODEL_TYPE_VALUES = ["Simple Model", "Complex Model", "Premium Model"]
    
    def __init__(self):
        super().__init__()

    # the command for closing the window
    def _close_window(self):
        self._window.destroy()

    # the command for getting data
    def _get_data(self):
        # store results in a dictionary
        result = {}
        
        # get all data of interest
        result["name_entry"] = self._name_entry.get()
        result["quantity_entry"] = self._quantity_entry.get()
        result["is_priority_checkbox"] = self._is_priority_value.get()
        result["model_type_list"] = self._model_type_list.get()
        result["comments_text"] = self._comments_text.get(1.0, tk.END)
        
        # return the result
        return result
        
    # the command for clearing data
    def _clear_data(self):
        # delete text entries
        self._name_entry.delete(0, tk.END)
        self._quantity_entry.delete(0, tk.END)
        
        # uncheck is priority
        self._is_priority_checkbox.deselect()

        # reset model type drop down
        self._model_type_list.set("")
        
        # reset comments text box
        self._comments_text.delete(1.0, tk.END)
        
    # the command for information processing
    def _process_information(self):
        print(self._get_data())
        self._clear_data()
    
    # generating the title area as a label 
    def _init_title_area(self):
        self._title_area_label = tk.Label(self._frame, text = "Please enter the order information")
        self._title_area_label.grid(row = 0, column = 0, columnspan = 2, pady=(10, 15))
        self._title_area_label.configure(font=('Arial', 15))
    
    # generating the command name text entry area
    def _init_name(self):
        name_entry_label = tk.Label(self._frame, text = "Order Name*:")
        self._name_entry = tk.Entry(self._frame, width = 30) 
        
        name_entry_label.grid(row = 1, column = 0, pady=5, sticky="w")
        self._name_entry.grid(row = 1, column = 1, padx=(0, 10), sticky="w")

    # generating the command quantity text entry area
    def _init_quantity(self):
        quantity_label = tk.Label(self._frame, text = "Order Quantity*:")
        self._quantity_entry = tk.Entry(self._frame, width = 30)
        
        quantity_label.grid(row = 2, column = 0,  pady=5, sticky="w")
        self._quantity_entry.grid(row = 2, column = 1, padx=(0, 10), sticky="w")

    # generating the is priority checkbox area
    def _init_is_priority(self):
        is_priority_label = tk.Label(self._frame, text = "Is Priority:")
        self._is_priority_value = tk.IntVar()
        self._is_priority_checkbox = tk.Checkbutton(self._frame, variable = self._is_priority_value)
        
        is_priority_label.grid(row = 3, column = 0, pady= 5, sticky="w")
        self._is_priority_checkbox.grid(row = 3, column = 1, sticky="w")
        
    # generating the model type drop down area
    def _init_model_type(self):
        model_type_label = tk.Label(self._frame, text = "Model Type*:")
        self._model_type_list = ttk.Combobox(
            self._frame,
            state = "readonly",
            values = self.MODEL_TYPE_VALUES
        )
        
        model_type_label.grid(row = 4, column = 0, pady= 5, sticky="w")
        self._model_type_list.grid(row = 4, column = 1, sticky="w")

    # generating the comments text box
    def _init_comments(self):
        model_comments_label = tk.Label(self._frame, text = "Comments:")
        self._comments_text = tk.Text(
            self._frame,
            height = 5
        )
        
        model_comments_label.grid(row = 5, column = 0, pady= 5, sticky="w", columnspan = 2)
        self._comments_text.grid(row = 6, column = 0, pady= 5, sticky="w", columnspan = 2)

    # generating the commands area (Cancel, Save)
    def _init_commands(self):
        self._cancel_button = tk.Button(self._frame, text = "Cancel", width = 10, command = self._close_window)
        self._save_button = tk.Button(self._frame, text = "Save", width = 10, command = self._process_information)
        
        self._cancel_button.grid(row = 7, column = 0 , padx = 10, pady= 5)
        self._save_button.grid(row = 7, column = 1)
                
    def _init_main_window(self):
        # init the superclass behavior
        super()._init_main_window()
        
        # initialize areas of interest
        self._init_title_area()
        self._init_name()
        self._init_quantity()
        self._init_is_priority()
        self._init_model_type()
        self._init_comments()
        self._init_commands()
        
        # reset window geometry
        self._window.geometry("")

if __name__ == "__main__": 
    application = OrderInformationUI()
    application.run()