from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Redirect back to the same page after successful form submission
            return redirect('index')

        else:
            # Log form errors for debugging purposes
            print(form.errors)

        return self.render_to_response({'form': form})


class CvPageView(TemplateView):
    template_name = 'cv.html'
