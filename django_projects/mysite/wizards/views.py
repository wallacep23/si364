from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from wizards.models import House, Wizard

# Create your views here.


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        hc = House.objects.count()
        wl = Wizard.objects.all()

        ctx = {'house_count': hc, 'wizard_list': wl}
        return render(request, 'wizards/wizard_list.html', ctx)


class HouseView(LoginRequiredMixin, View):
    def get(self, request):
        hl = House.objects.all()
        ctx = {'house_list': hl}
        return render(request, 'wizards/house_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class HouseCreate(LoginRequiredMixin, CreateView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class HouseUpdate(LoginRequiredMixin, UpdateView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class HouseDelete(LoginRequiredMixin, DeleteView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class WizardCreate(LoginRequiredMixin, CreateView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class WizardUpdate(LoginRequiredMixin, UpdateView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class WizardDelete(LoginRequiredMixin, DeleteView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

# class HouseCreate(LoginRequiredMixin, CreateView):
#     template = 'wizards/house_form.html'
#     success_url = reverse_lazy('wizards:all')

#     def get(self, request):
#         form = HouseForm()
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request):
#         form = HouseForm(request.POST)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         house = form.save()
#         return redirect(self.success_url)


# # HouseUpdate has code to implement the get/post/validate/store flow
# # WizardUpdate (below) is doing the same thing with no code
# # and no form by extending UpdateView
# class HouseUpdate(LoginRequiredMixin, UpdateView):
#     model = House
#     success_url = reverse_lazy('wizards:all')
#     template = 'wizards/house_form.html'

#     def get(self, request, pk):
#         house = get_object_or_404(self.model, pk=pk)
#         form = HouseForm(instance=house)
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         house = get_object_or_404(self.model, pk=pk)
#         form = HouseForm(request.POST, instance=house)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         form.save()
#         return redirect(self.success_url)


# class HouseDelete(LoginRequiredMixin, DeleteView):
#     model = House
#     success_url = reverse_lazy('wizards:all')
#     template = 'wizards/house_confirm_delete.html'

#     def get(self, request, pk):
#         house = get_object_or_404(self.model, pk=pk)
#         ctx = {'house': house}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         house = get_object_or_404(self.model, pk=pk)
#         house.delete()
#         return redirect(self.success_url)


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes


# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#createview
