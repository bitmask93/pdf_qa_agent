import openai

class LLMHandler:
	def __init__(self, api_key, model="gpt-4o-mini"):
		openai.api_key = api_key
        self.model = model

   	def get_answer(self, text_chunks, question):
   		'''
   			Returns answer for a question using the GPT model
   			Input : 
   				text_chunks : text chunks
   				question : Answer to a given question
   			Output : 
   				answer : Answer genrated from the model

   		'''
   		response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
            	{"role": "system", "content": "You are an assistant. Respond only if confident. \
            		Else respond 'Data Not Available'"},
            	{"role": "user", "content": f"Text: {text_chunk}\n\nQuestion: {question}"}
            ],
            )
   		answer = response['choices'][0]['message']['content'].strip()

   		return answer