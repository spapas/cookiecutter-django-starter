from django.contrib.auth import get_user_model
from django.http import HttpResponse


def hijack_form(request):
    return HttpResponse(
        """
        <form action="/hijack-action/" method="GET">
            <input name='username'>
            <button type="submit">Start hijacking</button>
        </form>
    """
    )


def hijack_action(request):
    from django.middleware.csrf import get_token

    username = request.GET.get("username")
    try:
        user = get_user_model().objects.get(username=username)
    except get_user_model().DoesNotExist:
        return HttpResponse(f"User {username} not found", status=404)
    return HttpResponse(
        """
        <form action="/hijack/acquire/" method="post">
            <input type='text' value='{0}' name='user_pk'>
            <input type="hidden" name="csrfmiddlewaretoken" value="{1}">
            <button type="submit">Hijack {2}</button>
        </form>
    """.format(
            user.pk,
            get_token(request),
            user.username,
        )
    )

