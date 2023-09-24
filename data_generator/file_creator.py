import sys
sys.path.append('./')
from data_generator.generate_canadian_pii import *
import csv
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_fake_data_csv(data_structure, line_count, obfuscate):
    match data_structure:
        case "Name, SIN":
            name = "Name+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'SIN']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', sin=True)
            for value in data_list:
                data.append(value)

        case "Name, Date of Birth, SIN":
            name = "Name+DOB+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'SIN', 'Date of Birth']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', sin=True, date_of_birth=True)
            for value in data_list:
                data.append(value)

        case "Name, Date of Birth, Address, SIN":
            name = "Name+DOB+ADDR+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'SIN', 'Date of Birth', 'Address']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', sin=True, date_of_birth=True, address=True)
            for value in data_list:
                data.append(value)

        case "Name, Drivers License":
            name = "Name+License" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'License Number']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', drivers_license=True)
            for value in data_list:
                data.append(value)
        
        case "Name, Date of Birth, Drivers License":
            name = "Name+License+DOB" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'License Number', 'Date of Birth']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', drivers_license=True, date_of_birth=True)
            for value in data_list:
                data.append(value)
        
        case "Name, Date of Birth, Address, Drivers License":
            name = "Name+License+DOB+ADDR" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'License Number', 'Date of Birth', 'Address']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', drivers_license=True, date_of_birth=True, address=True)
            for value in data_list:
                data.append(value)
            
    # Create Random Filename with descriptor
    filename = f"{name}-{line_count}lines-{randint(1000,9999)}.csv"
    # Write to file
    with open(f"./pii_data/{filename}", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print(f"CSV file '{filename}' generated successfully.")

def generate_data_struct(line_count, format, sin=False, drivers_license=False, date_of_birth=False, address=False):
    """_summary_
    Generates data to pass to file creation.
    
    Args:
        line_count (int): lines of data to generate
        format (str): csv, txt, or pdf
        date_of_birth (bool, optional): generate data of birth. Defaults to True.
        address (bool, optional): generate address. Defaults to True.
    """
    name = generate_fake_name()
    dob = generate_fake_date_of_birth()
    data_list = [name,
                 generate_fake_sin() if sin else None,
                 generate_drivers_license(name, dob) if drivers_license else None,
                 dob if date_of_birth else None,
                 generate_fake_address() if address else None]
    data_list = [x for x in data_list if x is not None]
    data_list_csv = [data_list]
    data = ', '.join(data_list)
    data += '\n'
    for i in range(line_count - 1):
        if format == 'txt':
            name = generate_fake_name()
            dob = generate_fake_date_of_birth()
            data_list = [name,
                 generate_fake_sin() if sin else None,
                 generate_drivers_license(name, dob) if drivers_license else None,
                 dob if date_of_birth else None,
                 generate_fake_address() if address else None]
            data_list = [x for x in data_list if x is not None]
            data_temp = ', '.join(data_list)
            if i != line_count - 1:
                data_temp += '\n'
            data += data_temp
        if format == 'csv':
            name = generate_fake_name()
            dob = generate_fake_date_of_birth()
            temp_list = [name,
                 generate_fake_sin() if sin else None,
                 generate_drivers_license(name, dob) if drivers_license else None,
                 dob if date_of_birth else None,
                 generate_fake_address() if address else None]
            data_list_csv.append([x for x in temp_list if x is not None])
    if format == 'txt':
        return data
    if format == 'csv':
        return data_list_csv
    
def generate_fake_data_pdf(data_structure, line_count, obfuscate=False):
    match data_structure:
        case "Name, SIN":
            name = "Name+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'SIN']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', sin=True)
            for value in data_list:
                data.append(value)

        case "Name, Date of Birth, SIN":
            name = "Name+DOB+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'SIN', 'Date of Birth']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', sin=True, date_of_birth=True)
            for value in data_list:
                data.append(value)

        case "Name, Date of Birth, Address, SIN":
            name = "Name+DOB+ADDR+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'SIN', 'Date of Birth', 'Address']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', sin=True, date_of_birth=True, address=True)
            for value in data_list:
                data.append(value)

        case "Name, Drivers License":
            name = "Name+License" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'License Number']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', drivers_license=True)
            for value in data_list:
                data.append(value)
        
        case "Name, Date of Birth, Drivers License":
            name = "Name+License+DOB" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'License Number', 'Date of Birth']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', drivers_license=True, date_of_birth=True)
            for value in data_list:
                data.append(value)
        
        case "Name, Date of Birth, Address, Drivers License":
            name = "Name+License+DOB+ADDR" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'License Number', 'Date of Birth', 'Address']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', drivers_license=True, date_of_birth=True, address=True)
            for value in data_list:
                data.append(value)
    
    num_columns = len(data[0])
    column_width = 100 / num_columns
    table = Table(data)

    pdf = SimpleDocTemplate(f"./pii_data/{name}-{randint(1000,9999)}.pdf", pagesize=letter)
    
    #table.hAlign = "LEFT"
    # Define style for table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('SHRINK', (0, 0), (-1, -1), 1),
    ])
    for col in range(num_columns):
        style.add('COLWIDTH', (col, 0), (col, -1), letter[0] * (column_width / 100))

    # Apply style to table
    table.setStyle(style)

    # Build the PDF
    elements = [table]
    pdf.build(elements)


def generate_fake_data_txt(data_structure, line_count, obfuscate=False):
    match data_structure:    
        case "Name, Date of Birth, SIN":
            name = "Name+DOB+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = generate_data_struct(line_count, 'txt', sin=True, date_of_birth=True)
        
        case "Name, SIN":
            name = "Name+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = generate_data_struct(line_count, 'txt', sin=True)
        
        case "Name, Date of Birth, Address, SIN":
            name = "Name+DOB+ADDR+SIN" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = generate_data_struct(line_count, 'txt', sin=True, date_of_birth=True, address=True)

        case "Name, Drivers License":
            name = "Name+DL" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = generate_data_struct(line_count, 'txt', drivers_license=True)

        case "Name, Drivers License, Date of Birth":
            name = "Name+DOB+DL" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = generate_data_struct(line_count, 'txt', drivers_license=True, date_of_birth=True)
        
        case "Name, Drivers License, Date of Birth, Address":
            name = "Name+DOB+ADDR+DL" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = generate_data_struct(line_count, 'txt', drivers_license=True, date_of_birth=True, address=True)
    
    # Create Random Filename with descriptor
    filename = f"{name}-{line_count}lines-{randint(1000,9999)}.txt"
    # Write to file
    with open(f"./pii_data/{filename}", 'w', newline='') as txt_file:
        txt_file.write(data)
    print(f"TXT file '{filename}' generated successfully.")

if __name__ == '__main__':
    random_low = 10
    random_high = 10
    ### Generate CSV Data ###
    # SIN
    generate_fake_data_csv("Name, SIN", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_csv("Name, Date of Birth, SIN", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_csv("Name, Date of Birth, Address, SIN", randint(random_low,random_high), obfuscate=False)
    # DL
    generate_fake_data_csv("Name, Drivers License", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_csv("Name, Date of Birth, Drivers License", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_csv("Name, Date of Birth, Address, Drivers License", randint(random_low,random_high), obfuscate=False)
    
    ### Generate TXT Data ###
    # SIN
    generate_fake_data_txt("Name, SIN", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_txt("Name, Date of Birth, SIN", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_txt("Name, Date of Birth, Address, SIN", randint(random_low,random_high), obfuscate=False)
    # DL
    generate_fake_data_txt("Name, Drivers License", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_txt("Name, Drivers License, Date of Birth", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_txt("Name, Drivers License, Date of Birth, Address", randint(random_low,random_high), obfuscate=False)

    ### Generate PDF Data ###
    # SIN
    generate_fake_data_pdf("Name, SIN", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_pdf("Name, Date of Birth, SIN", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_pdf("Name, Date of Birth, Address, SIN", randint(random_low,random_high), obfuscate=False)
    # DL
    generate_fake_data_pdf("Name, Drivers License", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_pdf("Name, Date of Birth, Drivers License", randint(random_low,random_high), obfuscate=False)
    generate_fake_data_pdf("Name, Date of Birth, Address, Drivers License", randint(random_low,random_high), obfuscate=False)