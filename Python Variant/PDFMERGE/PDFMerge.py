import PyPDF2

def merge_pdfs(input_pdfs, output_pdf):

    merger = PyPDF2.PdfMerger()

    try:

        for pdf in input_pdfs:

            merger.append(pdf)

 

        with open(output_pdf, 'wb') as merged_pdf:

            merger.write(merged_pdf)

        

        print(f'Merged PDFs successfully. Output saved to: {output_pdf}')

    except Exception as e:

        print(f'Error merging PDFs: {e}')

 

# Example usage

input_pdfs = [r'C:\Users\NickElgar\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\1.pdf', r'C:\Users\NickElgar\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\2.pdf']
output_pdf = r'C:\Users\NickElgar\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\3.pdf'

#USED THIS ON HOME PC 
input_pdfs_home = [r'C:\Users\Roma Invicta\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\1.pdf', r'C:\Users\Roma Invicta\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\2.pdf']
output_pdf_home = r'C:\Users\Roma Invicta\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\3.pdf'

merge_pdfs(input_pdfs, output_pdf)