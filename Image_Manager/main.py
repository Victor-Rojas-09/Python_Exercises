from PIL import Image
from Image_Manager.color.channels import RedChannel

img = Image.open("../data/IMG01.jpg")

op = RedChannel()

img_roja = op.apply(img)

img_roja_pil = Image.fromarray(img_roja.astype("uint8"))

img_roja_pil.show(title="Canal rojo")