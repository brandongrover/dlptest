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
        
        case "Name, Date of Birth, Address":
            name = "Name+DOB+ADDR" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'Date of Birth', 'Address']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', date_of_birth=True, address=True)
            for value in data_list:
                data.append(value)
        
        case "Name, Random Numbers":
            name = "Name+RANDINT" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'Random Number']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', random_int=True)
            for value in data_list:
                data.append(value)
            
    # Create Random Filename with descriptor
    filename = f"{name}-{line_count}lines-{randint(1000,9999)}.csv"
    # Write to file
    with open(f"./pii_data/{filename}", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print(f"CSV file '{filename}' generated successfully.")

def generate_data_struct(line_count, format, sin=False, drivers_license=False, date_of_birth=False, address=False, random_int=False):
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
                 generate_fake_address() if address else None,
                 generate_random_int() if random_int else None]
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
                 generate_fake_address() if address else None,
                 generate_random_int() if random_int else None]
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
                 generate_fake_address() if address else None,
                 generate_random_int() if random_int else None]
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

        case "Name, Date of Birth, Address":
            name = "Name+DOB+ADDR" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'Date of Birth', 'Address']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', date_of_birth=True, address=True)
            for value in data_list:
                data.append(value)
        
        case "Name, Random Numbers":
            name = "Name+RANDINT" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = [['Name', 'Random Number']] if not obfuscate else []
            data_list = generate_data_struct(line_count, 'csv', random_int=True)
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
    print(f"PDF file '{name}-{randint(1000,9999)}.pdf' generated successfully.")


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
        
        case "Name, Date of Birth, Address":
            name = "Name+DOB+ADDR" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = generate_data_struct(line_count, 'txt', date_of_birth=True, address=True)

        case "Name, Random Numbers":
            name = "Name+RANDINT" if not obfuscate else f"dlp_test_{randint(1000,9999)}"
            data = generate_data_struct(line_count, 'txt', random_int=True)

    # Create Random Filename with descriptor
    filename = f"{name}-{line_count}lines-{randint(1000,9999)}.txt"
    # Write to file
    with open(f"./pii_data/{filename}", 'w', newline='') as txt_file:
        txt_file.write(data)
    print(f"TXT file '{filename}' generated successfully.")

def main_params():
    if not len(sys.argv) > 1:
        print("Please pass a selection type (PDF, CSV, or TXT), a count of files to be created, and lines of PII data.")
        print("py file_creator.py <CSV/PDF/TXT> <File Count> <Lines of PII>")
        sys.exit()
    if sys.argv[1] not in ("CSV", "PDF", "TXT"):
        print("Please Select CSV, PDF, or TXT for the first parameter.")
        sys.exit()
    if sys.argv[2] not in ("DL", "SIN", "NOPII"):
        print("Please Select between Drivers License (DL) and Social Insurance Number (SIN), and No PII (NOPII).")
        sys.exit()
    try:
        if not len(sys.argv) > 3:
            print("Please type a valid number for file count.")
            sys.exit()
        int(sys.argv[3])
    except ValueError:
        print("Please type a valid number for file count.")
        sys.exit()
    try:
        if not len(sys.argv) > 4:
            print("Please type a valid number for PII line count.")
            sys.exit()
        int(sys.argv[4])
    except ValueError:
        print("Please type a valid number for PII line count.")
        sys.exit()

def main():
    main_params()
    match sys.argv[1]:
        case "CSV":
            for _ in range(int(sys.argv[3])):
                if sys.argv[2] == "SIN":
                    generate_fake_data_csv("Name, SIN", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_csv("Name, Date of Birth, SIN", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_csv("Name, Date of Birth, Address, SIN", int(sys.argv[4]), obfuscate=False)
                elif sys.argv[2] == "DL":
                    generate_fake_data_csv("Name, Drivers License", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_csv("Name, Date of Birth, Drivers License", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_csv("Name, Date of Birth, Address, Drivers License", int(sys.argv[4]), obfuscate=False)
                elif sys.argv[2] == "NOPII":
                    generate_fake_data_csv("Name, Date of Birth, Address", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_csv("Name, Random Numbers", int(sys.argv[4]), obfuscate=False)
        case "TXT":
            for _ in range(int(sys.argv[3])):
                if sys.argv[2] == "SIN":    
                    generate_fake_data_txt("Name, SIN", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_txt("Name, Date of Birth, SIN", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_txt("Name, Date of Birth, Address, SIN", int(sys.argv[4]), obfuscate=False)
                elif sys.argv[2] == "DL":
                    generate_fake_data_txt("Name, Drivers License", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_txt("Name, Drivers License, Date of Birth", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_txt("Name, Drivers License, Date of Birth, Address", int(sys.argv[4]), obfuscate=False)
                elif sys.argv[2] == "NOPII":
                    generate_fake_data_txt("Name, Date of Birth, Address", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_txt("Name, Random Numbers", int(sys.argv[4]), obfuscate=False)
        case "PDF":
            for _ in range(int(sys.argv[3])):
                if sys.argv[2] == "SIN":  
                    generate_fake_data_pdf("Name, SIN", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_pdf("Name, Date of Birth, SIN", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_pdf("Name, Date of Birth, Address, SIN", int(sys.argv[4]), obfuscate=False)
                    
                elif sys.argv[2] == "DL":
                    generate_fake_data_pdf("Name, Drivers License", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_pdf("Name, Date of Birth, Drivers License", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_pdf("Name, Date of Birth, Address, Drivers License", int(sys.argv[4]), obfuscate=False)
                elif sys.argv[2] == "NOPII":
                    generate_fake_data_pdf("Name, Date of Birth, Address", int(sys.argv[4]), obfuscate=False)
                    generate_fake_data_pdf("Name, Random Numbers", int(sys.argv[4]), obfuscate=False)
if __name__ == '__main__':
    # Create randomly between 10 and 20 lines of PII in each format
    main()