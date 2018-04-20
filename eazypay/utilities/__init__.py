def track_third_party(request, data, reaponce):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for is not None:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', None)
    return ip

  
  
   # ThirdPartyRequest.objects.create(request=data, ip=ip, responce=reaponce)