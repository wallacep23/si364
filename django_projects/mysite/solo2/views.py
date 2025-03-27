from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

class MainView(LoginRequiredMixin, View):
    def get(self,request):
        return render(request,'index.html')
    
    def post(self, request):
        context = {}
        # Get the data from both fields
        field1 = request.POST.get('field1', '')
        field2 = request.POST.get('field2', '')
        field1 = field1.strip()
        field2 = field2.strip() 

        # Concatenate and reverse the result (adjust logic as needed)
        concatenated = field1 + ' ' + field2
        reversed_str = concatenated[::-1]
        context['reversed_string'] = reversed_str

        return render(request, 'index.html', context)