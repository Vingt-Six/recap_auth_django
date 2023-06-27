import django
django.setup()

from coco.seed import run

if __name__ == '__main__':
    run()