from huggingface_hub import InferenceClient

def make_picture(prompt,name):
 client = InferenceClient(
    provider="nebius",
    api_key="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",
 )

 image = client.text_to_image(
    prompt,
    model="black-forest-labs/FLUX.1-dev"
 )

 image.save(f"images/{name}")
 print("✅ Rasm saqlandi: output.jpg")

