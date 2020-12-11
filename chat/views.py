from django.shortcuts import render

# Create your views here.


# chat room page
def index(request):
    return render(request,'chat/room.html')

# 특정 그룹에 속하는 모든 참가자들 get
def get_participants(group_id=None, group_obj=None, user=None):
    if group_id:
        chatgroup = ChatGroup.objects.get(id=id)
    else:
        chatgroup = group_obj

    temp_participants = []

    for participants in chatgroup.user_set.values_list('username', flat=True):
        if participatns != user:
            temp_participants.append(participants.title())
        temp_participants.append('You')
        return ','.join(temp_participants)

# 내가 속한 방
def room(request, group_id):
    if request.user.groups.filter(id=group_id).exists():
        chatgroup = ChatGroup.objects.get(id=group_id)

        assigned_groups = list(request.user.groups.values_list('id', flat=True))
        groups_participated = ChatGroup.objects.filter(id__in=assigned_groups)
        return render(request, 'chat/room.html',{
            'chatgroup': chatgroup,
            'participants': get_participants(group_obj=chatgroup, user=request.user.username),
            'groups_participated': groups_participated
        })
    else:
        return HttpResponseRedirect(reverse("chat:unauthorized"))

def unauthorized(request):
    return render(request, 'chat/unauthorized.html', {})


async def history(request, room_id):
    await Tortoise.init(**settings.TORTOISE_INIT)
    chat_message = await ChatMessage.filter(room_id=room_id).order_by('date_created').values()
    await Tortoise.close_connections()

    return await sync_to_async(JsonResponse)(chat_message, safe=False)
