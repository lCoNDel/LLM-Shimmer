import openai

openai.api_key = "sk-qojyZr6N3fqVB6Q25s8lKc0jesLkOmg_-zFCl5DlPAT3BlbkFJgVUnuCKf9eDpycZkdUj_He5xjz0TgaUt-6nox3_7sA
"
def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
