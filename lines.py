import PyPDF2
from copy import copy



def main():
    input_file = 'example.pdf'
    output_file = 'test_output'
    watermark_file = 'sample_watermark_2.pdf' # The user chooses position of the lines
                    

    with open(input_file, "rb") as filehandle_input:
    # read content of the original file
        pdf = PyPDF2.PdfFileReader(filehandle_input)

        # create a pdf writer object for the output file
        pdf_writer = PyPDF2.PdfFileWriter()
        
        with open(watermark_file, "rb") as filehandle_watermark:
            # read content of the watermark
            watermark = PyPDF2.PdfFileReader(filehandle_watermark)

            # get odd and even pages of the watermark PDF
            odd_watermark = even_watermark = watermark.getPage(0)
            if watermark.numPages > 1:  # Different for odd and even pages
                even_watermark = watermark.getPage(1) 

            # Open output file handle
            with open(output_file, "wb") as filehandle_output:
            
                # TODO: Distinguir entre páginas pares/impares con un pdf watermark con 2 pags
                for page in range(0,pdf.numPages):
                    # choose watermark page
                    watermark = copy(odd_watermark) if page%2 == 0 else copy(even_watermark)
                    # get page of the original PDF
                    page = pdf.getPage(page)
                    
                    # merge the two pages
                    watermark.merge_page(page,True) # Merges and expands page
                    
                    # add page to output file
                    pdf_writer.add_page(watermark)
                
                # write the watermarked file to the new file
                pdf_writer.write(filehandle_output)


if __name__ == '__main__':
    main()
    