from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url=reverse_lazy('representation:auth:login'))


class AdminRoleRequiredMixin(LoginRequiredMixin):
    @classmethod
    def get(cls, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(AdminRoleRequiredMixin, cls).get(request, *args, **kwargs)
        else:
            return redirect(reverse('representation:index'))
