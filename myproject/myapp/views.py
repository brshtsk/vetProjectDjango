# myapp/views.py
from django.shortcuts import render
from .forms import TextInputForm
from .utils import my_utility_function, get_response

async def text_input_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            entered_text = form.cleaned_data['text_input']

            response = get_response(entered_text)

            return render(request, 'myapp/preparedWeb/styledMenu.html', {'entered_text': response, 'form': form})

    else:
        form = TextInputForm()

    return render(request, 'myapp/preparedWeb/styledMenu.html', {'form': form})