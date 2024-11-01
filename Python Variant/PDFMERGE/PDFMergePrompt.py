import PyPDF2

def merge_pdfs(pdfInputs, pdfOutput):

    merger = PyPDF2.PdfMerger()

    try:

        for pdf in pdfInputs:

            merger.append(pdf)

 

        with open(pdfOutput, 'wb') as merged_pdf:

            merger.write(merged_pdf)

        

        print(f'Merged PDFs successfully. Output saved to: {pdfOutput}')

    except Exception as e:

        print(f'Error merging PDFs: {e}')

 
print("Please add your URL(s) of the pdf(s), separated by ENTER Key:\n")

pdfInputs = []

while True:
    pdfInput = input()
    if pdfInput == "": 
        print("You have exited the loop")
        break
    else:
        pdfInputs.append(pdfInput)



print(input())

print("\nPlease add the destination URL:\n")
pdfOutput = input()


merge_pdfs(pdfInputs, pdfOutput)