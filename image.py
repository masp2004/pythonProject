from openai import OpenAI

# Set your OpenAI API key directly, not recommended
api_key = "---"

client = OpenAI(api_key=api_key)

response = client.images.generate(
    prompt="A spaceship driving on street",
    n=1,
    size="1024x1024",
)

print(response.data[0].url)
