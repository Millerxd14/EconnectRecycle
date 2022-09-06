from notifications_app.models import BroadcastNotification


def notifications(request):
    if request.user.is_authenticated:
        notificaciones_usuario = BroadcastNotification.objects.filter(usuario_propietario = request.user, estado = "0").order_by("-id")[:5]
        return {
            'notificaciones': notificaciones_usuario,
            'room_name': 'broadcast'
        }
    else:
        return {
            'notificaciones': '',
            'room_name': 'broadcast'
        }