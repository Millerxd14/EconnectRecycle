from notifications_app.models import BroadcastNotification


def notifications(request):
    if request.user.is_authenticated:
        notificaciones_usuario = BroadcastNotification.objects.filter(usuario = request.user)
        return {
            'notificaciones': notificaciones_usuario
        }
    else:
        return {
            'notificaciones': ''
        }