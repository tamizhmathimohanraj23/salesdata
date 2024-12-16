
import json
import streamlit as st


def create_sales_report(file_name):
    try:
        with open(file_name, 'r') as file:
            sales_data = json.load(file)

      
            st.title("SALES REPORT")

           
            st.write(f"| {'Item Name':<15} | {'Quantity':<10} | {'Gross Amount':<15} | {'Discount':<10} | {'Net Amount':<15} | {'Tax Amount':<10} | {'Final Amount':<15} |")
            st.write("|" + "-" * 85 + "|")

            total_items_sold = 0
            total_discounts = 0.0
            total_taxes = 0.0
            total_sales = 0.0

            for sale in sales_data:
        
                item = sale.get('item', 'Unknown')
                quantity = sale.get('quantity', 0)
                price_per_unit = sale.get('price_per_unit', 0.0)
                discount = sale.get('discount', 0.0)
                tax_rate = sale.get('tax_rate', 0.0)

              
                gross_amount = quantity * price_per_unit
                discount_amount = gross_amount * discount
                net_amount = gross_amount - discount_amount
                tax_amount = net_amount * tax_rate
                final_amount = net_amount + tax_amount

            
                total_items_sold += quantity
                total_discounts += discount_amount
                total_taxes += tax_amount
                total_sales += final_amount
                st.write(f"| {item:<15} | {quantity:<10} | {gross_amount:<15.2f} | {discount_amount:<10.2f} | {net_amount:<15.2f} | {tax_amount:<10.2f} | {final_amount:<15.2f} |")

           
            st.subheader("SUMMARY")
            st.write(f"Total Items Sold: {total_items_sold}")
            st.write(f"Total Discounts Given: {total_discounts:.2f}")
            st.write(f"Total Taxes Collected: {total_taxes:.2f}")
            st.write(f"Total Sales Amount: {total_sales:.2f}")

    except FileNotFoundError:
        st.error(f"Error: File '{file_name}' not found.")
    except json.JSONDecodeError:
        st.error(f"Error: File '{file_name}' contains invalid JSON.")
    except Exception as e:
        st.error(f"An error occurred: {e}")


file_name = 'SalesData.py'


create_sales_report(file_name)
