import sys
from gimage import get_image_url

sys.stdout.write(get_image_url(" ".join(sys.argv[1:])))
