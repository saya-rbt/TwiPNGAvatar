# TwiPNGAvatar
Python script used to upload transparent PNG avatar if needed. If you want a PNG avatar, just include a transparent pixel and use the script.

### This script is obsolete, hasn't been updated in years, and only here as archiving purposes.
**Furthermore, someone (@buildknuckle on Twitter) seems to have found a way to upload a transparent avatar on Twitter: https://twitter.com/buildknuckle/status/1190669175594868740**, making this script not only obsolete but also useless.

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

If your avatar changed but you still have a jpg, it is because your image doesn't have transparency, so Twitter converts it automatically. You can edit it with GIMP/photoshop/anything just to add 1 transparent pixel, it is enough.

If when you try to erase, instead of transparency, you get white, it might be because you haven't got any alpha channel on your image. With GIMP, you can correct this by doing Layer > Transparency > Add an alpha channel (might be differently named, if so let me know).

Have fun!
