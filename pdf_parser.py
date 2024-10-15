import PyPDF2

class PDFParser:
	def __init__(self, chunk_size=2000):
		self.chunk_size = chunk_size 

	def read_text_from_pdf(self, pdf_path):
		'''
			Description : Reads and extracts text from pdf file
			Input : 
				pdf_path : path for the pdf file
			Output : 
				text : extracted textual information
		'''
		with open(pdf_path,'rb') as file:
			reader = PyPDF2.PdfReader(file)
			text = ""
			for page in reader.pages:
				text += page.extract_text()
		return text

	def generate_text_chunks(self, text):
		'''
			Description : Generates
			Input : 
				text : textual information
			Output : 
				chunks 

		'''
		all_chunks = []
		current_chunk = ""
		for sentence in text.split('. '):
			if len(current_chunk) + len(sentence) <= self.chunk_size:
				current_chunk += sentence + ". "
			else:
				all_chunks.append(current_chunk)
				current_chunk = sentence + ". "

		if(current_chunk):
			all_chunks.append(current_chunk)

		return all_chunks


if __name__ == "__main__":
	pdf_parser = PDFParser(chunk_size=2000)
	parsed_text = pdf_parser.read_text_from_pdf('handbook.pdf')
	#print(parsed_text)
	chunks = pdf_parser.generate_text_chunks(parsed_text)
	#print(chunks)