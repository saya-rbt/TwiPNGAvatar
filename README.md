# TwiPNGAvatar
Python script used to upload transparent PNG avatar if needed. Can also upload PNG images without transparency for higher image quality.

## How to use
**IMPORTANT ! Requires [tweepy](https://github.com/tweepy/tweepy) !**

1. Put the png image into the same folder as the script
2. Run the script with Python 3
3. Copy-paste the link the console returns you into your browser
4. Log yourself in
5. Copy the code the website returns you
6. Paste it into the console
7. Type the name of your image (e.g. 'avatar.png' but **type it without the quotes**)
8. Done! Your profile picture now features a png avatar with transparency!

## Troubleshooting

If you don't get the message "Avatar changed!", then the upload hasn't been successful. It's either that the name you wrote is incorrect or that Twitter is having trouble.

If your avatar changed but you still have a jpg, it is because your image doesn't have transparency, so Twitter converts it automatically. You can edit it with GIMP/photoshop/ anything just to add 1 transparent pixel, it is enough.

If when you try to erase, instead of transparency, you get white, it might be because you haven't got any alpha canal on your image. With GIMP, you can correct this by doing Layer > Transparency > Add an alpha canal (might be differently named, if so let me know).

Have fun!
