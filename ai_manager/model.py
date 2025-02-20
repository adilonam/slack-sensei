from groq import Groq








class QroqModel:
    def __init__(self ,groq_api_token ):
        self.content = self.read_file('./faq.txt')
        self.client = Groq(api_key=groq_api_token)
       


    def read_file(self , file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"The file at {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_response(self, question):
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"dont use MD syntax just simple text and answer in this context : {self.content}"
                },
                {
                    "role": "user",
                    "content": question
                },
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,  # Set stream to False to get the entire response at once
            stop=None,
        )
        return completion.choices[0].message.content