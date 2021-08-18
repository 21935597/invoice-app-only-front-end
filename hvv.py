import sqlite3
from tkinter import *
from sqlite3 import *
#We connect to database
conn = sqlite3.connect("Data_File.db")
#create a cursor
c = conn.cursor()
#Create a table
'''c.execute("""CREATE TABLE debtorsMaster(Account_code integer,Address1 text,Address2 text,Address3 text,Balance integer,SalesYearToDate integer,CostYearToDate integer)""")
c.execute("""CREATE TABLE debtors_transaction(
    Account_code integer,
    Date text,
    TransactionType text,
    DocumentNo integer,
    GrossTransactionValue integer,
    VatValue integer
    )""")
c.execute("""CREATE TABLE stock_master(
    stock_code integer,
    stock_Desciption text,
    cost integer,
    selling_price integer,
    total_purchases_excl_vat integer,
    total_sales_excl_vat integer,
    qty_purchased integer,
    qty_sold integer,
    stock_on_hand integer
    )""")
c.execute("""CREATE TABLE stock_transaction(
    stock_code integer,
    date text,
    transaction_type text,
    Document_no integer,
    qty integer,
    unity_cost integer,
    unit_selli nteger
    )""")
c.execute("""CREATE TABLE invoice_Header(
    invoice_No integer,
    Account_code integer,
    Date integer,
    total_sell_amount_excl_vat integer,
    vat integer,
    Total_cost integer
    )""")
c.execute("""CREATE TABLE invoice_detail(
    invoice_No integer,
    item_No integer,
    stock_code integer,
    qty_sold integer,
    unit_cost integer,
    unit_sell integer,
    disc integer,
    total integer
    )""")'''

#Comit Changes
conn.commit()

#close connection
conn.close()

root = Tk()
#save button function
def SaveButton():
    #We connect to database
    conn = sqlite3.connect("Data_File.db")
    #create a cursor
    c = conn.cursor()
    #clear all text box

   
    #Comit Changes
    conn.commit()

   
  
    
    c.execute("INSERT INTO debtorsMaster VALUES(:Account_code, :Address1, :Address2, :Address3, :Balance, :SalesYearToDate, :CostYearToDate )",
            {
                'Account_code': accountCodeEntry.get(),
                'Address1': Address1Entery.get(),
                'Address2': Address2Entry.get(),
                'Address3': Address3Entry.get(),
                'Balance': BalanceEntry.get(),
                'SalesYearToDate': SalesYearToDateEntry.get(),
                'CostYearToDate': UnitSellEntryEntry.get()  
            })
    c.execute("INSERT INTO debtors_transaction VALUES(:Account_code, :Date, :TransactionType, :DocumentNo, :GrossTransactionValue, :VatValue)",
            {
             'Account_code':AccEntry.get(),
             'Date': dateEntry.get(),
             'TransactionType':TransactionTypeEntry.get(),
             'DocumentNo': DocumentNoEntry.get(),
             'GrossTransactionValue': GrossTransactionValueEntry.get(),
             'VatValue': Vat_ValueEntry.get()
            })
    c.execute("INSERT INTO stock_master VALUES(:stock_code, :stock_Desciption, :cost, :selling_price, :total_purchases_excl_vat, :total_sales_excl_vat, :qty_purchased, :qty_sold, :stock_on_hand)",
            {
                'stock_code': stock_codeEntry.get(),
                'stock_Desciption':stock_DescriptionEntry.get(),
                'cost':costEntry.get(),
                'selling_price': SellPriceEntry.get(),
                'total_purchases_excl_vat': PriceExclVatEntry.get(),
                'total_sales_excl_vat': TotalSale1Entry.get(),
                'qty_purchased': QtyEntry.get(),
                'qty_sold': QtySoldEntry.get(),
                'stock_on_hand': g.get()
            })
    
    c.execute("INSERT INTO stock_transaction VALUES(:stock_code, :date, :transaction_type, :Document_no, :qty, :unity_cost, :unit_selli)",
           {
               'stock_code': StockCodeEntry.get(),
               'date': dateEntry.get(),
               'transaction_type': TransTypeEntry.get(),
               'Document_no': DocNoEntry.get(),
               'qty': qty1Entry.get(),
               'unity_cost': UnitCostEntry.get(),
               'unit_selli': UnitSellEntry.get()
           })
    c.execute("INSERT INTO invoice_Header VALUES(:invoice_No, :Account_code, :Date, :total_sell_amount_excl_vat, :vat,:Total_cost)",
            {
                'invoice_No': InvoiceNoEntry.get(),
                'Account_code': Accountcode1ENtry.get(),
                'Date': Date1Entry.get(),
                'total_sell_amount_excl_vat': TotalSaleEntry.get(),
                'vat': VAT1Entry.get(),
                'Total_cost': TotalCostEntry.get() 
            })
    c.execute("INSERT INTO invoice_detail VALUES(:invoice_No, :item_No, :stock_code, :qty_sold, :unit_cost, :unit_sell, :disc, :total)",
            {
                'invoice_No': InvoiceNo1Entry.get(),
                'item_No':ItemNo1Entry.get(),
                'stock_code': StockCode1Entry.get(),
                'qty_sold': QtySold1Entry.get(),
                'unit_cost': Unit1Entry.get(),
                'unit_sell': UnitSell1Entry.get(),
                'disc': DiscEntry.get(),
                'total': TotalEntry.get()
            })
     #close connection
    conn.close()
    accountCodeEntry.delete(0, END)
    Address1Entery.delete(0, END)
    Address2Entry.delete(0, END)
    Address3Entry.delete(0, END)
    BalanceEntry.delete(0, END)
    SalesYearToDateEntry.delete(0, END)
    UnitSellEntry.delete(0, END)
    AccEntry.delete(0, END)
    DateEntry.delete(0, END)
    TransactionTypeEntry.delete(0, END)
    DocumentNoEntry .delete(0, END)
    GrossTransactionValueEntry.delete(0, END)
    Vat_ValueEntry.delete(0, END)
    stock_codeEntry.delete(0, END)
    stock_DescriptionEntry.delete(0, END)
    costEntry.delete(0, END)
    SellPriceEntry.delete(0, END)
    PriceExclVatEntry.delete(0, END)
    DiscEntry.delete(0, END)
    TotalEntry.delete(0, END)
    UnitSell1Entry.delete(0, END)
    Unit1Entry.delete(0, END)
    StockCode1Entry.delete(0, END)
    ItemNo1Entry.delete(0, END)
    InvoiceNo1Entry.delete(0, END)
    TotalCostEntry.delete(0, END)
    VAT1Entry.delete(0, END)
    TotalSaleEntry.delete(0, END)
    PriceExclVatEntry.delete(0, END)
    SellPriceEntry.delete(0, END)
    QtySold1Entry.delete(0, END)
    QtySoldEntry.delete(0, END)
    QtyEntry.delete(0, END)
    dateEntry.delete(0, END)
    Date1Entry.delete(0, END)
    TotalSale1Entry.delete(0, END)
    StockCodeEntry.delete(0, END)
    qty1Entry.delete(0, END)
    Accountcode1ENtry.delete(0, END)
    TransTypeEntry.delete(0, END)   
    
#show database onscreen
def query():
    #We connect to database
    conn = sqlite3.connect("Data_File.db")
    #create a cursor
    c = conn.cursor()
    #call the database
    c.execute("SELECT *,oid FROM debtorsMaster")
    #table1= c.fetchall()
    c.execute("SELECT *,oid FROM debtors_transaction")
    #table2 =c.fetchall()
    #c.execute("SELECT *,oid FROM stock_master")
    table3 =c.fetchall()
    c.execute("SELECT *,oid FROM stock_transaction")
    #table4 = c.fetchall()
    c.execute("SELECT *,oid FROM invoice_Header")
    #table5 = c.fetchall()
    c.execute("SELECT *,oid FROM invoice_detail")
    table6 = c.fetchall()
    #allTable = str(table1)+ " "+ str(table2)+ " "+str(table3)+" "+str(table4)+" "+str(table5)+" "+str(table6)
    print(table6)
    print_records= ''
    for i in table6[0]:
        print_records += str(i) + "\n"
    myAnswer = Label(root,text=print_records)
    myAnswer.grid(row=6, column=10)
    
    #Comit Changes
    conn.commit()

    #close connection
    conn.close()
#Maintain Debtors
Tittle = Label(text="Debtors Master")
Tittle.grid(row=0,column=1,padx=10,pady=10)
accountCode = Label(text="Account code")
accountCode.grid(row=1, column=0,padx=10,pady=10)
accountCodeEntry = Entry(root)
accountCodeEntry.get()
accountCodeEntry.grid(row=1,column=1,columnspan=3,padx=10,pady=10)
Address1 = Label(text="Address 1")
Address1.grid(row=2, column=0,padx=10,pady=10)
Address1Entery = Entry(root)
Address1Entery.get()
Address1Entery.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
Address2 = Label(text="Address2")
Address2.grid(row=3, column=0,padx=10,pady=10)
Address2Entry = Entry(root)
Address2Entry.get()
Address2Entry.grid(row=3,column=1,columnspan=3,padx=10,pady=10)
Address3 = Label(text="Address3")
Address3.grid(row=4, column=0,padx=10,pady=10)
Address3Entry = Entry(root)
Address3Entry.get()
Address3Entry.grid(row=4,column=1,columnspan=3,padx=10,pady=10)
Balance = Label(text="Balance")
Balance.grid(row=5,column=0,padx=10,pady=10)
BalanceEntry = Entry(root)
BalanceEntry.get()
BalanceEntry.grid(row=5,column=1,columnspan=3,padx=10,pady=10)
SalesYearToDate = Label(text="Sales Year to date")
SalesYearToDate.grid(row=6, column=0,padx=10,pady=10)
SalesYearToDateEntry = Entry(root)
SalesYearToDateEntry.get()
SalesYearToDateEntry.grid(row=6,column=1,columnspan=3,padx=10,pady=10)
CostYearToDate = Label(text="Cost of the year")
CostYearToDate.grid(row=7, column=0,padx=10,pady=10)
UnitSellEntryEntry = Entry(root)
UnitSellEntryEntry.get()
UnitSellEntryEntry.grid(row=7,column=1,columnspan=3,padx=10,pady=10)

#Debtors transaction file
Tittle0 = Label(text="\t")
Tittle0.grid(row=8,column=1,padx=10,pady=10)
Tittle1= Label(text="Debtors transaction file")
Tittle1.grid(row=9,column=1,padx=10,pady=10)
Acc = Label(text="Account code")
Acc.grid(row=10, column=0,padx=10,pady=10)
AccEntry = Entry(root)
AccEntry.get()
AccEntry.grid(row=10,column=1,columnspan=3,padx=10,pady=10)
Date = Label(text="Date")
Date.grid(row=11, column=0,padx=10,pady=10)
DateEntry = Entry(root)
DateEntry.get()
DateEntry.grid(row=11,column=1,columnspan=3,padx=10,pady=10)
TransactionType = Label(text="Transaction type")
TransactionType.grid(row=12, column=0,padx=10,pady=10)
TransactionTypeEntry = Entry(root)
TransactionTypeEntry.get()
TransactionTypeEntry.grid(row=12,column=1,columnspan=3,padx=10,pady=10)
DocumentNo= Label(text="Document No")
DocumentNo.grid(row=13, column=0,padx=10,pady=10)
DocumentNoEntry = Entry(root)
DocumentNoEntry.get()
DocumentNoEntry.grid(row=13,column=1,columnspan=3,padx=10,pady=10)
GrossTransactionValue = Label(text="Gross Transaction Value")
GrossTransactionValue.grid(row=14, column=0,padx=10,pady=10)
GrossTransactionValueEntry = Entry(root)
GrossTransactionValueEntry.get()
GrossTransactionValueEntry.grid(row=14,column=1,columnspan=3,padx=10,pady=10)
Vat_Value = Label(text="Vat Value")
Vat_Value.grid(row=15, column=0,padx=10,pady=10)
Vat_ValueEntry = Entry(root)
Vat_ValueEntry.get()
Vat_ValueEntry.grid(row=15,column=1,columnspan=3)
#Stack Master file
Tittle2 = Label(text="\t")
Tittle2.grid(row=16,column=1,padx=10,pady=10)
Tittle1= Label(text="Stock Master File")
Tittle1.grid(row=17,column=1,padx=10,pady=10)
stock_code= Label(text="Stock Code")
stock_code.grid(row=18, column=0,padx=10,pady=10)
stock_codeEntry = Entry(root)
stock_codeEntry.get()
stock_codeEntry.grid(row=18,column=1,columnspan=3)
stock_Description = Label(text="Stock Description")
stock_Description.grid(row=19, column=0,padx=10,pady=10)
stock_DescriptionEntry = Entry(root)
stock_DescriptionEntry.get()
stock_DescriptionEntry.grid(row=19,column=1,columnspan=3,padx=10,pady=10)
cost= Label(text="cost")
cost.grid(row=10, column=5,padx=10,pady=10)
costEntry = Entry(root)
costEntry.get()
costEntry.grid(row=10,column=6,columnspan=3,padx=10,pady=10)
SellPrice= Label(text="selling price")
SellPrice.grid(row=11, column=5,padx=10,pady=10)
SellPriceEntry = Entry(root)
SellPriceEntry.get()
SellPriceEntry.grid(row=11,column=6,columnspan=3,padx=10,pady=10)
PriceExclVat= Label(text="Total Purchases Excl Vat")
PriceExclVat.grid(row=12, column=5,padx=10,pady=10)
PriceExclVatEntry = Entry(root)
PriceExclVatEntry.get()
PriceExclVatEntry.grid(row=12,column=6,columnspan=3,padx=10,pady=10)
TotalSale1= Label(text="Total Sales Excl Vat")
TotalSale1.grid(row=13, column=5,padx=10,pady=10)
TotalSale1Entry = Entry()
TotalSale1Entry.get()
TotalSale1Entry.grid(row=13,column=6,columnspan=3,padx=10,pady=10)
Qty= Label(text="Qty Purchsed")
Qty.grid(row=14, column=5,padx=10,pady=10)
QtyEntry = Entry()
QtyEntry.get()
QtyEntry.grid(row=14,column=6,columnspan=3,padx=10,pady=10)
QtySold= Label(text="Qty Sold")
QtySold.grid(row=15, column=5,padx=10,pady=10)
QtySoldEntry = Entry()
QtySoldEntry.get()
QtySoldEntry.grid(row=15,column=6,columnspan=3,padx=10,pady=10)
StockOnHand= Label(text="Stock On hand")
StockOnHand.grid(row=10, column=13,padx=10,pady=10)
g = Entry()
g.get()
g.grid(row=10,column=14,columnspan=3,padx=10,pady=10)
#Stock Transaction File
Tittle2 = Label(text="\t")
Tittle2.grid(row=0,column=4,padx=10,pady=10)
Tittle1= Label(text="Stock Transaction File")
Tittle1.grid(row=0,column=5,padx=10,pady=10)
StockCode= Label(text="Stock code")
StockCode.grid(row=1, column=4,padx=10,pady=10)
StockCodeEntry = Entry(root)
StockCodeEntry.get()
StockCodeEntry.grid(row=1,column=5,columnspan=3,padx=10,pady=10)
date= Label(text="Date")
date.grid(row=2, column=4,padx=10,pady=10)
dateEntry = Entry()
dateEntry.get()
dateEntry.grid(row=2,column=5,columnspan=3,padx=10,pady=10)
TransType= Label(text="Transaction Type")
TransType.grid(row=3, column=4,padx=10,pady=10)
TransTypeEntry = Entry(root)
TransTypeEntry.get()
TransTypeEntry.grid(row=3,column=5,columnspan=3,padx=10,pady=10)
DocNo= Label(text="Document Number")
DocNo.grid(row=4, column=4,padx=10,pady=10)
DocNoEntry = Entry(root)
DocNoEntry.get()
DocNo.grid(row=4,column=5,columnspan=3,padx=10,pady=10)
qty1= Label(text="Qty")
qty1.grid(row=5, column=4,padx=10,pady=10)
qty1Entry = Entry(root)
qty1Entry.get()
qty1Entry.grid(row=5,column=5,columnspan=3,padx=10,pady=10)
UnitCost= Label(text="Unit Cost")
UnitCost.grid(row=6, column=4,padx=10,pady=10)
UnitCostEntry = Entry()
UnitCostEntry.get()
UnitCost.grid(row=6,column=5,columnspan=3,padx=10,pady=10)
UnitSell= Label(text="Unit sell")
UnitSell.grid(row=7, column=4,padx=10,pady=10)
UnitSellEntry = Entry()
UnitSellEntry.get()
UnitSellEntry.grid(row=7,column=5,columnspan=3,padx=10,pady=10)
#Invoce Header 
Tittle2 = Label(text="\t")
Tittle2.grid(row=0,column=10,padx=10,pady=10)
Tittle1= Label(text="Invoice Header")
Tittle1.grid(row=0,column=10,padx=10,pady=10)
InvoiceNo= Label(text="Invoice No")
InvoiceNo.grid(row=1, column=8,padx=10,pady=10)
InvoiceNoEntry = Entry()
InvoiceNoEntry.get()
InvoiceNoEntry.grid(row=1,column=9,columnspan=3,padx=10,pady=10)
Accountcode1= Label(text="Account Code")
Accountcode1.grid(row=2, column=8,padx=10,pady=10)
Accountcode1ENtry = Entry(root)
Accountcode1ENtry.get()
Accountcode1ENtry.grid(row=2,column=9,columnspan=3,padx=10,pady=10)
Date1= Label(text="Date")
Date1.grid(row=3, column=8,padx=10,pady=10)
Date1Entry = Entry()
Date1Entry.get()
Date1Entry.grid(row=3,column=9,columnspan=3,padx=10,pady=10)
TotalSale= Label(text="Total Sell Amount Exl VAT")
TotalSale.grid(row=4, column=8,padx=10,pady=10)
TotalSaleEntry = Entry()
TotalSaleEntry.get()
TotalSaleEntry.grid(row=4,column=9,columnspan=3,padx=10,pady=10)
VAT1= Label(text="VAT")
VAT1.grid(row=1, column=8,padx=10,pady=10)
VAT1Entry = Entry()
VAT1Entry.get()
VAT1Entry.grid(row=1,column=9,columnspan=3,padx=10,pady=10)
TotalCost= Label(text="Total Cost")
TotalCost.grid(row=1, column=8,padx=10,pady=10)
TotalCostEntry = Entry()
TotalCostEntry.get()
TotalCostEntry.grid(row=1,column=9,columnspan=3,padx=10,pady=10)
#Invoice Detail
Tittle2 = Label(text="\t")
Tittle2.grid(row=9,column=11,padx=10,pady=10)
Tittle1= Label(text="Invoice Detail")
Tittle1.grid(row=9,column=11,padx=10,pady=10)
InvoiceNo1= Label(text="Invoice No")
InvoiceNo1.grid(row=10, column=10,padx=10,pady=10)
InvoiceNo1Entry = Entry()
InvoiceNo1Entry.get()
InvoiceNo1Entry.grid(row=10,column=11,columnspan=3,padx=10,pady=10)
ItemNo1= Label(text="Item No")
ItemNo1.grid(row=11, column=10,padx=10,pady=10)
ItemNo1Entry = Entry()
ItemNo1Entry.get()
ItemNo1Entry.grid(row=11,column=11,columnspan=3,padx=10,pady=10)
StockCode1= Label(text="Stock code")
StockCode1.grid(row=12, column=10,padx=10,pady=10)
StockCode1Entry = Entry()
StockCode1Entry.get()
StockCode1Entry.grid(row=12,column=11,columnspan=3,padx=10,pady=10)
Qty1= Label(text="Qty Sold")
Qty1.grid(row=13, column=10,padx=10,pady=10)
QtySold1Entry = Entry(root)
QtySold1Entry.get()
QtySold1Entry.grid(row=13,column=11,columnspan=3,padx=10,pady=10)
Unit1= Label(text="unit Cost")
Unit1.grid(row=14, column=10,padx=10,pady=10)
Unit1Entry = Entry()
Unit1Entry.get()
Unit1Entry.grid(row=14,column=11,columnspan=3,padx=10,pady=10)
UnitSell1= Label(text="Unit Sell")
UnitSell1.grid(row=15, column=10,padx=10,pady=10)
UnitSell1Entry = Entry()
UnitSell1Entry.get()
UnitSell1Entry.grid(row=15,column=11,columnspan=3,padx=10,pady=10)
Disc= Label(text="Disc")
Disc.grid(row=1, column=12,padx=10,pady=10)
DiscEntry = Entry(root)
DiscEntry.get()
DiscEntry.grid(row=1,column=13,columnspan=3,padx=10,pady=10)
Total= Label(text="Total")
Total.grid(row=2, column=12,padx=10,pady=10)
TotalEntry = Entry(root)
TotalEntry.get()
TotalEntry.grid(row=2,column=13,columnspan=3,padx=10,pady=10)
SaveButton = Button(root,text="save to Database",command=SaveButton)
SaveButton.grid(row=5, column=10)
ShowRecord =Button(root, text="show record",command=query)
ShowRecord.grid(row=5, column=11)
QuiteButton =Button(root, text="EXIT",command=quit)
QuiteButton.grid(row=5, column=12,)
root.mainloop()