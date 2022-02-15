from .forms import EmailForm


def email(request):
    form = EmailForm()
    return {
        'form':form
    }