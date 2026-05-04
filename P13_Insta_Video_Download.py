import instaloader

L = instaloader.Instaloader()

post_url = "https://www.instagram.com/p/DUUivmVkiv5/"
shortcode = post_url.split("/")[-2]

post = instaloader.Post.from_shortcode(L.context, shortcode)
L.download_post(post, target="downloads")
print("Download complete!")