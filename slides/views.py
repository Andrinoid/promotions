# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from slides.models import *
from copy import copy
from PIL import Image, ImageOps
import os
import StringIO
import json
import uuid


@user_passes_test(lambda user: not user.username, login_url='/slides', redirect_field_name=None)
def frontpage(request):
    return render(request, 'frontpage.html', {'message': 'hello'})


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/slides/')
        else:
            return HttpResponse('Account disabled')
            # Return a 'disabled account' error message
    else:
        return render('adminLogin.html', {'login_error': 'True'})


def logout_user(request):
    logout(request)
    return redirect('/')


def slides(request):
    promotions = Promotion.objects.all()
    return render(request, 'slides.html', {'promotions': promotions})


def promotion(request, promo_id):
    promotion = Promotion.objects.get(pk=promo_id)
    slides = Slide.objects.filter(promotion=promotion)
    return render(request, 'addPromotion.html', {'promoID': promo_id, 'slides': slides})


def show_promotion(request, promo_id):
    try:
        promotion = Promotion.objects.get(pk=promo_id)
    except Promotion.DoesNotExist:
        return render(request, 'noPromotionFound.html')

    slides = Slide.objects.filter(promotion=promotion).exclude(is_active=False).order_by('index')

    return render(request, 'showPromotion.html', {'promoID': promo_id, 'slides': slides})

def show_promotion_demo(request):
    return render(request, 'showPromotionDemo.html')


def api_add_promotion(request):
    promotion = Promotion()
    promotion.name = request.GET['name']
    promotion.author = request.user
    promotion.is_active = 'true' in request.GET['is_active']
    promotion.in_private = 'true' in request.GET['is_private']
    promotion.save()

    response = json.dumps({'success': True, 'promotionID': promotion.pk})
    return HttpResponse(response, content_type='application/json')


# @IMAGE TOOLS
def resize_image(imagefile, sizeXY):
    # Create Pillow image object with uploaded image
    image = Image.open(imagefile)

    # if not RGB, convert
    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')
    thumb = ImageOps.fit(image, sizeXY, Image.ANTIALIAS)

    return thumb


# @IMAGE TOOLS
def validate_image(tail, size):
    max_bytes = 10485760
    # filter file by allowed extensions
    tails = ('gif', 'jpg', 'jpeg', 'png')
    if not tail.lower() in tails:
        return 'Uploaded: %s format not accepted' % tail.upper()
    if size > max_bytes:
        print size
        return 'Uploaded image is to large'
    return False


def api_add_slide(request):
    # Get the promotion we are dealing with
    promotion_id = request.META['HTTP_PK']
    promotion = Promotion.objects.get(pk=promotion_id)
    # validate image
    tail = request.META['CONTENT_TYPE'].split('/')[1]
    filebytes = request.META['CONTENT_LENGTH']
    is_not_valid = validate_image(tail, int(filebytes))

    if is_not_valid:
        response = json.dumps({'success': False, 'errorMsg': is_not_valid})
        return HttpResponse(response, content_type="application/json")

    # save image as file
    image_name = "slide_%s_%s.%s" % (promotion_id, uuid.uuid4(), '.jpg')
    imagefile = StringIO.StringIO(request.body)
    PIL_image = Image.open(imagefile)
    PIL_image.save(os.path.join(settings.MEDIA_ROOT, 'images/' + image_name), 'JPEG', quality=95)

    # save thumb as file
    thumb_name = "slide_thumb_%s_%s.%s" % (promotion_id, uuid.uuid4(), '.jpg')
    PIL_thumb = resize_image(copy(imagefile), (300, 300))
    PIL_thumb.save(os.path.join(settings.MEDIA_ROOT, 'thumbs/' + image_name), 'JPEG', quality=95)

    index = Slide.objects.filter(promotion=promotion).count() + 1

    # new slide
    slide = Slide()
    slide.image = '/media/images/%s' % image_name
    slide.thumb = '/media/thumbs/%s' % image_name
    slide.promotion = promotion
    slide.index = index
    try:
        slide.save()
    except OSError:
        print "Deal with this situation"  # TODO setja viðeigandi response hér. kanski er þetta ekki nauðsynlegt skref

    # Make response
    response = {
        'success': True,
        'data': {
            'image': slide.image,
            'thumb': slide.thumb,
            'id': slide.pk,
            'index': slide.index,
            'is_active': slide.is_active
        }
    }
    return HttpResponse(json.dumps(response), content_type='application/json')


def api_get_slide(request):
    slide_id = request.GET['slideID']
    slides = Slide.objects.filter(pk=slide_id).values()
    for i, val in enumerate(slides):
        slides[i]['date'] = str(slides[i]['date'])

    response = {
        'success': True,
        'data': list(slides)[0]
    }
    return HttpResponse(json.dumps(response), content_type='application/json')


def api_get_slides(request):
    promotion_id = json.loads(request.body)['promoID']
    promotion = Promotion.objects.get(pk=promotion_id)
    slides = Slide.objects.filter(promotion=promotion).order_by('index').values()
    print slides
    # date is not json formatable. must be turned to string before dump
    for i, val in enumerate(slides):
        slides[i]['date'] = str(slides[i]['date'])
    response = {
        'success': True,
        'slides': list(slides)
    }
    return HttpResponse(json.dumps(response), content_type='application/json')


def api_remove_slide(request):
    slide_id = request.GET['slideID']
    slide = Slide.objects.get(pk=slide_id)
    slide.delete()
    return HttpResponse(json.dumps({'success': True}), content_type='application/json')


def api_hide_slide(request):
    slide_id = request.GET['slideID']
    slide = Slide.objects.get(pk=slide_id)
    slide.is_active = False
    slide.save()
    return HttpResponse(json.dumps({'success': True}), content_type='application/json')


def api_show_slide(request):
    slide_id = request.GET['slideID']
    print slide_id
    slide = Slide.objects.get(pk=slide_id)
    slide.is_active = True
    slide.save()
    return HttpResponse(json.dumps({'success': True}), content_type='application/json')


def api_update_slide(request):
    slide_data = json.loads(request.body)['slideData']
    slide_content = json.loads(request.body)['slideContent']

    slide = Slide.objects.get(pk=slide_data['id'])
    slide.headline = slide_content['hl1']
    slide.sub_headline = slide_content['hl2']
    slide.description = slide_content['description']
    slide.matrix = slide_content['matrixCube']
    slide.save()

    response = {
        'success': True,
    }
    return HttpResponse(json.dumps(response), content_type='application/json')



def api_update_indexlist(request):
    promotion_id = json.loads(request.body)['promoID']
    order_list = json.loads(request.body)['slideOrder']
    for item in order_list:
        Slide.objects.filter(pk=item[0]).update(index=item[1])
    return HttpResponse('hi')
