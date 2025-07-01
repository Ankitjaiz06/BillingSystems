
from tkinter import *
from tkinter import ttk
import sqlite3
import customtkinter as ctk
from tkinter import messagebox
import os
import tempfile
import smtplib


class RetailBillingSystem:
    def __init__(self):
        self.root = Tk()
        self.root.title("Retail Billing System")
        self.root.geometry('1270x685+90+50')
        self.root.configure(background='steelblue1')
        self.root.iconbitmap('icons.ico')


        ################### Fruits ###############################
        self.Fruits_item_entry_weight = {}
        self.Fruits_item_entry_price = {}
        self.Fruits_item_CTkButton = {}
        self.Fruits_item_Combobox  = {}
        self.Fruits_item_delete_CTkButton = {}
        self.Fruits_all_entry_button_combo_label = []
        self.Fruits_entry_weight_total = {}
        self.all_fruits_and_vegitbles = []

        #####################  Vegeatable ##########################
        self.Vegetable_item_entry_weight = {}
        self.Vegetable_item_entry_price = {}
        self.Vegetable_item_CTkButton = {}
        self.Vegetable_item_Combobox  = {}
        self.Vegetable_item_delete_CTkButton = {}
        self.Vegetables_all_entry_button_combo_label = []
        self.Vegetables_entry_weight_total = {}

        ############################## style for combobox #################
        self.y = ttk.Style(self.root)
        self.y.theme_use('clam')
        # Configure the style of Heading in Treeview widget
        self.y.configure('.', font=('TkDefaultFont', 11, 'italic'))
        ############################# EnD #################################

        ########################### Adding Project Menu and SubMenus #############
        self.menu = Menu(self.root)
        self.project = Menu(self.menu, tearoff=0, bg='darkseagreen') #tearoff make the menu stick close to the Window
        # SubMenu
        self.project.add_command(label="Create New", font=('Comic Sans MS', 8, 'bold'), activebackground='black', command=self.Adding_New_Database)
        # Menu Project
        self.menu.add_cascade(label="Project", menu=self.project)
        self.root.config(menu= self.menu)
        ############################ End #########################################

        ############################################ Retails Billing #########################################################
        Retail_Billing_System_Label = Label(self.root, font=('Comic Sans MS', 20, 'bold'), bg = 'lightskyblue1', fg='Black', text='Retail Billing System',height=1, width=75)
        Retail_Billing_System_Label.place(x = 0, y = 0)
        ################################################ End ###################################################

        ################################################## Customer Details ################################################################
        Customer_Details_LabelFrame = LabelFrame(self.root, relief=RIDGE, text='Customer Details', font=('Comic Sans MS', 15, 'bold'), bg = 'lightskyblue1',
                                             fg="blue", bd=4)
        Customer_Details_LabelFrame.place(x= 0, y= 50, width=1269, height=100)

        Name_Label = Label(Customer_Details_LabelFrame, text= 'Name', font=('Comic Sans MS', 13, 'bold'), bg='lightskyblue1', fg='black')
        Name_Label.place(x=40, y=10)

        self.Name_Entry = Entry(Customer_Details_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 14, 'bold'))
        self.Name_Entry.place(x=110, y=10)
        Name_Entry_line_Canvas = Canvas(Customer_Details_LabelFrame, width=180, height=2.0, bg='Black',highlightthickness=0)
        Name_Entry_line_Canvas.place(x= 110, y=37)

        Phone_Number_Label = Label(Customer_Details_LabelFrame, text= 'Phone Number', font=('Comic Sans MS', 13, 'bold'), bg='lightskyblue1', fg='black')
        Phone_Number_Label.place(x=320, y=10)

        self.Phone_Number_Entry = Entry(Customer_Details_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 14, 'bold'))
        self.Phone_Number_Entry.place(x= 470, y=10)
        Phone_Number_Entry_line_Canvas = Canvas(Customer_Details_LabelFrame, width=180, height=2.0, bg='Black',highlightthickness=0)
        Phone_Number_Entry_line_Canvas.place(x= 470, y=37)

        Bill_Number_Label = Label(Customer_Details_LabelFrame, text= 'Bill Number', font=('Comic Sans MS', 13, 'bold'), bg='lightskyblue1', fg='black')
        Bill_Number_Label.place(x = 690, y=10)

        self.Bill_Number_Entry = Entry(Customer_Details_LabelFrame, highlightthickness=0, width=12, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 14, 'bold'))
        self.Bill_Number_Entry.place(x=820, y=10)
        Bill_Number_Entry_line_Canvas = Canvas(Customer_Details_LabelFrame, width=140, height=2.0, bg='Black',highlightthickness=0)
        Bill_Number_Entry_line_Canvas.place(x= 820, y=37)

        self.serach_Number_Entry = Entry(Customer_Details_LabelFrame, highlightthickness=0, width=8, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 14, 'bold'))
        self.serach_Number_Entry.place(x=1040, y=10)
        Bill_serach_Entry_line_Canvas = Canvas(Customer_Details_LabelFrame, width=100, height=2.0, bg='Black',highlightthickness=0)
        Bill_serach_Entry_line_Canvas.place(x= 1040, y=37)

        Search_Button = ctk.CTkButton(Customer_Details_LabelFrame, text='Search', width=80, height=30,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                    fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command= self.search_bill)
        Search_Button.place(x=1150, y=10)
        ################################################### End Customer Details #######################################

        ##################################### Starting Fruits Items Frame  and LabelFrame ###############################
        self.Fruits_Product_Frame_label = LabelFrame(self.root, relief=RIDGE, text='Fruits Items', font=('Comic Sans MS', 10, 'bold'), bg = 'lightskyblue1',
                                             fg="blue", bd=4)
        self.Fruits_Product_Frame_label.place(x=1, y=158, width=430, height=400)

        ##########################################  End #################################################################

        ##################################    Using canvas scroolbar set fruit frame ###############################
        self.my_canvas_fruits = Canvas(self.Fruits_Product_Frame_label, height=370, width=403)
        self.my_canvas_fruits.pack(side=LEFT)
        # Add A Scrollbars to Canvas
        self.y_scrollbar_fruits = ttk.Scrollbar(self.Fruits_Product_Frame_label, orient=VERTICAL, command=self.my_canvas_fruits.yview)
        self.y_scrollbar_fruits.pack(side=RIGHT, fill=Y)
        # Configure the canvas
        self.main_frame_inner_fruits = Frame(self.my_canvas_fruits, bg='lightskyblue1')
        self.my_canvas_fruits.configure(yscrollcommand=self.y_scrollbar_fruits.set)
        self.main_frame_inner_fruits.bind("<Configure>", lambda e: self.my_canvas_fruits.config(scrollregion=self.my_canvas_fruits.bbox(ALL)))

        self.main_frame_Fruits = Frame(self.main_frame_inner_fruits,bg='lightskyblue1')
        self.main_frame_Fruits.pack(expand=1, fill=BOTH)
        # self.main_frame_Fruits.pack()
        def scroll_wheel(event):
            self.my_canvas_fruits.yview_scroll(int(-1*(event.delta/120)),'units')

        self.my_canvas_fruits.bind_all('<MouseWheel>', scroll_wheel)
        ######################## End ######################################################

        ######################################### Some Extra Fill Fruits ######################################################
        Fill_Fruit_Label = Label(self.main_frame_Fruits, text='Fill Fruit', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black')
        Fill_Fruit_Label.place(x=10, y=0)

        self.Fill_Fruit_Entry = Entry(self.main_frame_Fruits, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=9)
        self.Fill_Fruit_Entry.place(x=90,y=0)
        self.Fill_Fruit_Entry_line_canvas = Canvas(self.main_frame_Fruits, width=90, height=2.0, bg='Black',highlightthickness=0)
        self.Fill_Fruit_Entry_line_canvas.place(x=90, y=25)

        Fruit_Price_Label = Label(self.main_frame_Fruits, text='Fruit Price', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black')
        Fruit_Price_Label.place(x=180, y=0)

        self.Fruit_Price_Entry = Entry(self.main_frame_Fruits, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=6)
        self.Fruit_Price_Entry.place(x=270,y=0)
        self.Fruit_Price_Entry_line_canvas = Canvas(self.main_frame_Fruits, width=60, height=2.0, bg='Black',highlightthickness=0)
        self.Fruit_Price_Entry_line_canvas.place(x=270, y=25)

        self.Fruits_Submit_Button = ctk.CTkButton(self.main_frame_Fruits, text='Submit', width=15, height=8,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=self.Extra_Fruits_Inserted_Data)
        self.Fruits_Submit_Button.place(x=345, y=0)
        self.Auto_Fruits_Enrty_Label_Button_Created()
        ############################################  End ############################################################################

        ################################    Vegetable ################################################
        ##################################### Starting Vegeatable Items Frame  and LabelFrame ###############################
        self.Vegetable_Product_Frame_label = LabelFrame(self.root, relief=RIDGE, text='Vegetable Items', font=('Comic Sans MS', 10, 'bold'), bg = 'lightskyblue1',
                                             fg="blue", bd=4)
        self.Vegetable_Product_Frame_label.place(x=435, y=158, width=430, height=400)

        ##########################################  End #################################################################

        ##################################    Using canvas scroolbar set Vegetable frame ###############################
        self.my_canvas_vegetable = Canvas(self.Vegetable_Product_Frame_label, height=370, width=403)
        self.my_canvas_vegetable.pack(side=LEFT)
        # Add A Scrollbars to Canvas
        self.y_scrollbar_vegetable = ttk.Scrollbar(self.Vegetable_Product_Frame_label, orient=VERTICAL, command=self.my_canvas_vegetable.yview)
        self.y_scrollbar_vegetable.pack(side=RIGHT, fill=Y)
        # Configure the canvas
        self.main_frame_inner_vegetable = Frame(self.my_canvas_vegetable, bg='lightskyblue1')
        self.my_canvas_vegetable.configure(yscrollcommand=self.y_scrollbar_vegetable.set)
        self.main_frame_inner_vegetable.bind("<Configure>", lambda e: self.my_canvas_vegetable.config(scrollregion=self.my_canvas_vegetable.bbox(ALL)))

        self.main_frame_Vegetable = Frame(self.main_frame_inner_vegetable,bg='lightskyblue1')
        self.main_frame_Vegetable.pack(expand=1, fill=BOTH)
        # self.main_frame_Fruits.pack()
        def scroll_wheel(event):
            self.my_canvas_vegetable.yview_scroll(int(-1*(event.delta/120)),'units')

        self.my_canvas_vegetable.bind_all('<MouseWheel>', scroll_wheel)
        ######################## End ######################################################

        ######################################### Some Extra Fill Vegetable ######################################################
        Fill_Vegetable_Label = Label(self.main_frame_Vegetable, text='Fill Vege', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black')
        Fill_Vegetable_Label.place(x=10, y=5)

        self.Fill_Vegetable_Entry = Entry(self.main_frame_Vegetable, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=9)
        self.Fill_Vegetable_Entry.place(x=90,y=5)
        self.Fill_Vegetable_Entry_line_canvas = Canvas(self.main_frame_Vegetable, width=90, height=2.0, bg='Black',highlightthickness=0)
        self.Fill_Vegetable_Entry_line_canvas.place(x=90, y=30)

        Vegetable_Price_Label = Label(self.main_frame_Vegetable, text='Vege Price', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black')
        Vegetable_Price_Label.place(x=180, y=5)

        self.Vegetable_Price_Entry = Entry(self.main_frame_Vegetable, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=6)
        self.Vegetable_Price_Entry.place(x=270,y=5)
        self.Vegetable_Price_Entry_line_canvas = Canvas(self.main_frame_Vegetable, width=60, height=2.0, bg='Black',highlightthickness=0)
        self.Vegetable_Price_Entry_line_canvas.place(x=270, y=30)

        self.Vegetable_Submit_Button = ctk.CTkButton(self.main_frame_Vegetable, text='Submit', width=15, height=8,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=self.Extra_Vegetable_Inserted_Data)
        self.Vegetable_Submit_Button.place(x=345, y=5)
        self.Auto_Vegetable_Enrty_Label_Button_Created()
        ############################################  End ############################################################################

        ######################### Bill Area Text frame #########################################
        self.bill_frame = Frame(self.root, bg='lightskyblue1')
        self.bill_frame.place(x=870, y=158, width=395, height=400)

        bill_area_Label = Label(self.bill_frame, text='Bill Area', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        bill_area_Label.pack(fill=X)

        # Create a vertical scrollbar
        scrollbar = Scrollbar(self.bill_frame, orient=VERTICAL)
        scrollbar.place(x=376, y=30, height=370)

        # Create the text area
        self.text_area = Text(self.bill_frame, height=23, width=49)

        # Associate the scrollbar with the text area
        self.text_area.config(yscrollcommand=scrollbar.set)

        # Place the text area
        self.text_area.place(x=0, y=30, height=370, width=376)

        # Set the scrollbar to control the y-scrolling of the text area
        scrollbar.config(command=self.text_area.yview)


        ###################################### End ####################################

        ######################################## Bill Menu label Frame #####################
        ####################################### fruits Tax label button ######################
        Bill_menu_LabelFrame = LabelFrame(self.root, relief=RIDGE, text='Bill Menu', font=('Comic Sans MS', 12, 'bold'), bg = 'lightskyblue1',
                                             fg="blue", bd=4)
        Bill_menu_LabelFrame.place(x= 0, y= 560, width=1269, height=104)

        fruits_price_bill_Label = Label(Bill_menu_LabelFrame, text='Fruit Price bill', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        fruits_price_bill_Label.place(x=10, y=10)

        self.fruits_price_bill_entry = Entry(Bill_menu_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=10)
        self.fruits_price_bill_entry.place(x=210,y=10)
        self.fruits_price_bill_entry_line_canvas = Canvas(Bill_menu_LabelFrame, width=100, height=2.0, bg='Black',highlightthickness=0)
        self.fruits_price_bill_entry_line_canvas.place(x=210, y=35)

        fruits_price_tax_Label = Label(Bill_menu_LabelFrame, text='Fruit Price Tax', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        fruits_price_tax_Label.place(x=340, y=10)

        self.fruits_calculate_price_bill_entry = Entry(Bill_menu_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=8)
        self.fruits_calculate_price_bill_entry.place(x=510,y=10)
        self.fruits_calculate_price_bill_entry_line_canvas = Canvas(Bill_menu_LabelFrame, width=75, height=2.0, bg='Black',highlightthickness=0)
        self.fruits_calculate_price_bill_entry_line_canvas.place(x=510, y=35)

        self.fruits_price_tax_entry = Entry(Bill_menu_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=6)
        self.fruits_price_tax_entry.place(x=600,y=10)
        self.fruits_price_tax_entry_line_canvas = Canvas(Bill_menu_LabelFrame, width=60, height=2.0, bg='Black',highlightthickness=0)
        self.fruits_price_tax_entry_line_canvas.place(x=600, y=35)

        self.tax_update_fruits = ctk.CTkButton(Bill_menu_LabelFrame, text='Update', width=10, height=20,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=lambda:self.show_data_in_tax_fruits(update_value=self.fruits_price_tax_entry.get()))
        self.tax_update_fruits.place(x=670, y=10)
        self.show_data_in_tax_fruits()

        ############################################## vegetable tax label button ############################
        vegetable_price_bill_Label = Label(Bill_menu_LabelFrame, text='Vegetable Price bill', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        vegetable_price_bill_Label.place(x=10, y=45)

        self.vegetable_price_bill_entry = Entry(Bill_menu_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=10)
        self.vegetable_price_bill_entry.place(x=210,y=45)
        self.vegetable_price_bill_entry_line_canvas = Canvas(Bill_menu_LabelFrame, width=100, height=2.0, bg='Black',highlightthickness=0)
        self.vegetable_price_bill_entry_line_canvas.place(x=210, y=70)

        vegetable_price_tax_Label = Label(Bill_menu_LabelFrame, text='Vegetable Price Tax', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        vegetable_price_tax_Label.place(x=340, y=45)

        self.vegetable_calculated_price_tax_entry = Entry(Bill_menu_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=8)
        self.vegetable_calculated_price_tax_entry.place(x=510,y=45)
        vegetable_calculated_price_tax_entry_line_canvas = Canvas(Bill_menu_LabelFrame, width=75, height=2.0, bg='Black',highlightthickness=0)
        vegetable_calculated_price_tax_entry_line_canvas.place(x=510, y=70)

        self.vegetable_price_tax_entry = Entry(Bill_menu_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=6)
        self.vegetable_price_tax_entry.place(x=600,y=45)
        vegetable_price_tax_entry_line_canvas = Canvas(Bill_menu_LabelFrame, width=60, height=2.0, bg='Black',highlightthickness=0)
        vegetable_price_tax_entry_line_canvas.place(x=600, y=70)

        self.tax_update_vegetable= ctk.CTkButton(Bill_menu_LabelFrame, text='Update', width=10, height=20,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=lambda:self.show_data_in_tax_vegetable(update_value=self.vegetable_price_tax_entry.get()))
        self.tax_update_vegetable.place(x=670, y=46)
        self.show_data_in_tax_vegetable()

        ########################################## button frame #######################################
        button_frame = Frame(Bill_menu_LabelFrame, bg='steelblue1', height=70, width=500)
        button_frame.place(x=750, y=1)
        ###################################################### Total Button Area ################################
        self.total_Button = ctk.CTkButton(button_frame, text='Total', width=60, height=40,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=self.total_bill_fruits)
        self.total_Button.place(x=20, y=20)
        ##################################################### Bill button Area ############################################
        self.bill_Button = ctk.CTkButton(button_frame, text='Bill', width=60, height=40,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=self.bill_area)
        self.bill_Button.place(x=120, y=20)
        #################################################### Email button area #############################################
        self.email_Button = ctk.CTkButton(button_frame, text='Email', width=60, height=40,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=self.send_email)
        self.email_Button.place(x=220, y=20)
        ################################################## Print button Area #######################################
        self.print_Button = ctk.CTkButton(button_frame, text='Print', width=60, height=40,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=self.print_bill)
        self.print_Button.place(x=320, y=20)
        ################################################ clear Button Area #########################################
        self.clear_Button = ctk.CTkButton(button_frame, text='Clear', width=60, height=40,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'))
        self.clear_Button.place(x=420, y=20)
        self.submit_data()

        self.root.mainloop()
        ####################################### End #######################################


    ############################### Fruits def function Start ######################################
    def Auto_Fruits_Enrty_Label_Button_Created(self):
    #     # ########################### Delete Command ###########################
    #     # connection = sqlite3.connect('MaterialsDetails.db')
    #     # cursor = connection.cursor()
    #     # ###### Fetch data from the database
    #     # cursor.execute("Delete from tbl_materials")
    #     # data = cursor.fetchall()
    #     # print(data)
    #     # connection.commit()
    #     # connection.close()
    #     ##########################  Close ######################################


    #     ##########################  Inserted Data Command ###########################
        # connection = sqlite3.connect('materials.db')
        # cursor = connection.cursor()
        # ######## Insert data into the database
        # cursor.execute("INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (1, 'Mango', 60)")
        # cursor.execute("INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (2, 'Orange', 80)")
        # cursor.execute("INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (3, 'Apple', 90)")
        # cursor.execute("INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (4, 'Banana', 70)")
        # cursor.execute("INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (5, 'Papaya', 50)")
        # cursor.execute("INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (6, 'Kiwi', 30)")
        # cursor.execute("INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (7, 'Coconut', 50)")
        # cursor.execute("INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (8, 'Watermilon', 30)")
        # ####### Fetch data from the database
        # # cursor.execute("SELECT ItemsDetails, Price FROM tbl_materials_fruits ORDER BY ItemsID")
        # data = cursor.fetchall()
        # print(data)
        # connection.commit()
        # connection.close()
        ########################################### Close ###############################

        ################################## Show Data Command ############################
        connection = sqlite3.connect('materials.db')
        cursor = connection.cursor()
        ######### Fetch data from the database #######################################
        cursor.execute("SELECT ItemsDetails, Price, ItemsID FROM tbl_materials_fruits ORDER BY ItemsID")
        self.data = cursor.fetchall()
        self.place_y = 40
        x_plus = 20

        for ItemsDetails, Price, ItemsID in self.data:

            def update_price_items(Fruits_Items_Id_Number = ItemsID, Fruits_Items_details_name = ItemsDetails):
                Fruits_Items_details_name_given = Fruits_Items_details_name
                Fruits_Items_price_given = self.Fruits_item_entry_price[Fruits_Items_Id_Number].get()
                connection = sqlite3.connect('materials.db')
                cursor = connection.cursor()
                ######## Insert data into the database
                cursor.execute(f"update tbl_materials_fruits set price={Fruits_Items_price_given} where ItemsDetails='{Fruits_Items_details_name_given}'")
                connection.commit()
                connection.close()

            def Delete_Extra_Fruits(Fruits_Items_Id_Number_deleted = ItemsID):
                connection = sqlite3.connect('materials.db')
                cursor = connection.cursor()
                cursor.execute(f"delete from tbl_materials_fruits where ItemsID={Fruits_Items_Id_Number_deleted}")
                cursor.execute(f"update tbl_materials_fruits set ItemsID=ItemsID - 1 where ItemsID >='{Fruits_Items_Id_Number_deleted}'")
                connection.commit()
                connection.close()
                for Delete_Data in self.Fruits_all_entry_button_combo_label:
                    Delete_Data.place_forget()
                self.Auto_Fruits_Enrty_Label_Button_Created()


            Creating_auto_fruitsLabel = Label(self.main_frame_Fruits, text=ItemsDetails, font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black')
            Creating_auto_fruitsLabel.place(x=10+ x_plus, y=10+self.place_y)
            self.Fruits_all_entry_button_combo_label.append(Creating_auto_fruitsLabel)

            self.Fruits_item_entry_weight[ItemsID] = Entry(self.main_frame_Fruits, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=10)
            self.Fruits_item_entry_weight[ItemsID].place(x=70+ x_plus,y=10+self.place_y)
            self.Fruits_all_entry_button_combo_label.append(self.Fruits_item_entry_weight[ItemsID])

            self.Fruits_item_entry_weight_line_canvas = Canvas(self.main_frame_Fruits, width=100, height=2.0, bg='Black',highlightthickness=0)
            self.Fruits_item_entry_weight_line_canvas.place(x= 70+ x_plus, y=35+self.place_y)
            self.Fruits_all_entry_button_combo_label.append(self.Fruits_item_entry_weight_line_canvas)

            self.Fruits_item_entry_price[ItemsID] = Entry(self.main_frame_Fruits, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=10)
            self.Fruits_item_entry_price[ItemsID].place(x=250+ x_plus,y=10+self.place_y)
            self.Fruits_all_entry_button_combo_label.append(self.Fruits_item_entry_price[ItemsID])
            self.Fruits_item_entry_price[ItemsID].insert(0, Price)

            self.Fruits_item_entry_price_line_canvas = Canvas(self.main_frame_Fruits, width=70, height=2.0, bg='Black',highlightthickness=0)
            self.Fruits_item_entry_price_line_canvas.place(x= 250+ x_plus, y=35+self.place_y)
            self.Fruits_all_entry_button_combo_label.append(self.Fruits_item_entry_price_line_canvas)

            self.Fruits_item_CTkButton[ItemsID] = ctk.CTkButton(self.main_frame_Fruits, text='Update', width=20, height=10,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                        fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=update_price_items)
            self.Fruits_item_CTkButton[ItemsID].place(x=323+ x_plus, y=10+self.place_y)
            self.Fruits_all_entry_button_combo_label.append(self.Fruits_item_CTkButton[ItemsID])

            self.Fruits_item_Combobox [ItemsID] = ttk.Combobox(self.main_frame_Fruits, font=("Comic Sans MS", 8, 'bold'), width=5)
            self.Fruits_item_Combobox [ItemsID]['values'] = ('Kg', 'Gm')
            self.Fruits_item_Combobox [ItemsID].set('Kg')
            self.Fruits_item_Combobox [ItemsID].place(x=185+ x_plus,y=10+self.place_y, height=26)
            self.Fruits_all_entry_button_combo_label.append(self.Fruits_item_Combobox [ItemsID])

            self.Fruits_entry_weight_total[ItemsDetails] = (self.Fruits_item_entry_weight[ItemsID], self.Fruits_item_entry_price[ItemsID], self.Fruits_item_Combobox [ItemsID], ItemsDetails)

            self.Fruits_item_delete_CTkButton[ItemsID] = ctk.CTkButton(self.main_frame_Fruits, text='X', width=10, height=10,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                        fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',10, 'bold'), command=Delete_Extra_Fruits)
            self.Fruits_item_delete_CTkButton[ItemsID].place(x=5, y=15+self.place_y)
            self.Fruits_all_entry_button_combo_label.append(self.Fruits_item_delete_CTkButton[ItemsID])

            self.place_y += 40

            if self.place_y < 377:
                self.my_canvas_fruits.configure(scrollregion=(0, 0, 408, 376))
                self.my_canvas_fruits.create_window((0, 0), window=self.main_frame_inner_fruits, anchor="nw", height=376, width=408)

            else:
                self.my_canvas_fruits.configure(scrollregion=(0, 0, 408, 16 + self.place_y))
                self.my_canvas_fruits.create_window((0, 0), window=self.main_frame_inner_fruits, anchor="nw", height=16 + self.place_y, width=408)

            self.y_scrollbar_fruits.config(command=self.my_canvas_fruits.yview)

    def Extra_Fruits_Inserted_Data(self):
        connection = sqlite3.connect('materials.db')
        cursor = connection.cursor()
        ######## Insert data into the database #######################
        cursor.execute("SELECT ItemsID FROM tbl_materials_fruits ORDER BY ItemsID desc limit 1")
        Extra_Data = cursor.fetchall()
        if Extra_Data:
            cursor.execute(f"INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES ({int(Extra_Data[0][0])+1}, '{self.Fill_Fruit_Entry.get()}', {self.Fruit_Price_Entry.get()})")
        else:
            cursor.execute(f"INSERT INTO tbl_materials_fruits (ItemsID, ItemsDetails, Price) VALUES (1, '{self.Fill_Fruit_Entry.get()}', {self.Fruit_Price_Entry.get()})")
        connection.commit()
        connection.close()
        #################### Page Refresh Adding Some Data in Fruits ##################
        for Delete_Data in self.Fruits_all_entry_button_combo_label:
            Delete_Data.place_forget()
        self.Auto_Fruits_Enrty_Label_Button_Created()



    ################################  Vegetable def function #########################
    def Auto_Vegetable_Enrty_Label_Button_Created(self):
        ################################## Show Data Command ############################
        connection = sqlite3.connect('materials.db')
        cursor = connection.cursor()
        ######### Fetch data from the database #######################################
        cursor.execute("SELECT ItemsDetails, Price, ItemsID FROM tbl_materials_vegetables ORDER BY ItemsID")
        self.data = cursor.fetchall()
        self.place_y = 40
        x_plus = 20

        for ItemsDetails, Price, ItemsID in self.data:

            def update_vegetable_price_items(Vegetable_Items_Id_Number = ItemsID, Vegetable_Items_details_name = ItemsDetails):
                Vegetable_Items_details_name_given = Vegetable_Items_details_name
                Vegetable_Items_price_given = self.Vegetable_item_entry_price[Vegetable_Items_Id_Number].get()
                connection = sqlite3.connect('materials.db')
                cursor = connection.cursor()
                ######## Insert data into the database
                cursor.execute(f"update tbl_materials_vegetables set price={Vegetable_Items_price_given} where ItemsDetails='{Vegetable_Items_details_name_given}'")
                connection.commit()
                connection.close()

            def Delete_Extra_Vegetable(Vegetable_Items_Id_Number_deleted = ItemsID):
                connection = sqlite3.connect('materials.db')
                cursor = connection.cursor()
                cursor.execute(f"delete from tbl_materials_vegetables where ItemsID={Vegetable_Items_Id_Number_deleted}")
                cursor.execute(f"update tbl_materials_vegetables set ItemsID=ItemsID - 1 where ItemsID >='{Vegetable_Items_Id_Number_deleted}'")
                connection.commit()
                connection.close()
                for Delete_Data in self.Vegetables_all_entry_button_combo_label:
                    Delete_Data.place_forget()
                self.Auto_Vegetable_Enrty_Label_Button_Created()


            Creating_auto_vegetable_Label = Label(self.main_frame_Vegetable, text=ItemsDetails, font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black')
            Creating_auto_vegetable_Label.place(x=10+ x_plus, y=10+self.place_y)
            self.Vegetables_all_entry_button_combo_label.append(Creating_auto_vegetable_Label)

            self.Vegetable_item_entry_weight[ItemsID] = Entry(self.main_frame_Vegetable, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=10)
            self.Vegetable_item_entry_weight[ItemsID].place(x=70+ x_plus,y=10+self.place_y)
            self.Vegetables_all_entry_button_combo_label.append(self.Vegetable_item_entry_weight[ItemsID])

            self.Vegetable_item_entry_weight_line_canvas = Canvas(self.main_frame_Vegetable, width=100, height=2.0, bg='Black',highlightthickness=0)
            self.Vegetable_item_entry_weight_line_canvas.place(x= 70+ x_plus, y=35+self.place_y)
            self.Vegetables_all_entry_button_combo_label.append(self.Vegetable_item_entry_weight_line_canvas)

            self.Vegetable_item_entry_price[ItemsID] = Entry(self.main_frame_Vegetable, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=10)
            self.Vegetable_item_entry_price[ItemsID].place(x=250+ x_plus,y=10+self.place_y)
            self.Vegetables_all_entry_button_combo_label.append(self.Vegetable_item_entry_price[ItemsID])
            self.Vegetable_item_entry_price[ItemsID].insert(0, Price)

            self.Vegetable_item_entry_price_line_canvas = Canvas(self.main_frame_Vegetable, width=70, height=2.0, bg='Black',highlightthickness=0)
            self.Vegetable_item_entry_price_line_canvas.place(x= 250+ x_plus, y=35+self.place_y)
            self.Vegetables_all_entry_button_combo_label.append(self.Vegetable_item_entry_price_line_canvas)


            self.Vegetable_item_CTkButton[ItemsID] = ctk.CTkButton(self.main_frame_Vegetable, text='Update', width=20, height=10,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                        fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=update_vegetable_price_items)
            self.Vegetable_item_CTkButton[ItemsID].place(x=323+ x_plus, y=10+self.place_y)
            self.Vegetables_all_entry_button_combo_label.append(self.Vegetable_item_CTkButton[ItemsID])

            self.Vegetable_item_Combobox [ItemsID] = ttk.Combobox(self.main_frame_Vegetable, font=("Comic Sans MS", 8, 'bold'), width=5)
            self.Vegetable_item_Combobox [ItemsID]['values'] = ('Kg', 'Gm')
            self.Vegetable_item_Combobox [ItemsID].set('Kg')
            self.Vegetable_item_Combobox [ItemsID].place(x=185+ x_plus,y=10+self.place_y, height=26)
            self.Vegetables_all_entry_button_combo_label.append(self.Vegetable_item_Combobox [ItemsID])

            self.Vegetables_entry_weight_total[ItemsDetails] = (self.Vegetable_item_entry_weight[ItemsID], self.Vegetable_item_entry_price[ItemsID], self.Vegetable_item_Combobox [ItemsID], ItemsDetails)

            self.Vegetable_item_delete_CTkButton[ItemsID] = ctk.CTkButton(self.main_frame_Vegetable, text='X', width=10, height=10,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                        fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',10, 'bold'), command=Delete_Extra_Vegetable)
            self.Vegetable_item_delete_CTkButton[ItemsID].place(x=5, y=15+self.place_y)
            self.Vegetables_all_entry_button_combo_label.append(self.Vegetable_item_delete_CTkButton[ItemsID])

            self.place_y += 40

            if self.place_y < 377:
                self.my_canvas_vegetable.configure(scrollregion=(0, 0, 408, 376))
                self.my_canvas_vegetable.create_window((0, 0), window=self.main_frame_inner_vegetable, anchor="nw", height=376, width=408)

            else:
                self.my_canvas_vegetable.configure(scrollregion=(0, 0, 408, 16 + self.place_y))
                self.my_canvas_vegetable.create_window((0, 0), window=self.main_frame_inner_vegetable, anchor="nw", height=16 + self.place_y, width=408)

            self.y_scrollbar_vegetable.config(command=self.my_canvas_vegetable.yview)

    def Extra_Vegetable_Inserted_Data(self):
        connection = sqlite3.connect('materials.db')
        cursor = connection.cursor()
        ######## Insert data into the database #######################
        cursor.execute("SELECT ItemsID FROM tbl_materials_vegetables ORDER BY ItemsID desc limit 1")
        Extra_Data = cursor.fetchall()
        if Extra_Data:
            cursor.execute(f"INSERT INTO tbl_materials_vegetables (ItemsID, ItemsDetails, Price) VALUES ({int(Extra_Data[0][0])+1}, '{self.Fill_Vegetable_Entry.get()}', {self.Vegetable_Price_Entry.get()})")
        else:
            cursor.execute(f"INSERT INTO tbl_materials_vegetables (ItemsID, ItemsDetails, Price) VALUES (1, '{self.Fill_Vegetable_Entry.get()}', {self.Vegetable_Price_Entry.get()})")
        connection.commit()
        connection.close()
        #################### Page Refresh Adding Some Data in Fruits ##################
        for Delete_Data in self.Vegetables_all_entry_button_combo_label:
            Delete_Data.place_forget()
        self.Auto_Vegetable_Enrty_Label_Button_Created()



    def total_bill_fruits(self):
        self.bill_list = set()
        self.all_fruits_and_vegitbles.clear()
        self.total_weight_final1 = 0
        for weight_item, price_item, kg_gm, name_fruits in self.Fruits_entry_weight_total.values():
            if weight_item.get() == "":
                continue
            weight = weight_item.get()
            price = price_item.get()
            combo_kg_gm = kg_gm.get()
            self.fruits_name = name_fruits
            # print(weight, price, combo_kg_gm, fruits_name)

            if combo_kg_gm == "Kg":
                value_in_gm = 1000 * int(weight)
                total_weight_final = int(int(price) / 1000 * value_in_gm)

            else:
                total_weight_final = float(int(price) / 1000 * int(weight))

            connection = sqlite3.connect('materials.db')
            cursor = connection.cursor()
            cursor.execute(f"SELECT ItemsDetails FROM tbl_materials_fruits where ItemsDetails='{self.fruits_name}'")
            data_fruits = cursor.fetchall()
            if data_fruits:
                self.bill_list.add("Fruits Tax")

            self.total_weight_final1 += total_weight_final
            self.all_fruits_and_vegitbles.append((weight_item, price_item, kg_gm, name_fruits, total_weight_final))
        self.fruits_price_bill_entry.delete(0,END)
        self.fruits_price_bill_entry.insert(0,f'{self.total_weight_final1} Rs')

        tax_rate_fruits = float(self.fruits_price_tax_entry.get())
        tax_amount_fruits = float(f'{self.total_weight_final1}')
        # self.inerted_tax_amount_calclated_entry_fruits = tax_rate_fruits * tax_amount_fruits
        self.inerted_tax_amount_calclated_entry_fruits = float(float(tax_amount_fruits/100)*tax_rate_fruits)

        self.rounded_tax_amount_fruits = round(self.inerted_tax_amount_calclated_entry_fruits, 2)

        self.fruits_calculate_price_bill_entry.delete(0, END)
        self.fruits_calculate_price_bill_entry.insert(0, f'{self.rounded_tax_amount_fruits} Rs')

        #####################################   Vegeatble total #########################################
        self.total_weight_final2 = 0

        for weight_item, price_item, kg_gm, name_vegetable in self.Vegetables_entry_weight_total.values():
            if weight_item.get() == "":
                continue
            weight = weight_item.get()
            price = price_item.get()
            combo_kg_gm = kg_gm.get()
            vegetable_name = name_vegetable
            # print(weight, price, combo_kg_gm, fruits_name)

            if combo_kg_gm == "Kg":
                value_in_gm = 1000 * int(weight)
                total_weight_final = int(int(price) / 1000 * value_in_gm)

            else:
                total_weight_final = float(int(price) / 1000 * int(weight))

            connection = sqlite3.connect('materials.db')
            cursor = connection.cursor()
            cursor.execute(f"SELECT ItemsDetails FROM tbl_materials_vegetables where ItemsDetails='{vegetable_name}'")
            data_vegetables = cursor.fetchall()
            if data_vegetables:
                self.bill_list.add("Vegetable Tax")

            self.total_weight_final2 += total_weight_final
            self.all_fruits_and_vegitbles.append((weight_item, price_item, kg_gm, vegetable_name, total_weight_final))

        self.vegetable_price_bill_entry.delete(0,END)
        self.vegetable_price_bill_entry.insert(0,f'{self.total_weight_final2} Rs')

        tax_rate_vegetable = float(self.vegetable_price_tax_entry.get())
        tax_amount_vegetable = float(f'{self.total_weight_final2}')

        # self.inerted_tax_amount_calclated_entry_vegetable = tax_rate_vegetable * tax_amount_vegetable
        self.inerted_tax_amount_calclated_entry_vegetable = float(float(tax_amount_vegetable/100) * tax_rate_vegetable)

        rounded_tax_amount_vegetable = round(self.inerted_tax_amount_calclated_entry_vegetable, 2)

        self.vegetable_calculated_price_tax_entry.delete(0, END)
        self.vegetable_calculated_price_tax_entry.insert(0, f'{rounded_tax_amount_vegetable} Rs')

    def bill_area(self):
        self.total_bill_fruits()
        if self.Name_Entry.get()=='' or self.Phone_Number_Entry.get()=='':
            messagebox.showerror('Error','Customer Details Are Required')
        elif self.fruits_price_bill_entry.get()=='' and self.vegetable_price_bill_entry.get()=='':
            messagebox.showerror('Error','No Products are selected')
        elif self.fruits_price_bill_entry.get()=='0 Rs' and self.vegetable_price_bill_entry.get()=='0 Rs':
            messagebox.showerror('Error','No Products are selected')
        else:
            self.text_area.delete('1.0', END)
            self.text_area.insert(END,'Welcome Customer To Engineer Fruit Seller Shop \n')
            self.text_area.insert("end", f'\n Bill Number: {self.Bill_Number_Entry.get()} \n')
            self.text_area.insert("end", f'\n Customer Name: {self.Name_Entry.get()} \n')
            self.text_area.insert("end", f'\n Customer Phone Number: {self.Phone_Number_Entry.get()} \n')
            self.text_area.insert("end", f'\n ============================================= ')
            self.text_area.insert("end", f'\n Product \t\tQuantity \t Price \t Total Price \n')
            self.text_area.insert("end", f' ============================================= \n')

            for weight_item, price_item, kg_gm, name_fruits_vegetable, total_weight_final in self.all_fruits_and_vegitbles:

                self.text_area.insert("end", f'\n {name_fruits_vegetable}\t\t   {weight_item.get()}{kg_gm.get()}\t    {price_item.get()}Rs \t  {total_weight_final}Rs\n')
            self.text_area.insert("end", f'\n ============================================= \n')

            for text_name in self.bill_list:
                if text_name == "Fruits Tax":
                    self.text_area.insert("end", f' \t\t{text_name}          {self.fruits_calculate_price_bill_entry.get()}')
                elif text_name == "Vegetable Tax":
                    self.text_area.insert("end", f'\n \t\t{text_name}       {self.vegetable_calculated_price_tax_entry.get()}\n')

            # if self.fruits_calculate_price_bill_entry.get() >= '0 Rs':
            #     self.text_area.insert("end", f' \t\tFruits Tax          {self.fruits_calculate_price_bill_entry.get()}')

            # if self.vegetable_calculated_price_tax_entry.get() >= '0 Rs':
            #     self.text_area.insert("end", f'\n \t\tVegetable Tax       {self.vegetable_calculated_price_tax_entry.get()}\n')
            self.text_area.insert("end", f'\n ---------------------------------------------')

            fruits_total_bill_includ = float(self.total_weight_final2)
            vegetable_total_bill_includ = float(self.total_weight_final1)
            self.fruits_calculate_price = float(self.fruits_calculate_price_bill_entry.get().split()[0])  # Remove ' Rs' and convert to float
            self.vegetable_calculated_price = float(self.vegetable_calculated_price_tax_entry.get().split()[0])  # Remove ' Rs' and convert to float
            total_bill_included_tax = fruits_total_bill_includ + vegetable_total_bill_includ + self.fruits_calculate_price + self.vegetable_calculated_price
            self.text_area.insert("end", f'\n Total Bill Included Taxes \t\t\t\t{total_bill_included_tax} Rs')
            self.save_bill()
            self.save_data_alll()

    def show_data_in_tax_fruits(self, update_value=None):
        connection = sqlite3.connect('materials.db')
        cursor = connection.cursor()
        if update_value != None:
            cursor.execute(f"Update tbl_fruits_tax set TaxFruits={self.fruits_price_tax_entry.get()}")
        cursor.execute("SELECT TaxFruits FROM tbl_fruits_tax")
        self.data = cursor.fetchall()
        self.fruits_price_tax_entry.delete(0, END)
        for i in self.data:
            self.fruits_price_tax_entry.insert(0,str(i[0]))
        connection.commit()
        connection.close()

    def show_data_in_tax_vegetable(self, update_value=None):
        connection = sqlite3.connect('materials.db')
        cursor = connection.cursor()
        if update_value != None:
            cursor.execute(f"Update tbl_vegetable_tax set TaxVegetable={self.vegetable_price_tax_entry.get()}")
        cursor.execute("SELECT TaxVegetable FROM tbl_vegetable_tax")
        self.data = cursor.fetchall()
        self.vegetable_price_tax_entry.delete(0, END)
        for i in self.data:
            self.vegetable_price_tax_entry.insert(0,str(i[0]))
        connection.commit()
        connection.close()

    def submit_data(self):
        bill_number = self.Bill_Number_Entry.get()
        connection = sqlite3.connect('materials.db')
        self.cursor = connection.cursor()
        self.cursor.execute("SELECT BillNumber FROM tbl_customer_details order by BillNumber desc limit 1")
        existing_bill = self.cursor.fetchall()
        bill_number = 1
        if existing_bill:
            bill_number = int(existing_bill[0][0]) + 1
        self.Bill_Number_Entry.delete(0, END)
        self.Bill_Number_Entry.insert(0, str(bill_number))
        connection.commit()
        connection.close()

    def save_data_alll(self):
        name = self.Name_Entry.get()
        phone_number = self.Phone_Number_Entry.get()
        bill_number = self.Bill_Number_Entry.get()
        connection = sqlite3.connect('materials.db')
        self.cursor = connection.cursor()
        self.cursor.execute("INSERT INTO tbl_customer_details (SerialID, Name, PhoneNumber, BillNumber) VALUES (?, ?, ?, ?)", (bill_number, name, phone_number, bill_number))
        connection.commit()
        connection.close()

    def print_bill(self):
        if self.text_area.get(1.0, 'end') == '\n':
            messagebox.showerror('Error', 'Bill is empty')
        else:
            file_path = tempfile.mktemp('.txt')
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, 'end'))
            # Specify the printer name as the third argument
            os.startfile(file_path, 'print', 'Printer_Name')

    def send_email(self):

        # if self.text_area.get(1.0, END)=='\n':
        #     messagebox.showerror('Error', 'Bill is empty')
        # else:
        self.top = Toplevel()
        self.top.title('Send Gmail')
        self.top.config(bg='lightskyblue1')
        self.top.geometry('540x620+900+50')
        self.top.resizable(0,0)


        Sender_LabelFrame = LabelFrame(self.top, relief=RIDGE, text='SENDER', font=('Comic Sans MS', 12, 'bold'), bg = 'lightskyblue1',
                                             fg="blue", bd=4)
        Sender_LabelFrame.place(x= 20, y= 10, width=500, height=120)

        sender_Label = Label(Sender_LabelFrame, text="Sender's Email", font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        sender_Label.place(x=10, y=10)

        self.sender_entry = Entry(Sender_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=35)
        self.sender_entry.place(x=150,y=10)
        self.sender_entry_line_canvas = Canvas(Sender_LabelFrame, width=320, height=2.0, bg='Black',highlightthickness=0)
        self.sender_entry_line_canvas.place(x=150, y=35)

        password_Label = Label(Sender_LabelFrame, text="Password", font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        password_Label.place(x=10, y=50)

        self.password_entry = Entry(Sender_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=20, show='*')
        self.password_entry.place(x=150,y=50)
        self.password_entry_line_canvas = Canvas(Sender_LabelFrame, width=200, height=2.0, bg='Black',highlightthickness=0)
        self.password_entry_line_canvas.place(x=150, y=75)

        recipient_LabelFrame = LabelFrame(self.top, relief=RIDGE, text='RECIPIENT', font=('Comic Sans MS', 12, 'bold'), bg = 'lightskyblue1',
                                             fg="blue", bd=4)
        recipient_LabelFrame.place(x= 20, y= 130, width=500, height=490)

        reciever_Label = Label(recipient_LabelFrame, text="Email Address", font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        reciever_Label.place(x=10, y=10)

        self.reciever_entry = Entry(recipient_LabelFrame, highlightthickness=0, relief=FLAT, bg='lightskyblue1', fg='black', font=('yu gothic ui', 12, 'bold'),width=35)
        self.reciever_entry.place(x=150,y=10)
        self.reciever_entry_line_canvas = Canvas(recipient_LabelFrame, width=320, height=2.0, bg='Black',highlightthickness=0)
        self.reciever_entry_line_canvas.place(x=150, y=35)

        message_Label = Label(recipient_LabelFrame, text="Message", font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        message_Label.place(x=10, y=50)

        ######################### Bill Area Text frame #########################################
        self.gmail_bill_frame = Frame(recipient_LabelFrame, bg='lightskyblue1')
        self.gmail_bill_frame.place(x=90, y=50, width=395, height=410)

        gmail_bill_area_Label = Label(self.gmail_bill_frame, text='Bill Area', font=('Comic Sans MS', 11, 'bold'), bg='lightskyblue1', fg='Black', bd=3, relief=GROOVE)
        gmail_bill_area_Label.pack(fill=X)

        # Create a vertical scrollbar
        scrollbar = Scrollbar(self.gmail_bill_frame, orient=VERTICAL)
        scrollbar.place(x=376, y=30, height=370)

        # Create the text area
        self.gmail_text_area = Text(self.gmail_bill_frame, height=23, width=49)

        # Associate the scrollbar with the text area
        self.gmail_text_area.config(yscrollcommand=scrollbar.set)

        # Place the text area
        self.gmail_text_area.place(x=0, y=30, height=370, width=376)

        # Set the scrollbar to control the y-scrolling of the text area
        scrollbar.config(command=self.gmail_text_area.yview)
        self.gmail_text_area.delete(1.0, END)
        self.gmail_text_area.insert(END, self.text_area.get(1.0, END).replace('=','').replace('-',''))


        def send_email_customer():
            print('pp')
            try:
                ob = smtplib.SMTP('smtp.gmail.com', 587)
                ob.starttls()
                ob.login(self.sender_entry.get(), self.password_entry.get())
                message_email = self.gmail_text_area.get(1.0, END)
                ob.sendmail(self.sender_entry.get(), self.receiver_entry.get(), message_email)
                ob.quit()
                messagebox.showinfo('Success', 'Bill is Successfully sent')
            except Exception as e:
                messagebox.showerror('Error', f'An error occurred: {str(e)}')

        self.send_button= ctk.CTkButton(recipient_LabelFrame, text='Send', width=10, height=20,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=send_email_customer())
        self.send_button.place(x=10, y=420)

        self.top.mainloop()


    def search_bill(self):
        for i in os.listdir('bills/'):
            if i.split('.')[0] == self.serach_Number_Entry.get():
                f = open(f'bills/{i}','r')
                self.text_area.delete('1.0',END)
                for data in f:
                    self.text_area.insert(END,data)
                f.close()
                break
        else:
            messagebox.showerror('Error', 'Bill not found')


    if not os.path.exists('bills'):
        os.mkdir('bills')

    def save_bill(self):
        result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
        if result:
            bill_content = self.text_area.get(1.0, END)
            file_path = f'bills/{self.Bill_Number_Entry.get()}.txt'
            with open(file_path, 'w') as file:
                file.write(bill_content)
            messagebox.showinfo('Success', f'Bill number {self.Bill_Number_Entry.get()} is saved successfully')

    ###################   Database Creation ###########################################
    def Adding_New_Database(self):
        self.self.top = Tk()
        self.self.top.title("Add New Database")
        self.self.top.geometry("300x100")
        self.self.top.config(background='steelblue1')

        Create_Database_Label = Label(self.self.top, text='Create Database', font=('Comic Sans MS', 11, 'bold'), bg='steelblue1', fg='Black')
        Create_Database_Label.place(x=10, y=10)

        self.Create_Database_Entry = Entry(self.self.top, highlightthickness=0, relief=FLAT, bg='steelblue1', fg='white', font=('yu gothic ui', 12, 'bold'),width=15)
        self.Create_Database_Entry.place(x=150, y=10)
        self.Create_Database_Entry_line_canvas = Canvas(self.self.top, width=135, height=2.0, bg='Black',highlightthickness=0)
        self.Create_Database_Entry_line_canvas.place(x=150, y=35)

        def Databse_Insert_Data():
            database_name = self.Create_Database_Entry.get()
            connection = sqlite3.connect(f'{database_name}.db')
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE tbl_materials_fruits(
                    ItemsID int NOT NULL,
                    ItemsDetails nvarchar(550) NOT NULL,
                    Price int NOT NULL
                )""")
            cursor.execute("""
                CREATE TABLE tbl_materials_vegetables(
                    ItemsID int NOT NULL,
                    ItemsDetails nvarchar(550) NOT NULL,
                    Price int NOT NULL
                )""")
            cursor.execute("""
                CREATE TABLE tbl_customer_details(
                    SerialID int NOT NULL,
                    Name nvarchar(550) NOT NULL,
                    PhoneNumber int NOT NULL,
                    BillNumber int NOT NULL
                )""")
            cursor.execute("""
                CREATE TABLE tbl_fruits_tax(
                    TaxID int NOT NULL,
                    TaxFruits int NOT NULL
                )""")
            cursor.execute("""
                CREATE TABLE tbl_vegetable_tax(
                    TaxID int NOT NULL,
                    TaxVegetable int NOT NULL
                )""")
            cursor.execute("""
                CREATE TABLE tbl_userdata(
                    username nvarchar(100) NOT NULL,
                    paswword nvarchar(100) NOT NULl
                )""")
            connection.commit()
            connection.close()

        Submit_database_button = ctk.CTkButton(self.self.top, text='Submit', width=14, height=8,corner_radius= 10, border_width=1,border_color='white',border_spacing=2,
                     fg_color='#1F6AA5',hover_color='red', text_color='yellow',font = ('Comic Sans MS',15, 'bold'), command=Databse_Insert_Data)
        Submit_database_button.place(x=120, y=55)

if __name__ == "__main__":
    RetailBillingSystem()

