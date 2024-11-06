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

input_pdfs = [r'C:\Users\NickElgar\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\Nick Elgar - CV 31.10.24 v2.pdf', r'C:\Users\NickElgar\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\Nick Elgar - MS Learn Transcript 06.11.2024.pdf']
output_pdf = r'C:\Users\NickElgar\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\Nick Elgar - CV + Transcript.pdf'

#USED THIS ON HOME PC 
input_pdfs_home = [r'C:\Users\Roma Invicta\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\Nick Elgar - CV 31.10.24 v2.pdf', r'C:\Users\Roma Invicta\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\Nick Elgar - MS Learn Transcript 06.11.2024.pdf']
output_pdf_home = r'C:\Users\Roma Invicta\source\repos\BassBoulder\PythonPySpark\Python Variant\PDFMERGE\PDFs\Nick Elgar - CV + Transcript.pdf'

merge_pdfs(input_pdfs, output_pdf)