"""Adds data validation and mock processing.
Adds functionality for error and information messages.
"""
import tkinter.messagebox as tkm

from m_02_order_information_ui import OrderInformationUI

class OrderInformationForm(OrderInformationUI):
    def __init__(self):
        super().__init__()
    
    # the command for showing an error
    def _show_error_message(self, error_message):
        tkm.showerror(parent = self._window,title = "Order Entry Form", message = error_message)

    # the command for showing a processing information
    def _show_info_message(self, information_message):
        tkm.showinfo(parent = self._window, title = "Order Entry Form", message = information_message)
                
    # the command for information processing
    def _process_information(self):        
        data = self._get_data()

        name_entry = data["name_entry"].strip()
        if (len(name_entry) == 0) :
            self._show_error_message("No value has been provided for the Order Name!")
            return
        if (len(name_entry) > 32) :
            self._show_error_message("Order Name must have at most 32 characters!")
            return
        if (not name_entry.isalnum()) :
            self._show_error_message("Order Name must be alphanumeric!")
            return
        name_value = name_entry        

        quantity_entry = data["quantity_entry"].strip()
        quantity_value = None
        if (len(quantity_entry) == 0) :
            self._show_error_message("No value has been provided for the Order Quantity!")
            return
        try:
            quantity_value = int(quantity_entry)
        except ValueError:
            self._show_error_message("Order Quantity must be an integer!")
            return
        if quantity_value <= 0: 
            self._show_error_message("Order Quantity must be greater than zero!")
            return
        
        is_priority_value = data["is_priority_checkbox"] == 1
        
        model_type_list = data["model_type_list"]
        if (model_type_list == "") :
            self._show_error_message("No value has been provided for the Model Type!")
            return
        model_type_value = self.MODEL_TYPE_VALUES.index(model_type_list)
        
        comments_text = data["comments_text"]
        comments_value = comments_text.strip().strip("\n")

        data_processing_message = """The following data has been processed: \n
Order Name: {0}\n
Order Quantity: {1}\n
Is Priority: {2} \n
Model Type: {3} \n
Order Comments: \n {4}
""".format(name_value, quantity_value, is_priority_value, model_type_value, comments_value)
        
        self._show_info_message(data_processing_message)
        
        self._clear_data()
    

if __name__ == "__main__": 
    application = OrderInformationForm()
    application.run()