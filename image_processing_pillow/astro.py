from PIL import Image

astro_img = Image.open('astro.jpg')
astro_edit = astro_img.resize((400, 400))
astro_edit.save("astro_edit.png")
astro_edit.show()

astro_img.thumbnail((400, 200))
astro_img.save('thumbnail.png')
astro_img.show()
